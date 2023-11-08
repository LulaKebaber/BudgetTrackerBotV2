import os
from dotenv import load_dotenv

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from api_handlers.user_api import UserAPI

load_dotenv()

router = Router()


@router.message(CommandStart())
async def create_user(message: Message):
    user = UserAPI(os.getenv("BASE_URL"), message).add_new_user()
    await message.answer(user)