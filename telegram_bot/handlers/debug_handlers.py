from telegram_bot_020623.telegram_bot.config import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from telegram_bot_020623.telegram_bot.keyboards.keyboards import StartMenu
from aiogram.types import Message

async def debug_handler(message: Message, state: FSMContext) -> None:
    # Хендлер отвечает на незарегистрированные команды приложения

    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    await message.answer(text=f'*Перед вами главное меню:*',
                         reply_markup=StartMenu.keyboard(),
                         parse_mode='Markdown'
    )


def register_debug_handlers(dp: Dispatcher) -> None:
    # Регистрирует debug хендлеры приложения
    dp.register_message_handler(debug_handler,
                                state=['*']
    )
