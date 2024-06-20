from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import FSMContext

import database as db
from states import create_test, tests

from keyboards import inline
from keyboards import default


@dp.message_handler(CommandStart(), state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    await db.create_table.create_table()
    
    if message.chat.id == message.from_id:
        if len(message.text.split()) == 1:
            if not await db.user.get_user(message.from_id):
                msg = await message.answer("<b>🔥Пройдите тест для себя:</b>")
                await message.answer("<b>📱Где ты зависаешь больше всего?</b>", reply_markup=inline.test_button.social_media(False, msg.message_id + 1))

                await create_test.TestFriend.so_media.set()
            else:
                msg = await message.answer(f"""<b>⭐️Отправьте ссылку на ваш тест друзьям и посмотрите на сколько они хорошо вас знают!\n\nВаша ссылка:</b>\n👥 <code>https://t.me/testyourfriend_bot?start={message.from_user.id}</code>""", reply_markup=inline.test_button.menu(message.message_id + 1))
        else:
            user_id = message.text.split()[1]
            user = await db.tests.get_user(user_id)
            if user:
                if not message.from_id == int(user_id):
                    name = await db.user.get_user(user_id)

                    msg = await message.answer(f"<b>📱Где {name[2]} зависает больше всего?</b>", reply_markup=inline.solve.social_media(message.message_id + 1))
                    await tests.TestFriends.so_media.set()
                    await state.update_data({'id': int(user_id)})
                else:
                    await message.answer("<b>Вы не можете решить тест, который создали сами❌</b>")


@dp.callback_query_handler(lambda call: str(call.data).startswith('test_again'))
async def test_again_handler(call: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_text(chat_id=call.from_user.id, text="<b>📱Где ты зависаешь больше всего?</b>", reply_markup=inline.test_button.social_media(True, call.data.split(':')[1]), message_id=int(call.data.split(':')[1]))
    
    await create_test.TestFriend.so_media.set()


@dp.callback_query_handler(lambda call: str(call.data).startswith('see_result'))
async def results_handler(call: types.CallbackQuery, state: FSMContext):
    result = await db.tests.get_result(call.from_user.id)
    result_user = await db.tests.get_user_result(call.from_user.id)
    
    results = []
    result_middle = 0
    result_user_middle = 0
    
    for i in result_user:
        results.append(float(i[4]))
    
    results = sorted(results)
    
    name = ''

    for y in result_user:
        if str(y[4])[0:5] == str(results[-1])[0:5]:
            name = y[1]
    
    for x in result:
        result_middle += float(x[4])
    
    for l in result_user:
        result_user_middle += float(l[4])
    
    try:    
        result_middle = result_middle / len(result)
    except ZeroDivisionError:
        result_middle = '0.00'

    try:
        result_user_middle = result_user_middle / len(result_user)
    except ZeroDivisionError:
        result_user_middle ='0.00'
    
    try:
        msg = await bot.edit_message_text(chat_id=call.from_user.id, text=f"""<b>📊Мои результаты

🌟 Вы прошли {len(result)} тестов, со средним результатом {str(result_middle)[0:5]}%!
👥 Ваш тест прошли {len(result_user)} раз! Ваши друзья вас знают на {str(result_user_middle)[0:5]}%!
🔥 Ваш лучший друг {name}. Он набрал {str(results[-1])[0:5]}%!</b>""", message_id=int(call.data.split(':')[1]), reply_markup=inline.test_button.back(call.data.split(':')[1]))
    except:
        try:
            msg = await bot.edit_message_text(chat_id=call.from_user.id, text=f"""<b>📊Мои результаты

👥 Ваш тест прошли {len(result_user)} раз! Ваши друзья вас знают на {str(result_user_middle)[0:5]}%!
🔥 Ваш лучший друг {name}. Он набрал {str(results[-1])[0:5]}%!</b>""", message_id=int(call.data.split(':')[1]), reply_markup=inline.test_button.back(call.data.split(':')[1]))
        except:
            msg = await bot.edit_message_text(chat_id=call.from_user.id, text=f"""<b>📊Мои результаты

🌟 Вы прошли {len(result)} тестов, со средним результатом {str(result_middle)[0:5]}%!</b>""", message_id=int(call.data.split(':')[1]), reply_markup=inline.test_button.back(call.data.split(':')[1]))
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('back'), state="*")
async def back_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    
    await bot.edit_message_text(chat_id=call.from_user.id, text=f"""<b>⭐️Отправьте ссылку на ваш тест друзьям и посмотрите на сколько они хорошо вас знают!\n\nВаша ссылка:</b>\n👥 <code>https://t.me/testyourfriend_bot?start={call.from_user.id}</code>""", reply_markup=inline.test_button.menu(call.data.split(':')[1]), message_id=int(call.data.split(':')[1]))
    
    
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('youtube') or str(call.data).startswith('instagram') or str(call.data).startswith('tiktok') or str(call.data).startswith('telegram'), state=create_test.TestFriend.so_media)
async def so_media_handler(call: types.CallbackQuery, state: FSMContext):
    so_media = call.data.split(':')
    await state.update_data({'so_media': so_media[0]})
    
    await bot.edit_message_text(text="<b>🦔Какое животное выберешь?</b>", reply_markup=inline.test_button.animal(int(so_media[1])), message_id=int(so_media[1]), chat_id=call.message.chat.id)
    
    await create_test.TestFriend.animal.set()


