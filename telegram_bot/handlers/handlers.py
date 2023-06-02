from telegram_bot_020623.telegram_bot.config import Bot, Dispatcher

from aiogram.types import Message


async def start(message: Message) -> None:
    await message.answer(text=f'Hello, {message.from_user.id}')


def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        start, commands=['start']
    )