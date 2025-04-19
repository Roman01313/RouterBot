from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Filter, Text, Command
from keyborads.for_questions import get_yes_no_kb

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer("Are yoy happy with your work?", reply_markup=get_yes_no_kb)

@router.message(Text(Text='yes', text_ignore_case=True))
async def answer_yes(message: Message):
    await message.answer('that quite good', reply_markup=ReplyKeyboardRemove())

@router.message(Text(Text='no', text_ignore_case=True))
async def answer_yes(message: Message):
    await message.answer('that neither bad', reply_markup=ReplyKeyboardRemove())