@dp.callback_query_handler(lambda call: str(call.data).startswith('dog') or str(call.data).startswith('cat') or str(call.data).startswith('monkey') or str(call.data).startswith('parrot') or str(call.data).startswith('cow') or str(call.data).startswith('frog') or str(call.data).startswith('fox') or str(call.data).startswith('rat'), state=create_test.TestFriend.animal)
async def animal_handler(call: types.CallbackQuery, state: FSMContext):
    animal = call.data.split(':')
    await state.update_data({'animal': animal[0]})
    
    await bot.edit_message_text(text="<b>🎠Куда бы ты хотел(-а) отправиться на выходных?</b>", reply_markup=inline.test_button.place_for_camp(int(animal[1])), message_id=int(animal[1]), chat_id=call.message.chat.id)
    
    await create_test.TestFriend.place_for_camp.set()
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('beach') or str(call.data).startswith('attraction') or str(call.data).startswith('store') or str(call.data).startswith('mountain') or str(call.data).startswith('cruise') or str(call.data).startswith('aquapark') or str(call.data).startswith('cinema') or str(call.data).startswith('theater'), state=create_test.TestFriend.place_for_camp)
async def place_camp_handler(call: types.CallbackQuery, state: FSMContext):
    place = call.data.split(':')
    await state.update_data({'place': place[0]})
    
    await bot.edit_message_text(text="<b>⛅️Какое время года твоё любимое?</b>", reply_markup=inline.test_button.season(int(place[1])), message_id=int(place[1]), chat_id=call.message.chat.id)
    
    await create_test.TestFriend.season.set()
    
    
@dp.callback_query_handler(lambda call: str(call.data).startswith('winter') or str(call.data).startswith('summer') or str(call.data).startswith('fall') or str(call.data).startswith('spring'), state=create_test.TestFriend.season)
async def season_handler(call: types.CallbackQuery, state: FSMContext):
    season = call.data.split(':')
    await state.update_data({'season': season[0]})
    
    await bot.edit_message_text(text="<b>🌪Что выберешь?</b>", reply_markup=inline.test_button.weather(int(season[1])), message_id=int(season[1]), chat_id=call.message.chat.id)
    
    await create_test.TestFriend.weather.set()
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('rain') or str(call.data).startswith('sun') or str(call.data).startswith('cloud') or str(call.data).startswith('moon'), state=create_test.TestFriend.weather)
async def weather_handler(call: types.CallbackQuery, state: FSMContext):
    weather = call.data.split(':')
    await state.update_data({'weather': weather[0]})
    
    await bot.edit_message_text(text="<b>🧁Какой твой любимый десерт?</b>", reply_markup=inline.test_button.cake(int(weather[1])), message_id=int(weather[1]), chat_id=call.message.chat.id)
    
    await create_test.TestFriend.cake.set()
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('cake') or str(call.data).startswith('chocolat') or str(call.data).startswith('cookie') or str(call.data).startswith('donut') or str(call.data).startswith('icecream'), state=create_test.TestFriend.cake)
async def cake_handler(call: types.CallbackQuery, state: FSMContext):
    cake = call.data.split(':')
    await state.update_data({'cake': cake[0]})
    
    await bot.edit_message_text(text="<b>🗓В каком месяце у тебя день рождения?</b>", reply_markup=inline.test_button.month(int(cake[1])), message_id=int(cake[1]), chat_id=call.message.chat.id)
    
    await create_test.TestFriend.month.set()
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('december') or str(call.data).startswith('january') or str(call.data).startswith('february') or str(call.data).startswith('march') or str(call.data).startswith('april') or str(call.data).startswith('may') or str(call.data).startswith('juny') or str(call.data).startswith('july') or str(call.data).startswith('august') or str(call.data).startswith('september') or str(call.data).startswith('october') or str(call.data).startswith('november'), state=create_test.TestFriend.month)
async def month_handler(call: types.CallbackQuery, state: FSMContext):
    month = call.data.split(':')
    message_id = int(month[1]) - 1

    await state.update_data({'month': month[0]})
    
    data = await state.get_data()
    user_id = call.from_user.id
    so_media = data['so_media']
    animal = data['animal']
    place = data['place']
    season = data['season']
    weather = data['weather']
    cake = data['cake']
    month = data['month']
    
    await bot.delete_message(chat_id=call.message.chat.id, message_id=message_id)
    await bot.edit_message_text(text=f"""<b>⭐️Отправьте ссылку на ваш тест друзьям и посмотрите на сколько они хорошо вас знают!\n\nВаша ссылка:</b>\n👥 <code>https://t.me/testyourfriend_bot?start={call.from_user.id}</code>""", message_id=message_id + 1, chat_id=call.message.chat.id, reply_markup=inline.test_button.menu(message_id + 1))
    
    if not await db.user.get_user(call.from_user.id):
        await db.tests.create_test(user_id=user_id,
                                social=so_media,
                                animal=animal,
                                place=place,
                                season=season,
                                weather=weather,
                                cake=cake,
                                month=month)
        
        await db.user.add_user(user_id=call.from_user.id, username=call.from_user.username, name=call.from_user.full_name)
    else:
        await db.tests.update_test(user_id=user_id,
                                social=so_media,
                                animal=animal,
                                place=place,
                                season=season,
                                weather=weather,
                                cake=cake,
                                month=month)
    
    await state.finish()



