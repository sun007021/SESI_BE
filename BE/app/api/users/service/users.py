from app.api.users.repository.users import create_user
from model.schema import users_schema
from sqlalchemy.ext.asyncio import AsyncSession


async def sign_up(db: AsyncSession, user: users_schema.Users):
    # TODO: 예외처리 필요(중복된 이메일, 유저 등)
    return await create_user(db, user)
