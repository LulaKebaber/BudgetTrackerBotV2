from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from api_handlers.user_api import UserAPI


router = Router()


@router.message(CommandStart())
async def create_user(message: Message):
    user = UserAPI.add_new_user(message)
    await message.answer(user)