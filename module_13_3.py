from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот, помогающий твоему здоровью. Чем могу помочь?")

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.reply("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    # Start the bot
    executor.start_polling(dp, skip_updates=True)
