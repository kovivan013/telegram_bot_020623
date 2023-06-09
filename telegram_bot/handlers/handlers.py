import random
import string

from telegram_bot_020623.telegram_bot.config import Bot, Dispatcher, bot
from telegram_bot_020623.telegram_bot.keyboards.keyboards import *
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext


def register_main_handlers(dp: Dispatcher) -> None:
    pass