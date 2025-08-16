import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from bot.core.bot import bot, dp
from bot.core.settings import Settings
from bot.handlers import __all_routers__
from bot.middleware import __all_middlewares__
from bot.infrastructure.http.webhook import webhook_router


@asynccontextmanager
async def lifespan(_: FastAPI):
     await dp.include_routers(__all_routers__)
     
     for types in dp.resolve_used_update_types():
          event = dp.observers.get(types)
          for middleware in __all_middlewares__:
               await event.middleware(middleware())
               
     await bot.set_webhook(
          url=Settings.webhook_url(),
          allowed_updates=dp.resolve_used_update_types(),
          drop_pending_updates=True,
          secret_token=Settings.secret_webhook_token
     )
               
     yield
     
     await bot.delete_webhook(drop_pending_updates=True)
        
               

app = FastAPI(lifespan=lifespan)
app.include_router(webhook_router)


if __name__ == "__main__":
     uvicorn.run(
          app="main:app",
          port=8083,
          host="0.0.0.0"
     )