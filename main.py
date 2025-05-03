import asyncio
from aiogram import Bot, Dispatcher
from questions import router
from different_types import types_router

async def main():
    bot = Bot(token="7876853275:AAEOJzd2weQmTW_dld1txsaEui-V8LrWV-Y")
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(types_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())