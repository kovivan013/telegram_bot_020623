from telegram_bot_020623.telegram_bot.config import Bot, Dispatcher
from telegram_bot_020623.telegram_bot.keyboards.keyboards import *
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text


async def start(message: Message) -> None:

    await message.answer(text=f'*{message.from_user.username}*, главное меню:',
                         reply_markup=Stop_1.keyboard(),
                         parse_mode="Markdown"
                         )

def register_main_handlers(dp: Dispatcher) -> None:
    pass