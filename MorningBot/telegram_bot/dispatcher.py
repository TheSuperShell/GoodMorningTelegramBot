import logging

import aiogram.types
from aiogram import Dispatcher
from aiogram.bot import Bot

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=aiogram.types.ParseMode.HTML)
dp = Dispatcher(bot=bot)
