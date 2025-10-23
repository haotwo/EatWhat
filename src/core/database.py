from typing import AsyncGenerator
import asyncio

from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy import text, event
from sqlalchemy.orm import Session

from src.core.config import settings
from src.core.base_model import Base,DateTimeMixin
from src.dishes.model import Dish

# 创建数据库引擎和会话工厂
engine = create_async_engine(settings.database_url,**settings.engine_options)

SessionFactory = async_sessionmaker(
    class_=AsyncSession,autoflush=False,expire_on_commit=False,bind=engine
)

# 数据库依赖注入
async def get_db() ->AsyncGenerator[AsyncSession,None]:
    async with SessionFactory() as session: 
        yield session