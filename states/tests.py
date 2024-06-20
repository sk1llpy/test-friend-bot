from aiogram.dispatcher.filters.state import State, StatesGroup


class TestFriends(StatesGroup):
    so_media = State()
    animal = State()
    place_for_camp = State()
    season = State()
    weather = State()
    cake = State()
    month = State()