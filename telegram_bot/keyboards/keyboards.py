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
class Menu(BaseMenu):

    button_1: str = 'test_1'

    @classmethod
    def keyboard(cls) -> 'ReplyKeyboardMarkup':
        return default_keyboard().add(
            KeyboardButton(cls.button_1)
        )


@dataclass(frozen=True)
class Keyboard(BaseMenu):

    button_1: str = 'test_2'

    @classmethod
    def keyboard(cls) -> 'ReplyKeyboardMarkup':
        return default_keyboard().add(
            KeyboardButton(cls.button_1)
        )