from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Рассчитать'))
keyboard.add(KeyboardButton('Информация'))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот, помогающий твоему здоровью. Чем могу помочь?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def set_age(message: types.Message):
    await message.reply("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await message.reply("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['growth'] = int(message.text)
    await message.reply("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = int(message.text)
        age = data['age']
        growth = data['growth']
        weight = data['weight']

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.reply(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()

@dp.message_handler(lambda message: message.text == 'Информация')
async def send_info(message: types.Message):
    await message.reply("Я бот, помогающий рассчитать вашу дневную норму калорий. Используйте кнопку 'Рассчитать' для начала.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)