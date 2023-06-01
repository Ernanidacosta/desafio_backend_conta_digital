from pytz import timezone

from typing import Optional, List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from models.person_model import PersonModel
from core.configs import settings
from core.security import verify_password


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/users/login'
)


async def authenticate(username: str, password: str, db: AsyncSession) -> Optional[PersonModel]:
    async with db as session:
        query = select(PersonModel).filter(PersonModel.username == username)
        result = await session.execute(query)
        user: PersonModel = result.scalars().unique().one_or_none()

        if not user:
            return None

        if not verify_password(password, user.password):
            return None


def _create_token(type_token: str, lifetime: timedelta, sub: str) -> str:
    payload = {}

    recife = timezone('America/Recife')
    expiration = datetime.now(tz=recife) + lifetime

    payload['type'] = type_token
    payload['exp'] = expiration
    payload['iat'] = datetime.now(recife)
    payload['sub'] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def create_token_access(sub: str) -> str:

    return _create_token(
        type_token='access_token',
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
