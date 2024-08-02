from app.api.users.repository.users import create_user
from model.schema import users_schema
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.users.repository.users import get_user_by_email_or_phone
from app.exception import Duplicated_User


async def sign_up(db: AsyncSession, user: users_schema.Users):
    # TODO: 예외처리 필요(중복된 이메일, 유저 등)
    if await is_exisiting_user(db, user):
        # TODO: email과 phone중 뭐가 중복인지도 반환해주어야 함, 현재는 그냥 존재 여부만 반환
        raise Duplicated_User()
    return await create_user(db, user)


async def is_exisiting_user(db: AsyncSession, get_user: users_schema.UserGet):
    user = await get_user_by_email_or_phone(db, get_user)
    if user:
        return True
    else:
        return False
