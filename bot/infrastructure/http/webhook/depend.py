from fastapi import Request, HTTPException

from bot.core.settings import Settings



async def validate_secret_token(request: Request) -> None:
     token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
     if token != Settings.secret_webhook_token:
          raise HTTPException(
               status_code=400,
               detail="Invalid secret webhook token!"
          )