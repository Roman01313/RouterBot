from aiogram import Router
from aiogram import F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Filter, Command
from for_questions import get_yes_no_kb

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer("Are yoy happy with your work?", reply_markup=get_yes_no_kb())

@router.message(F.text == 'yes')
async def answer_yes(message: Message):
    await message.answer('that quite good', reply_markup=ReplyKeyboardRemove())

@router.message(F.text == 'no')
async def answer_yes(message: Message):
    await message.answer('that rather good', reply_markup=ReplyKeyboardRemove())