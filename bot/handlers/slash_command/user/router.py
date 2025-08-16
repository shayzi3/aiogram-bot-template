from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart



user_slash_command_router = Router("user_slash_command_router")


@user_slash_command_router.message(CommandStart())
async def start(message: Message):
     await message.answer("Bot working success...")