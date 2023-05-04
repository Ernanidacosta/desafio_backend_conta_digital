from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.card_model import CardModel

from core.deps import get_session

router = APIRouter()


# POST Card
@router.post(
    '/account/card',
    status_code=status.HTTP_201_CREATED,
    response_model=CardModel,
)
async def card_create(
    card: CardModel, db: AsyncSession = Depends(get_session)
):
    new_card = CardModel(
        card_id=card.card_id,
        title=card.title,
        pan=card.pan,
        expiry_mm=card.expiry_mm,
        expiry_yyyy=card.expiry_yyyy,
        security_code=card.security_code,
        date=card.date,
    )
    db.add(new_card)
    await db.commit()
    return new_card


# GET Cards
@router.get('/account/cards', response_model=List[CardModel])
async def get_cards(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CardModel)
        result = await session.execute(query)
        cards: List[CardModel] = result.scalars().all()

        return cards
