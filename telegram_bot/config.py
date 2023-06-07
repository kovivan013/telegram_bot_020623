from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN_API'))
dp = Dispatcher(bot)