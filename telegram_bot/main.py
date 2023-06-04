from aiogram import executor
from config import bot, dp
from handlers.handlers import register_main_handlers

register_main_handlers(dp)

async def on_startup(_) -> None:
    print('Bot Started!')

async def on_shutdown(_) -> None:
    print('Bot Shutdown!')

def start_bot() -> None:

    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )


if __name__ == '__main__':
    start_bot()