import os
from dotenv import load_dotenv

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from api_handlers.settlement_api import SettlementAPI
from utils.states import AddSettlementForm
from utils.states import RepaidTheDebtForm

load_dotenv()
base_url = os.getenv("BASE_URL")

router = Router()


@router.message(Command("add_settlement"))
async def add_settlement(message: Message, state: FSMContext):
    await state.set_state(AddSettlementForm.username)
    await message.answer("Enter the username of the debtor:")


@router.message(AddSettlementForm.username)
async def add_settlement_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(AddSettlementForm.amount)
    await message.answer("Enter the amount of money:")


@router.message(AddSettlementForm.amount)
async def add_settlement_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await state.set_state(AddSettlementForm.end)
    await message.answer("Add one more debtor or not? (yes/no)")


@router.message(AddSettlementForm.end)
async def add_settlement_end(message: Message, state: FSMContext):
    if message.text.lower() == "yes":
        data = {
            "payer": message.from_user.id,
            "username": (await state.get_data())['username'],
            "amount": (await state.get_data())['amount'],
        }

        settlement = SettlementAPI(base_url, data).add_new_settlement()
        await message.answer(settlement)

        await state.set_state(AddSettlementForm.username)
        await message.answer("Enter the username of the debtor:")
    elif message.text.lower() == "no":
        await state.set_state(AddSettlementForm.finish)

        data = {
            "payer": message.from_user.id,
            "username": (await state.get_data())['username'],
            "amount": (await state.get_data())['amount'],
        }

        settlement = SettlementAPI(base_url, data).add_new_settlement()
        await message.answer(settlement)
    else:
        await message.answer("Wrong answer!")


@router.message(Command("return_debt"))
async def return_debt(message: Message, state: FSMContext):
    await state.set_state(RepaidTheDebtForm.username)
    await message.answer("Enter the username of the debtor:")


@router.message(RepaidTheDebtForm.username)
async def return_debt_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(RepaidTheDebtForm.amount)
    await message.answer("Enter the amount of money:")


@router.message(RepaidTheDebtForm.amount)
async def return_debt_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await state.set_state(RepaidTheDebtForm.finish)

    data = {
        "payer": message.from_user.id,
        "username": (await state.get_data())['username'],
        "amount": str(int((await state.get_data())['amount']) * -1),
    }

    settlement = SettlementAPI(base_url, data).add_new_settlement()
    await message.answer(settlement)


@router.message(Command("get_debts"))
async def get_user_debts(message: Message):
    data = {
        "telegram_id": message.from_user.id,
    }

    debts = SettlementAPI(base_url, data).get_debts()
    await message.answer(debts)