04.24 22:11
import os
import json
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
#  START
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(" Bot ishga tushdi")
#  MINI APP DATA QABUL QILISH
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def webapp(msg: types.Message):
    try:
        data = json.loads(msg.web_app_data.data)
        t = data.get("type")
        d = data.get("data")
        await msg.answer("⏳ Qabul qilindi")
        if t == "url":
            await msg.answer(f" URL:\n{d}")
        elif t == "telegram":
            await msg.answer(" Telegram video qabul qilindi")
        else:
            await msg.answer("❓ Noma’lum format")
    except Exception as e:
        await msg.answer(f"❌ Xatolik: {e}")
#️ RUN
dp.run_polling(bot)

