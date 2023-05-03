from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.friends_model import FriendsModel

from schemas.friend_schema import FriendSchema

from core.deps import get_session


router = APIRouter()


# GET Friends
@router.get('/account/friends', response_model=List[FriendSchema])
async def get_friends(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FriendsModel)
        result = await session.execute(query)
        friends: List[FriendsModel] = result.scalars().all()

        return friends

