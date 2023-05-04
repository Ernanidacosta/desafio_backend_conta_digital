from typing import List

from fastapi import APIRouter, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.friends_model import FriendsModel

from core.deps import get_session


router = APIRouter()


# POST Friend
@router.post(
    '/account/friend',
    status_code=status.HTTP_201_CREATED,
    response_model=FriendsModel,
)
async def post_friend(
    person: FriendsModel, db: AsyncSession = Depends(get_session)
):
    new_friend = FriendsModel(
        first_name=person.first_name,
        last_name=person.last_name,
        birthday=person.birthday,
        username=person.username,
        user_id=person.user_id,
    )
    db.add(new_friend)
    await db.commit()
    return new_friend


# GET Friends
@router.get('/account/friends', response_model=List[FriendsModel])
async def get_friends(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FriendsModel)
        result = await session.execute(query)
        friends: List[FriendsModel] = result.scalars().all()

        return friends
