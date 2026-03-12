# main.py
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Бот запущен на Bothost. Пиши что угодно — эхо-ответ.")

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот стартовал (polling)")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
