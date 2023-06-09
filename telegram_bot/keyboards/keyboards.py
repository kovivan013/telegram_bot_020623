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
        row_width=3
    )

@dataclass(frozen=True)
class StartMenu:
    # Стандартное меню пользователя

    info: str = '🧾 Информация'

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:

        return default_keyboard().add(
            KeyboardButton(text=cls.info)
        )

class InfoInlineMenu:
    # Меню получения информации о боте

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        return (
            default_inline_keyboard().add(
                InlineKeyboardButton(text='📑 Получить Информация',
                                     callback_data='get_info_callback')
            )
        )
