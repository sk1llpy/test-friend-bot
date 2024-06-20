from aiogram import types


def social_media(started: bool, message_id):
    if started:
        button = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton("❤️YouTube", callback_data=f'youtube:{message_id}'),
                types.InlineKeyboardButton("💙Telegram", callback_data=f'telegram:{message_id}'),
                types.InlineKeyboardButton("💜Instagram", callback_data=f'instagram:{message_id}')
            ],
            [
                types.InlineKeyboardButton("🖤TikTok", callback_data=f'tiktok:{message_id}')
            ],
            [
                types.InlineKeyboardButton("⬅️Назад", callback_data=f'back:{message_id}')
            ]
        ])
    else:
        button = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton("❤️YouTube", callback_data=f'youtube:{message_id}'),
                types.InlineKeyboardButton("💙Telegram", callback_data=f'telegram:{message_id}'),
                types.InlineKeyboardButton("💜Instagram", callback_data=f'instagram:{message_id}')
            ],
            [
                types.InlineKeyboardButton("🖤TikTok", callback_data=f'tiktok:{message_id}')
            ]
        ])
        
    return button


def animal(message_id):
    button = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("🐕Собака", callback_data=f'dog:{message_id}'),
            types.InlineKeyboardButton("🐱Кошка", callback_data=f'cat:{message_id}'),
            types.InlineKeyboardButton("🐒Обезьякна", callback_data=f'monkey:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🦜Попугай", callback_data=f'parrot:{message_id}'),
            types.InlineKeyboardButton("🐮Коровка", callback_data=f'cow:{message_id}'),
            types.InlineKeyboardButton("🐸Жабка", callback_data=f'frog:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🦊Лиса", callback_data=f'fox:{message_id}'),
            types.InlineKeyboardButton("🐁Крыска", callback_data=f'rat:{message_id}')
        ]
    ])
    
    return button
    

def place_for_camp(message_id):
    button =  types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("🏝Пляж", callback_data=f'beach:{message_id}'),
            types.InlineKeyboardButton("🎢Парк аттракционов", callback_data=f'attraction:{message_id}'),
            types.InlineKeyboardButton("🛍Торговый центр", callback_data=f'store:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🏔Горы", callback_data=f'mountain:{message_id}'),
            types.InlineKeyboardButton("🛳Круиз", callback_data=f'cruise:{message_id}'),
            types.InlineKeyboardButton("🐟Аквапарк", callback_data=f'aqupark:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🍿Кинотеатр", callback_data=f'cinema:{message_id}'),
            types.InlineKeyboardButton("🎭Театр", callback_data=f'theater:{message_id}')
        ]
    ])
    
    return button


def season(message_id):
    button =  types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("❄️Зима", callback_data=f'winter:{message_id}'),
            types.InlineKeyboardButton("🌷Весна", callback_data=f'spring:{message_id}'),
            types.InlineKeyboardButton("🌈Лето", callback_data=f'summer:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🍂Осень", callback_data=f'fall:{message_id}')
        ]
    ])
    
    return button


def weather(message_id):
    button =  types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("☀️Солнце", callback_data=f'sun:{message_id}'),
            types.InlineKeyboardButton("🌚Луна", callback_data=f'moon:{message_id}'),
            types.InlineKeyboardButton("☁️Облако", callback_data=f'cloud:{message_id}')
        ],
        [
            types.InlineKeyboardButton("☔️Дождь", callback_data=f'rain:{message_id}')
        ]
    ])
    
    return button


def cake(message_id):
    button =  types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("🍰Торт", callback_data=f'cake:{message_id}'),
            types.InlineKeyboardButton("🍫Шоколад", callback_data=f'chocolat:{message_id}'),
            types.InlineKeyboardButton("🍪Печенье", callback_data=f'cookie:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🍩Пончик", callback_data=f'donut:{message_id}'),
            types.InlineKeyboardButton("🍦Мороженое", callback_data=f'icecream:{message_id}')
        ]
    ])
    
    return button



def month(message_id):
    button =  types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("☃️Декабрь", callback_data=f'december:{message_id}'),
            types.InlineKeyboardButton("🌨Январь", callback_data=f'january:{message_id}'),
            types.InlineKeyboardButton("❄️Феврал", callback_data=f'february:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🌷Март", callback_data=f'march:{message_id}'),
            types.InlineKeyboardButton("🌹Апрель", callback_data=f'april:{message_id}'),
            types.InlineKeyboardButton("🌺Май", callback_data=f'may:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🌿Июнь", callback_data=f'juny:{message_id}'),
            types.InlineKeyboardButton("🪻Июль", callback_data=f'july:{message_id}'),
            types.InlineKeyboardButton("🪷Август", callback_data=f'august:{message_id}')
        ],
        [
            types.InlineKeyboardButton("🍁Сентябрь", callback_data=f'september:{message_id}'),
            types.InlineKeyboardButton("🍂Октябрь", callback_data=f'october:{message_id}'),
            types.InlineKeyboardButton("🪸Ноябрь", callback_data=f'november:{message_id}')
        ]
    ])
    
    return button


def menu(message_id):
    button =  types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("📊Посмотреть мои результаты", callback_data=f'see_result:{message_id}')
        ],
        [
            types.InlineKeyboardButton("✍️Перепройти тест", callback_data=f'test_again:{message_id}')
        ]
    ])
    
    return button


def back(message_id):
    button =  types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("⬅️Назад", callback_data=f'back:{message_id}')
        ]
    ])
    
    return button