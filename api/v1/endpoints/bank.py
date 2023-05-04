from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.bank_statement_model import BankStatementModel
from models.transfer_model import TransferModel

from schemas.bank_statement_schema import BankStatementSchema
from schemas.transfer_schema import TransferSchema

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.card_model import CardModel

from schemas.card_schema import CardSchema

from core.deps import get_session

router = APIRouter()


router = APIRouter()


# POST transfer
@router.post(
    '/account/transfer',
    status_code=status.HTTP_201_CREATED,
    response_model=TransferSchema,
)
async def post_transfer(
    transfer: TransferSchema, db: AsyncSession = Depends(get_session)
):
    new_transfer = TransferSchema(
        friend_id=transfer.friend_id,
        user_id=transfer.user_id,
        value=transfer.value,
        from_card=transfer.billing_card.card_id,
    )
    db.add(new_transfer)
    await db.commit()
    return new_transfer


# GET Bank Statements
@router.get('/account/bank-statement', response_model=BankStatementSchema)
async def get_bank_statement(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(BankStatementModel)
        result = await session.execute(query)
        bank_statement: List[BankStatementModel] = result.scalars().all()

        return bank_statement


# GET GET Bank Statements by id
@router.get(
    '/account/bank-statement/{usertId}',
    response_model=BankStatementSchema,
    status_code=status.HTTP_200_OK,
)
async def get_bank_statement_by_id(
    user_id: str, db: AsyncSession = Depends(get_session)
):
    async with db as session:
        query = select(BankStatementModel).filter(
            BankStatementModel.id == user_id
        )
        result = await session.execute(query)

        bank_statement = result.scalar_one_os_none()

        if bank_statement:
            return bank_statement

        raise HTTPException(
            detail='Bank statement not found',
            status_code=status.HTTP_404_NOT_FOUND,
        )


# POST Card
@router.post(
    '/account/card',
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
@router.get('/account/cards', response_model=List[CardSchema])
async def get_cards(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CardModel)
        result = await session.execute(query)
        cards: List[CardModel] = result.scalars().all()

        return cards
