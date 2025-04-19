from aiogram import BaseMiddleware
from datetime import datetime
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender

def is_weekend():
    return datetime.utcnow().weekday() in (5, 6)

class WeekendMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if not is_weekend():
            return await handler(event, data)
        
class WeekendCallbackMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if not is_weekend():
            return await handler(event, data)
        await event.answer('бот не работает по выходным!', show_alert=True)
        return