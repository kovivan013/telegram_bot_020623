from telegram_bot_020623.telegram_bot.config import Bot, Dispatcher
from telegram_bot_020623.telegram_bot.keyboards.keyboards import Stop_1, Stop_2, Stop_3
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text


async def start(message: Message) -> None:

    await message.answer(text=f'*{message.from_user.username}*, главное меню:',
                         reply_markup=Stop_1.keyboard(),
                         parse_mode="Markdown"
                         )

async def change_markup(callback: CallbackQuery) -> None:
    pass

def register_main_handlers(dp: Dispatcher) -> None:
    pass