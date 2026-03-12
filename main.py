# main.py

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    # Создаём inline-клавиатуру с одной кнопкой-ссылкой
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="ПРОДАТЬ ПУШКИНСКУЮ КАРТУ",
                    url="https://t.me/sasha_links"   # или просто "t.me/sasha_teatr" — тоже работает
                )
            ]
        ]
    )

    # Отправляем сообщение с кнопкой
    await message.answer(
        "Здравствуйте! Приветствуем вас в сервисе по продаже пушкинских карт! 👋\n"
        "Нажми кнопку ниже, чтобы перейти в диалог к менеджеру:",
        reply_markup=keyboard
    )


# Опционально: эхо на все остальные сообщения (можно убрать или оставить)
@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    # Удаляем старый webhook (если был) — важно для Bothost
    await bot.delete_webhook(drop_pending_updates=True)
    
    logging.info("Бот запущен (polling)")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
