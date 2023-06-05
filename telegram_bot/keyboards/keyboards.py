from dataclasses import dataclass
from typing import Union


from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

def default_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup (
        resize_keyboard=True,
        one_time_keyboard=True,
        row_width=2
    )

def default_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup (
        row_width=2
    )

@dataclass(frozen=True)
class BaseMenu:

    cancel_key: str = "Cancel"

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:

        return default_keyboard().add(
            KeyboardButton(cls.cancel_key)
        )

@dataclass(frozen=True)
class Main_Menu:
    """ Главное меню бота """

    help_btn: str = '🆘 Помощь'
    desc_btn: str = '📋 Описание Бота'
    rand_btn: str = '📷 Рандомное Фото'

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()
        keyboard.add(
            KeyboardButton(
                text=cls.help_btn
            ),
            KeyboardButton(
                text=cls.desc_btn
            ),
            KeyboardButton(
                text=cls.rand_btn
            )
        )

        return keyboard

@dataclass(frozen=True)
class ToMain_Menu:
    """ Возврат на главное меню """

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(
                text='На главное меню',
                callback_data='Back_To_Main_Menu'
            )
        )

        return keyboard

@dataclass(frozen=True)
class GeneratePhoto_Menu:
    """Меню генерации рандомного фото"""

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(
                text='На главное меню',
                callback_data='Back_To_Main_Menu'
            ),
            InlineKeyboardButton(
                text='Следующее',
                callback_data='Next_Photo'
            )
        )

        return keyboard