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
    await callback.message.answer(text=f'*{callback.from_user.username}*, [информация получена успешно](https://www.roblox.com/home)!',
                                  parse_mode='Markdown')
    await bot.send_photo(photo='https://images.unsplash.com/photo-1566275529824-cca6d008f3da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cGhvdG98ZW58MHx8MHx8fDA%3D&w=1000&q=80',
                         caption=f'[test](https://www.roblox.com/home)',
                         chat_id=callback.message.chat.id,
                         reply_markup=ReplyKeyboardRemove(),
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