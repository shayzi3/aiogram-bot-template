from typing import Callable, Awaitable, Any

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message, TelegramObject



class LogMiddleware(BaseMiddleware):
     
     async def __call__(
          self, 
          handler: Callable[[Message, dict[str, Any]], Awaitable], 
          event: TelegramObject, 
          data: dict[str, Any]
     ) -> None:
          ...