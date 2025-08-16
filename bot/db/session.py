from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot.core.settings import Settings


engine = create_async_engine(url=Settings.sql_url)
session_maker = async_sessionmaker(engine)



async def get_async_session():
     async with session_maker() as async_session:
          try:
               yield async_session
          except Exception as ex:
               await async_session.rollback()
               raise ex
          finally:
               await async_session.close()