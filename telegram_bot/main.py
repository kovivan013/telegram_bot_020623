from aiogram import executor

from config import bot, dp

def on_startup(_) -> None:
    print('Bot Started!')

def on_shutdown(_) -> None:
    print('Bot Stutdown!')

def start_bot() -> None:
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup(),
        on_shutdown=on_shutdown()
    )

if __name__ == '__main__':
    start_bot()