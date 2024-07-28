from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
import contextlib

engine = create_async_engine(
    'postgresql+asyncpg://sesiadmin:sesi1234@localhost:5432/sesidb')

Base = declarative_base()


# TODO: 비동기 제대로 사용하려면 alembic 사용 필요
# 세션 생성기
SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


# 종속성 주입을 위한 세션 생성 함수
# @contextlib.asynccontextmanager
# NOTE: 동기방식에서는 endpoint에서 Depends로 get_db() 함수 이용시 데코레이터 사용 X 사용시 중복되어 오류
# 하지만 비동기 방식에는 빼야하는지 넣어야하는지 몰라서 일단 주석처리함
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
