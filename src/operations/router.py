import time

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import UserManager
from src.auth.schemas import UserCreate, ShowUser

user_router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


async def _create_new_user(body: UserCreate, session) -> ShowUser:
    async with session.begin():
        user_man = UserManager(session)
        user = await user_man.create_user(
            username=body.username,
            surname=body.surname,
            email=body.email,
        )
        return ShowUser(
            user_id=user.user_id,
            username=user.name,
            surname=user.surname,
            email=user.email,
            is_active=user.is_active,
        )


@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate) -> ShowUser:
    return await _create_new_user(body)
