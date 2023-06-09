from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN_API: str = '5456421384:AAGeZHqGzcJ9cin-vnUoH35kiuNkQ1xGkjI'

storage = MemoryStorage()
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)