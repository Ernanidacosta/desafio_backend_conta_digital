from typing import List
from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.transfer_model import TransferModel

from schemas.bank_statement_schema import BankStatementSchema
from schemas.transfer_schema import TransferSchema

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.card_model import CardModel

from schemas.card_schema import CardSchema

from core.deps import get_session

router = APIRouter()


# POST transfer
@router.post(
    '/transfer',
    status_code=status.HTTP_201_CREATED,
    response_model=TransferSchema,
)
async def post_transfer(
    transfer: TransferSchema, db: AsyncSession = Depends(get_session)
):
    new_transfer = TransferModel(
        user_id=transfer.user_id,
        friend_id=transfer.friend_id,
        total_to_transfer=transfer.total_to_transfer,
        billing_card=transfer.billing_card
    )
    db.add(new_transfer)
    await db.commit()
    return new_transfer


@router.get('/bank-statement', response_model=List[TransferSchema])
async def get_bank_statement(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TransferModel)
        result = await session.execute(query)
        bank_statement: List[TransferModel] = result.scalars().all()

        # Map TransferModel objects to TransferSchema objects
        return [TransferSchema(
            id=transfer.id,
            user_id=transfer.user_id,
            friend_id=transfer.friend_id,
            total_to_transfer=transfer.total_to_transfer,
            billing_card=transfer.billing_card
        ) for transfer in bank_statement]


# GET Bank Statements by id
@router.get(
    '/bank-statement/{usertId}',
    response_model=TransferSchema,
    status_code=status.HTTP_200_OK,
)
async def get_bank_statement_by_id(
    user_id: str, db: AsyncSession = Depends(get_session)
):
    async with db as session:
        query = select(TransferModel).filter(
            TransferModel.user_id == user_id
        )
        result = await session.execute(query)

        transfer = result.scalar_one_or_none()

        if transfer:
            return transfer

        raise HTTPException(
            detail='Bank statement not found',
            status_code=status.HTTP_404_NOT_FOUND,
        )


# POST Card
@router.post(
    '/card',
    status_code=status.HTTP_201_CREATED,
    response_model=CardSchema,
)
async def card_create(
    card: CardSchema, db: AsyncSession = Depends(get_session)
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
@router.get('/cards', response_model=List[CardSchema])
async def get_cards(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CardModel)
        result = await session.execute(query)
        cards: List[CardModel] = result.scalars().all()

        return cards
