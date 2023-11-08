import asyncio
import sys
import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher

import handlers

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')


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


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
