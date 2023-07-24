import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import user
from sqlalchemy.dialects.postgresql import UUID

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False, nullable=False)
    is_verified = Column(Boolean(), default=False, nullable=False)


class UserManager:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
            self, username: str, surname: str, email: str) -> User:
        new_user = User(
            username=username,
            surname=surname,
            email=email,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
