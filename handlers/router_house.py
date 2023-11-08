import os
from dotenv import load_dotenv

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import CreateHouseForm
from utils.states import AddHouseMemberForm
from utils.states import GetHouseInfoForm
from api_handlers.house_api import HouseAPI

load_dotenv()
base_url = os.getenv("BASE_URL")

router = Router()


@router.message(Command("create_house"))
async def create_house(message: Message, state: FSMContext):
    await state.set_state(CreateHouseForm.house_name)
    await message.answer("Enter house name:")


@router.message(CreateHouseForm.house_name)
async def form_house_name(message: Message, state: FSMContext):
    await state.update_data(house_name=message.text)
    await state.set_state(CreateHouseForm.finish)

    data = {
        "house_name": (await state.get_data())['house_name'],
        "owner": message.from_user.id,
    }

    house = HouseAPI(base_url, data).create_new_house()
    await message.answer(house)


@router.message(Command("add_member"))
async def add_member(message: Message, state: FSMContext):
    await state.set_state(AddHouseMemberForm.house_name)
    await message.answer("Enter house name:")


@router.message(AddHouseMemberForm.house_name)
async def form_house_name(message: Message, state: FSMContext):
    await state.update_data(house_name=message.text)
    await state.set_state(AddHouseMemberForm.member_name)
    await message.answer("Enter member name:")


@router.message(AddHouseMemberForm.member_name)
async def form_member_name(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(AddHouseMemberForm.finish)

    data = {
        "house_name": (await state.get_data())['house_name'],
        "username": (await state.get_data())['username'],
        "owner": message.from_user.id,
    }
    member = HouseAPI(base_url, data).add_member()
    await message.answer(member)


@router.message(Command("get_house_members"))
async def get_house_members(message: Message, state: FSMContext):
    await state.set_state(GetHouseInfoForm.house_name)
    await message.answer("Enter house name:")


@router.message(GetHouseInfoForm.house_name)
async def form_house_name(message: Message, state: FSMContext):
    await state.update_data(house_name=message.text)
    await state.set_state(GetHouseInfoForm.finish)

    data = {
        "house_name": (await state.get_data())['house_name'],
    }

    members = HouseAPI(base_url, data).get_house_members()
    await message.answer(members)