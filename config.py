import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

print("берем токен из .env")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()