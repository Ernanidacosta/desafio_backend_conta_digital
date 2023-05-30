from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from models.person_model import PersonModel
from models.transfer_model import BillingCardModel
from models.transfer_model import TransferModel
from schemas.transfer_schema import TransferSchema
from core.deps import get_session, get_current_user


router = APIRouter()


# POST transfer
@router.post(
    '/transfer',
    status_code=status.HTTP_201_CREATED,
    response_model=TransferSchema,
)
async def post_transfer(
    transfer: TransferSchema,
    db: AsyncSession = Depends(get_session),
    user_loged: PersonModel = Depends(get_current_user)
):
    billing_card_data = transfer.billing_card

    billing_card = BillingCardModel(card_id=billing_card_data.card_id)
    db.add(billing_card)
    await db.flush()

    new_transfer = TransferModel(
        user_id=user_loged.user_id,
        friend_id=transfer.friend_id,
        total_to_transfer=transfer.total_to_transfer,
        billing_card=billing_card,
    )
    db.add(new_transfer)
    await db.commit()

    if new_transfer:
        return new_transfer
    
    raise HTTPException(
        detail='Transfer not created',
        status_code=status.HTTP_400_BAD_REQUEST,
        )

@router.get('/bank-statements',
            response_model=List[TransferSchema],
            status_code=status.HTTP_200_OK
)
async def get_bank_statement(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TransferModel).options(
            selectinload(TransferModel.billing_card)
        )
        result = await session.execute(query)
        bank_statement: List[TransferModel] = result.scalars().all()

        if bank_statement:
            return bank_statement

        raise HTTPException(
            detail='Bank statement not found',
            status_code=status.HTTP_404_NOT_FOUND,
            )

# GET Bank Statements by id
@router.get(
    '/bank-statement/{transferId}',
    response_model=TransferSchema,
    status_code=status.HTTP_200_OK,
)
async def get_bank_statement_by_id(
    transferId: int, db: AsyncSession = Depends(get_session)
):
    async with db as session:
        query = (
            select(TransferModel)
            .join(TransferModel.billing_card)
            .filter(TransferModel.id == transferId)
            .options(selectinload(TransferModel.billing_card))
        )
        result = await session.execute(query)

        transfer = result.scalar_one_or_none()

        if transfer:
            return transfer

        raise HTTPException(
            detail='Transfer not found',
            status_code=status.HTTP_404_NOT_FOUND,
        )
