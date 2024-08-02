from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Your bot's API token
API_TOKEN = ''

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Command handler for the /start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот, помогающий твоему здоровью. Чем могу помочь?")

# Handler for all other messages
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.reply("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    # Start the bot
    executor.start_polling(dp, skip_updates=True)