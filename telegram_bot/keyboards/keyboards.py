from dataclasses import dataclass
from typing import Union


from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton
)

def default_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup (
        resize_keyboard=True,
        one_time_keyboard=True,
        row_width=2
    )

@dataclass(frozen=True)
class BaseMenu:

    cancel_key: str = "Cancel"

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:

        return default_keyboard().add(KeyboardButton(cls.cancel_key))


@dataclass(frozen=True)
class StartMenu(BaseMenu):

    test_text_1: str = 'test button 1'
    test_text_2: str = 'test button 2'
    test_text_3: str = 'test button 3'
    test_text_4: str = 'test button 4'

    @classmethod
    def keyboard(cls) -> 'ReplyKeyboardMarkup':

        return default_keyboard().add(
            KeyboardButton(cls.test_text_1),
            KeyboardButton(cls.test_text_2),
            KeyboardButton(cls.test_text_3),
            KeyboardButton(cls.test_text_4),
            KeyboardButton(cls.cancel_key)
        )