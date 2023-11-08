import os
from dotenv import load_dotenv

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from api_handlers.user_api import UserAPI

load_dotenv()

router = Router()


@router.message(CommandStart())
async def create_user(message: Message):
    user = UserAPI(os.getenv("BASE_URL"), message).add_new_user()
    await message.answer(user)


@router.message(Command("help"))
async def help_user(message: Message):
    await message.answer("""Available commands:\n
    /start - create new user\n
    /create_house - create new house\n
    /add_member - add new member to the house\n
    /get_house_info - get house info\n
    /add_expense - add new expense\n
    /add_settlement - add new settlement\n
    /get_debt_info - get info about your debts\n
    /return_debt - return your debt\n
    """)
