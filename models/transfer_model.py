from typing import Optional
from sqlmodel import Field, SQLModel


class TransferModel(SQLModel, table=True):
    __tablename__ = 'transfer'

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    friend_id: str
    total_to_transfer: int
    billing_card: str
