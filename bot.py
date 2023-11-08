import asyncio
import sys
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import handlers

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

scheduler = AsyncIOScheduler()


async def main() -> None:
    bot = Bot(bot_token)
    dp = Dispatcher()

    dp.include_routers(
        handlers.router_expense.router,
        handlers.router_user.router,
        handlers.router_house.router,
        handlers.router_settlement.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, reset_webhook=True)


async def keep_bot_active():
    await asyncio.sleep(0.1)


scheduler.add_job(keep_bot_active, 'interval', seconds=15)
scheduler.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
