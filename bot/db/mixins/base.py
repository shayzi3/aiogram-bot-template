from typing import TypeVar, Generic, Any

from bot.db.models import Base


T = TypeVar("T", bound=Base)



class BaseMixin(Generic[T]):
     
     @classmethod
     async def read(cls) -> T:
          ...
          
     @classmethod
     async def read_many(cls) -> list[T]:
          ...
          
     @classmethod
     async def update(cls) -> Any:
          ...
          
     @classmethod
     async def update_many(cls) -> Any:
          ...
          
     @classmethod
     async def create(cls) -> Any:
          ...
          
     @classmethod
     async def create_many(cls) -> Any:
          ...
          
     @classmethod
     async def delete(cls) -> Any:
          ...