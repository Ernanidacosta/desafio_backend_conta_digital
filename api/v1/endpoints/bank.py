from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.transfer_model import TransferModel, BillingCardModel
from schemas.transfer_schema import TransferSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
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
    billing_card_data = transfer.billing_card

    billing_card = BillingCardModel(card_id=billing_card_data.card_id)
    db.add(billing_card)
    await db.flush()

    new_transfer = TransferModel(
        user_id=transfer.user_id,
        friend_id=transfer.friend_id,
        total_to_transfer=transfer.total_to_transfer,
        billing_card=billing_card,
    )
    db.add(new_transfer)
    await db.commit()
    return new_transfer


@router.get('/bank-statements', response_model=List[TransferSchema])
async def get_bank_statement(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TransferModel).options(
            selectinload(TransferModel.billing_card)
        )
        result = await session.execute(query)
        bank_statement: List[TransferModel] = result.scalars().all()

        return bank_statement


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
        query = select(TransferModel).filter(TransferModel.user_id == user_id)
        result = await session.execute(query)

        transfer = result.scalar_one_or_none()

        if transfer:
            return transfer

        raise HTTPException(
            detail='Bank statement not found',
            status_code=status.HTTP_404_NOT_FOUND,
        )
