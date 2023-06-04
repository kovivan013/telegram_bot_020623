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
class Stop_1:

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(
                text='Вперед ->',
                callback_data='to_stop_2'
            )
        )
        return keyboard

@dataclass(frozen=True)
class Stop_2:

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(
                text='<- Назад',
                callback_data='to_stop_1'
            ),
            InlineKeyboardButton(
                text='Вперед ->',
                callback_data='to_stop_3'
            )

        )
        return keyboard

@dataclass(frozen=True)
class Stop_3:

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(
                text='<- Назад',
                callback_data='to_stop_2'
            )
        )
        return keyboard