@dp.callback_query_handler(lambda call: str(call.data).startswith('youtube') or str(call.data).startswith('instagram') or str(call.data).startswith('tiktok') or str(call.data).startswith('telegram'), state=tests.TestFriends.so_media)
async def so_media_friend_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = await db.tests.get_user(data['id'])
    name = await db.user.get_user(data['id'])
    
    so_media = call.data.split(':')
    await state.update_data({'so_media': so_media[0]})
    
    await bot.edit_message_reply_markup(reply_markup=inline.solve.social_media_check(user[1], so_media[0]), message_id=int(so_media[1]), chat_id=call.message.chat.id)
    
    msg = await bot.send_message(chat_id=call.message.chat.id, text=f"<b>🦔Какое животное выберает {name[2]}?</b>", reply_markup=inline.solve.animal(0))
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg.message_id, reply_markup=inline.solve.animal(msg.message_id))
    
    await tests.TestFriends.animal.set()


@dp.callback_query_handler(lambda call: str(call.data).startswith('dog') or str(call.data).startswith('cat') or str(call.data).startswith('monkey') or str(call.data).startswith('parrot') or str(call.data).startswith('cow') or str(call.data).startswith('frog') or str(call.data).startswith('fox') or str(call.data).startswith('rat'), state=tests.TestFriends.animal)
async def animal_friend_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = await db.tests.get_user(data['id'])
    name = await db.user.get_user(data['id'])
    
    animal = call.data.split(':')
    await state.update_data({'animal': animal[0]})
    
    await bot.edit_message_reply_markup(reply_markup=inline.solve.animal_check(user[2], animal[0]), message_id=int(animal[1]), chat_id=call.message.chat.id)
    
    msg = await bot.send_message(chat_id=call.message.chat.id, text=f"<b>🎠Куда бы {name[2]} хотел(-а) отправиться на выходных?</b>", reply_markup=inline.solve.place_for_camp(0))
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg.message_id, reply_markup=inline.solve.place_for_camp(msg.message_id))
    
    await tests.TestFriends.place_for_camp.set()
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('beach') or str(call.data).startswith('attraction') or str(call.data).startswith('store') or str(call.data).startswith('mountain') or str(call.data).startswith('cruise') or str(call.data).startswith('aquapark') or str(call.data).startswith('cinema') or str(call.data).startswith('theater'), state=tests.TestFriends.place_for_camp)
async def place_camp_check_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = await db.tests.get_user(data['id'])
    name = await db.user.get_user(data['id'])
    
    place = call.data.split(':')
    await state.update_data({'place': place[0]})
    
    await bot.edit_message_reply_markup(reply_markup=inline.solve.place_for_camp_check(user[3], place[0]), message_id=int(place[1]), chat_id=call.message.chat.id)
    
    msg = await bot.send_message(chat_id=call.message.chat.id, text=f"<b>⛅️Какое время года любимое для {name[2]}?</b>", reply_markup=inline.solve.season(0))
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg.message_id, reply_markup=inline.solve.season(msg.message_id))
    
    await tests.TestFriends.season.set()
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('winter') or str(call.data).startswith('summer') or str(call.data).startswith('fall') or str(call.data).startswith('spring'), state=tests.TestFriends.season)
async def season_check_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = await db.tests.get_user(data['id'])
    name = await db.user.get_user(data['id'])
    
    season = call.data.split(':')
    await state.update_data({'season': season[0]})
    
    await bot.edit_message_reply_markup(reply_markup=inline.solve.season_check(user[4], season[0]), message_id=int(season[1]), chat_id=call.message.chat.id)
    
    msg = await bot.send_message(chat_id=call.message.chat.id, text=f"<b>🌪Что {name[2]} выбрал(-а)?</b>", reply_markup=inline.solve.weather(0))
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg.message_id, reply_markup=inline.solve.weather(msg.message_id))
    
    await tests.TestFriends.weather.set()
    

