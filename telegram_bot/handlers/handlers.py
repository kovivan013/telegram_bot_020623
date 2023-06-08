import random
import string

from telegram_bot_020623.telegram_bot.config import Bot, Dispatcher
from telegram_bot_020623.telegram_bot.keyboards.keyboards import Main_Menu, ToMain_Menu, GeneratePhoto_Menu, Collapse_InlineMenu
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text


""" COMMANDS """


async def start(message: Message) -> None:
    # Возвращает главное меню
    await message.answer(text=f'*{message.from_user.username}*, главное меню:',
                         reply_markup=Main_Menu.keyboard(),
                         parse_mode="Markdown"
                         )


async def help(message: Message) -> None:
    # Возвращает меню help
    await message.answer(text=f'*{message.from_user.username}*, к сожалению, здесь пока ничего нет!',
                   reply_markup=ToMain_Menu.keyboard(),
                   parse_mode='Markdown')

async def description(message: Message) -> None:
    # Возвращает меню описания bot
    await message.answer(text=f'*{message.from_user.username}*, к сожалению, здесь пока ничего нет!',
                   reply_markup=ToMain_Menu.keyboard(),
                   parse_mode='Markdown')

async def random_photo(message: Message) -> None:
    await message.answer(text=f'*{message.from_user.username}*, рандомный символ: {random.choice(string.ascii_lowercase)}',
                         reply_markup=GeneratePhoto_Menu.keyboard(),
                         parse_mode='Markdown')



async def callback_handlers(callback: CallbackQuery) -> None:
    print(callback)
    # Ловит callback возврата на главное меню
    if callback.data == 'Back_To_Main_Menu':
        await callback.message.answer(text=f'главное меню:',
                                      reply_markup=Main_Menu.keyboard(),
                                      parse_mode="Markdown"
                                      )
        await callback.message.delete()

    # Ловит callbacks от like и dislike
    if callback.data == 'like':
        await callback.answer(text=f'Вы поставили лайк на фотографию!')


    elif callback.data == 'dislike':
        await callback.answer(text=f'Вы поставили дизлайк на фотографию!')

    # Ловит callback генерации нового фото (символа)
    if callback.data == 'Next_Photo':
        await callback.message.answer(text=f'*{callback.from_user.username}*, рандомный символ: {random.choice(string.ascii_lowercase)}',
                         reply_markup=GeneratePhoto_Menu.keyboard(),
                         parse_mode='Markdown')
        await callback.message.delete()

    # Ловит callback на сворачивание меню
    if callback.data == 'Expand_Menu':
        await callback.message.edit_reply_markup(
            reply_markup=GeneratePhoto_Menu.keyboard()
        )

    # Ловит callback на разворот меню
    if callback.data == 'Collapse_Menu':
        await callback.message.edit_reply_markup(
            reply_markup=Collapse_InlineMenu.keyboard()
        )



def register_main_handlers(dp: Dispatcher) -> None:

    dp.register_message_handler(
        start, commands=['start']
    )
    dp.register_message_handler(
        help, Text(equals=Main_Menu.help_btn)
    )
    dp.register_message_handler(
        description, Text(equals=Main_Menu.desc_btn)
    )
    dp.register_message_handler(
        random_photo, Text(equals=Main_Menu.rand_btn)
    )
    dp.register_callback_query_handler(
        callback_handlers
    )