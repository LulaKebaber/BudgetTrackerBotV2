import os
from dotenv import load_dotenv

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import AddExpenseForm
from api_handlers.expense_api import ExpenseAPI

from datetime import datetime

load_dotenv()
base_url = os.getenv("BASE_URL")

router = Router()


@router.message(Command("add_expense"))
async def add_expense(message: Message, state: FSMContext):
    await state.set_state(AddExpenseForm.amount)
    await message.answer("Enter amount of expense:")


@router.message(AddExpenseForm.amount)
async def form_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await state.set_state(AddExpenseForm.description)
    await message.answer("Enter description of expense:")


@router.message(AddExpenseForm.description)
async def form_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(AddExpenseForm.finish)

    data = {
        "amount": (await state.get_data())['amount'],
        "description": (await state.get_data())['description'],
        "buyer": message.from_user.id,
        "date": datetime.now().strftime("%Y-%m-%d"),
    }

    expense = ExpenseAPI(base_url, data).add_expense()

    await message.answer(expense)