@dp.callback_query_handler(lambda call: str(call.data).startswith('rain') or str(call.data).startswith('sun') or str(call.data).startswith('cloud') or str(call.data).startswith('moon'), state=tests.TestFriends.weather)
async def weather_check_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = await db.tests.get_user(data['id'])
    name = await db.user.get_user(data['id'])
    
    weather = call.data.split(':')
    await state.update_data({'weather': weather[0]})
    
    await bot.edit_message_reply_markup(reply_markup=inline.solve.weather_check(user[5], weather[0]), message_id=int(weather[1]), chat_id=call.message.chat.id)
    
    msg = await bot.send_message(chat_id=call.message.chat.id, text=f"<b>🧁Какой у {name[2]} любимый десерт?</b>", reply_markup=inline.solve.cake(0))
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg.message_id, reply_markup=inline.solve.cake(msg.message_id))
    
    await tests.TestFriends.cake.set()
    
    
@dp.callback_query_handler(lambda call: str(call.data).startswith('cake') or str(call.data).startswith('chocolat') or str(call.data).startswith('cookie') or str(call.data).startswith('donut') or str(call.data).startswith('icecream'), state=tests.TestFriends.cake)
async def cake_check_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = await db.tests.get_user(data['id'])
    name = await db.user.get_user(data['id'])
    
    cake = call.data.split(':')
    await state.update_data({'cake': cake[0]})
    
    await bot.edit_message_reply_markup(reply_markup=inline.solve.cake_check(user[6], cake[0]), message_id=int(cake[1]), chat_id=call.message.chat.id)
    
    msg = await bot.send_message(chat_id=call.message.chat.id, text=f"<b>🗓В каком месяце у {name[2]} день рождения?</b>", reply_markup=inline.solve.month(0))
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg.message_id, reply_markup=inline.solve.month(msg.message_id))
    
    await tests.TestFriends.month.set()
    
    
@dp.callback_query_handler(lambda call: str(call.data).startswith('december') or str(call.data).startswith('january') or str(call.data).startswith('february') or str(call.data).startswith('march') or str(call.data).startswith('april') or str(call.data).startswith('may') or str(call.data).startswith('juny') or str(call.data).startswith('july') or str(call.data).startswith('august') or str(call.data).startswith('september') or str(call.data).startswith('october') or str(call.data).startswith('november'), state=tests.TestFriends.month)
async def month_check_handler(call: types.CallbackQuery, state: FSMContext):
    d = await state.get_data()
    user = await db.tests.get_user(d['id'])
    name = await db.user.get_user(d['id'])
    
    month = call.data.split(':')
    await state.update_data({'month': month[0]})
    
    await bot.edit_message_reply_markup(reply_markup=inline.solve.month_check(user[7], month[0]), message_id=int(month[1]), chat_id=call.message.chat.id)
    
    
    data = await state.get_data()
    lst = ['so_media', 'animal', 'place', 'season', 'weather', 'cake', 'month']
    
    user_choices = []
    correct_answers = []
    correct_answers_count = 0
    
    for i in range(7):
        user_choices.append(data[lst[i]])
        correct_answers.append(user[i + 1])
        
    for l in range(7):
        if user_choices[l] == correct_answers[l]:
            correct_answers_count += 1

    result = 100 / 7
    result = result * correct_answers_count
    result = str(result)[0:5]
    
    await db.tests.add_result(call.from_user.id, call.from_user.full_name, name[0], name[2], result)
    await bot.send_message(chat_id=call.message.chat.id, text=f"<b>🌟Вы знаете {name[2]} на {result}%</b>")
    
    try:
        await bot.send_message(chat_id=int(d['id']), text=f"<b>🌟{call.from_user.full_name} прошел ваш тест на {result}%</b>")
    except:
        pass
    
    
    await state.finish()
    
