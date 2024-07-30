from model.appmodel import Users
from model.schema import users_schema
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(db: AsyncSession, user: users_schema.Users):
    db_user = Users(email=user.email,
                    password=user.password,
                    name=user.name,
                    sex=user.sex,
                    birth=user.birth,
                    address=user.address,
                    phone=user.phone)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
