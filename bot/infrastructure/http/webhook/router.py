from fastapi import APIRouter, Depends, Request, Response
from aiogram.types import Update

from bot.core.bot import bot, dp
from .depend import validate_secret_token



webhook_router = APIRouter(
     prefix="/webhook",
     dependencies=[Depends(validate_secret_token)]
)



@webhook_router.post("/telegram", response_class=Response)
async def telegram(request: Request):
     update = Update.model_validate(await request.json(), context={"bot": bot})
     await dp.feed_update(bot=bot, update=update)
     return Response()