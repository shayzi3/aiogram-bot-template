from aiogram import Bot, Dispatcher

from .settings import Settings


bot = Bot(token=Settings.bot_token)
dp = Dispatcher()