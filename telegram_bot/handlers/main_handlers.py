import random
import string

from telegram_bot_020623.telegram_bot.config import Bot, Dispatcher, bot
from telegram_bot_020623.telegram_bot.keyboards.keyboards import StartMenu, InfoInlineMenu
from telegram_bot_020623.telegram_bot.states.states import MainStates
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext


async def main_menu(message: Message) -> None:
    await message.answer(text=f'Главное меню:',
                         reply_markup=StartMenu.keyboard())

async def info(message: Message, state: FSMContext) -> None:
    await MainStates.info.set()
    await message.answer(text=f'*Выберите тип:*',
                         reply_markup=InfoInlineMenu.keyboard(),
                         parse_mode='Markdown')

async def get_info(callback: CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['telegram_id'] = callback.from_user.id
        data['username'] = callback.from_user.username if callback.from_user.username is not None else ""

    await callback.message.answer(text=f"Your *telegram ID* is {data['telegram_id']}\n" \
                                  f"Your *telegram username* is {data['username']}",
                                  parse_mode='Markdown')
    await state.finish()


def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        main_menu, commands=['start'], state=None
    )
    dp.register_message_handler(
        info, Text(equals=StartMenu.info)
    )
    dp.register_callback_query_handler(
        get_info, state=MainStates.info
    )