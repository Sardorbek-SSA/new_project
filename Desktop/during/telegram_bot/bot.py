import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")

# links
cities = {
    "Seul": "https://t.me/+abcd1234",
    "Busan": "https://t.me/+efgh5678",
    "Incheon": "https://t.me/+ijkl91011"
}

dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=city, callback_data=city)] for city in cities
        ]
    )
    await message.answer(
        "Assalomu alaykum!\nShaharingizni tanlang 👇",
        reply_markup=keyboard
    )

@dp.callback_query(lambda c: c.data in cities)
async def city_selected(callback: types.CallbackQuery):
    city = callback.data
    link = cities[city]
    await callback.message.answer(
        f"📍 Siz *{city}* ni tanladingiz.\nGuruh havolasi: {link}",
        parse_mode="Markdown"
    )
    await callback.answer()

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())