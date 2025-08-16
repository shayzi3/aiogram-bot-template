from bot.core.bot import bot
from bot.core.settings import Settings



class MessageAlert:
     
     @classmethod
     async def send_alert(cls, message: str) -> None:
          async with bot as session:
               await session.send_message(
                    chat_id=Settings.alert_chat,
                    text=message
               )