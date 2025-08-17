import logging

from datetime import datetime

from bot.core.settings import Settings



class BaseLogger(logging.Logger):
     def __init__(self, name: str, filename: str):
          super().__init__(name, logging.INFO)
          
          handler = logging.FileHandler(filename=filename)
          formatter = logging.Formatter(fmt=Settings.logging_format)
          handler.setFormatter(formatter)
          self.addHandler(handler)
          
          
          
class FactoryBaseLogger:
     
     def __current_day(self) -> str:
          return datetime.now().strftime("%Y-%m-%d")
     
     @property
     def bot(self) -> BaseLogger:
          return BaseLogger(
               name="BOT",
               filename=f"data/logs/bot/{self.__current_day()}.txt"
          )
          
          
logger = FactoryBaseLogger()