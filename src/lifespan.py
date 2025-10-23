# app/lifespan.py
import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI
from loguru import logger

# 定义北京时区常量
BEIJING_TIMEZONE = timezone(timedelta(hours=8))


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:
    # -------- 启动 --------
    logger.info("应用启动，开始加载所有资源...")
    
    # await create_db_and_tables()

    # -------- 运行 --------
    yield

    # -------- 关闭 --------

    logger.info("应用关闭，资源已释放。")