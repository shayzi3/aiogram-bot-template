from typing import Callable, Awaitable, Any

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject

from bot.core.settings import Settings
from bot.logger import logger
from bot.alert import MessageAlert



class LogMiddleware(BaseMiddleware):
     
     async def __call__(
          self, 
          handler: Callable[[TelegramObject, dict[str, Any]], Awaitable], 
          event: TelegramObject, 
          data: dict[str, Any]
     ) -> None:
          router_name = getattr(data.get("event_router"), "name", "")
          
          callback = getattr(data.get("handler"), "callback", None)
          if callback is not None:
               callback_name = getattr(callback, "__name__", "")
          
          logger.bot.info(f"USER {event.from_user.id} ROUTER: {router_name} CALLBACK: {callback_name}")
          
          try:
               return await handler(event, data)
          except Exception as ex:
               logger.bot.error(msg=str(ex), exc_info=True)
               await MessageAlert.send_alert(
                    message=f"Error: {ex} \nRouter: {router_name} \nCallback: {callback_name}"
               )
               return await event.answer(Settings.server_error_message)
               