from aiogram import Router, F
from aiogram.types import Message 

types_router = Router()

@types_router.message(F.text)
async def message_text(message: Message):
    await message.answer('Its a text message')

@types_router.message(F.sticker)
async def get_sticker_msg(message:Message):
    await message.answer('its a sticker')

@types_router.message(F.animation)
async def anim_msg(message: Message):
    await message.answer('its an animations')