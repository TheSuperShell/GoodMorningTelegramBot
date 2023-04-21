from datetime import date

from config import CHANNEL_LINK, WEATHER_API
from telegram_bot.dispatcher import dp
from weather_data.weather_requests import get_weather

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

months = (
	'явнваря',
	'февраля',
	'марта',
	'апреля',
	'мая',
	'июня',
	'июля',
	'августа',
	'сентября',
	'октября',
	'ноября',
	'декабря'
)


async def send_morning_report():
	await label()
	await send_weather_report()


async def label():
	try:
		curr_date = date.today()
		month = months[curr_date.month - 1]
		await dp.bot.send_message(CHANNEL_LINK,
								  f'** {curr_date.day} {month} {curr_date.year} **\n\n<b>Доброе утро!</b>')
	except Exception as e:
		print(e)


async def send_weather_report():
	try:
		markup = InlineKeyboardMarkup()
		markup.add(InlineKeyboardButton("Яндекс погода", url='yandex.ru/pogoda/moscow'))
		await dp.bot.send_message(CHANNEL_LINK, get_weather('Moscow', WEATHER_API), reply_markup=markup)
	except Exception as e:
		print(e)
