from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


router = Router()


@router.message(Command("add"))
async def add(message: Message):
    await message.answer("hi")