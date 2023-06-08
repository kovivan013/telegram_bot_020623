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
class BaseMenu:

    cancel_key: str = "Cancel"

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()

        keyboard.add(
            KeyboardButton(cls.cancel_key)
        )
        return keyboard

@dataclass(frozen=True)
class Main_Menu:
    """ Главное меню бота """

    help_btn: str = '🆘 Помощь'
    desc_btn: str = '📋 Описание Бота'
    rand_btn: str = '📷 Рандомное Фото'
    lang_btn: str = '📱 Выбрать Язык'

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()
        keyboard.add(
            KeyboardButton(text=cls.help_btn
            ),
            KeyboardButton(text=cls.desc_btn
            ),
            KeyboardButton(text=cls.rand_btn
            ),
            KeyboardButton(text=cls.lang_btn
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

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f'🠉',
                                  callback_data='Collapse_Menu'
            )],

            [InlineKeyboardButton(text=f'Лайк 👍',
                                  callback_data='like'
                                  ),
             InlineKeyboardButton(text=f'Следующая фотография',
                                  callback_data='Next_Photo'
                                  ),
             InlineKeyboardButton(text=f'Дизлайк 👎',
                                  callback_data='dislike'
                                  ),
            ],

            [InlineKeyboardButton(
                text='На главное меню',
                callback_data='Back_To_Main_Menu'
            )]
        ])

        return keyboard

@dataclass(frozen=True)
class Collapse_InlineMenu:

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(text=f'🠋',
                                 callback_data='Expand_Menu'
                                 )
        )

        return keyboard



@dataclass(frozen=True)
class Language_Menu:

    @classmethod
    def keyboard(cls, language) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()

        english_list = ['en', 'en', 'en', 'en', 'en', 'en']
        lietuviskai_list = ['lat', 'lat', 'lat', 'lat', 'lat', 'lat']
        russian_list = ['ru', 'ru', 'ru', 'ru', 'ru', 'ru']
        polish_list = ['pl', 'pl', 'pl', 'pl', 'pl', 'pl']

        if language == 'English':
            lst = english_list
        elif language == 'Lietuviskai':
            lst = lietuviskai_list
        elif language == 'Russian':
            lst = russian_list
        elif language == 'Polish':
            lst = polish_list

        x = 0
        for i in lst:
            if x >= 6:
                break
            keyboard.add(KeyboardButton(text=str(lst[x])),
                         KeyboardButton(text=str(lst[x + 1]))
                         )
            x += 2

        return keyboard


class LanguageVariant_Menu:

    en_btn: str = 'English'
    li_btn: str = 'Lietuviskai'
    ru_btn: str = 'Russian'
    pl_btn: str = 'Polish'

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()

        keyboard.add(
            KeyboardButton(text=cls.en_btn),
            KeyboardButton(text=cls.li_btn),
            KeyboardButton(text=cls.ru_btn),
            KeyboardButton(text=cls.pl_btn),

        )

        return keyboard