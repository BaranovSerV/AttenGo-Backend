import asyncio
from aiogram import Bot, Dispatcher

from src.settings import settings

print(settings.BOT_API_TOKEN)

bot = Bot(token=settings.BOT_API_TOKEN)
dp = Dispatcher()


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()



if __name__ == "__main__":
    asyncio.run(main())
