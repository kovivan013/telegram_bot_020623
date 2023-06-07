from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN_API'))
dp = Dispatcher(bot)


def default() -> None:
    global like_status
    like_status = None

def lk() -> None:
    global like_status
    if like_status or None:
        like_status = False
    elif not like_status or None:
        like_status = True

