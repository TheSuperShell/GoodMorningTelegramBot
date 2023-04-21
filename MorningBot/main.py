from telegram_bot.dispatcher import dp
from aiogram import executor, types
from telegram_bot.scheduler import on_startup

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup)