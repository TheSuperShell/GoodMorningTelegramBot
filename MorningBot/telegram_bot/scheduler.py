import aioschedule
import asyncio
from telegram_bot.scheduled_commands import send_morning_report


async def scheduler(time, func):
	aioschedule.every().day.at(time).do(func)
	while True:
		await aioschedule.run_pending()
		await asyncio.sleep(1)


async def on_startup(_):
	asyncio.create_task(scheduler('11:40', send_morning_report))
