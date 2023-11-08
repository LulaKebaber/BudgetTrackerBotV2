from aiogram.fsm.state import StatesGroup, State


class CreateHouseForm(StatesGroup):
    house_name = State()
    finish = State()


class AddHouseMemberForm(StatesGroup):
    house_name = State()
    member_name = State()
    finish = State()


class AddExpenseForm(StatesGroup):
    amount = State()
    description = State()
    finish = State()


class GetHouseInfoForm(StatesGroup):
    house_name = State()
    finish = State()


class AddSettlementForm(StatesGroup):
    username = State()
    amount = State()
    end = State()
    finish = State()


class RepaidTheDebtForm(StatesGroup):
    username = State()
    amount = State()
    finish = State()