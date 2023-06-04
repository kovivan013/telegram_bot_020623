from telegram_bot_020623.telegram_bot.config import Bot, Dispatcher
from telegram_bot_020623.telegram_bot.keyboards.keyboards import MainMenu, ToMainMenu
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text


""" COMMANDS """


async def start(message: Message) -> None:
    """ Возвращает главное меню """

    await message.answer(text=f'*{message.from_user.username}*, главное меню:',
                         reply_markup=MainMenu.keyboard(),
                         parse_mode="Markdown"
                         )

async def help(message: Message) -> None:
    await message.answer(text=f'*{message.from_user.username}*, к сожалению, здесь пока ничего нет!',
                   reply_markup=ToMainMenu.keyboard(),
                   parse_mode='Markdown')

async def description(message: Message) -> None:
    await message.answer(text=f'*{message.from_user.username}*, к сожалению, здесь пока ничего нет!',
                   reply_markup=ToMainMenu.keyboard(),
                   parse_mode='Markdown')

""" CALLBACKS """

async def to_main_menu_callback(callback: CallbackQuery) -> None:
    if callback.data == 'Back_To_Main_Menu':
        await callback.message.answer(text=f'главное меню:',
                         reply_markup=MainMenu.keyboard(),
                         parse_mode="Markdown"
        )
        await callback.message.delete()

def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        start, commands=['start']
    )
    dp.register_message_handler(
        help, Text(equals=MainMenu.help_btn)
    )
    dp.register_message_handler(
        description, Text(equals=MainMenu.desc_btn)
    )
    dp.register_callback_query_handler(
        to_main_menu_callback
    )