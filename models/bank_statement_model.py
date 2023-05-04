from typing import Optional
from sqlmodel import Field, SQLModel


class BankStatementModel(SQLModel, table=True):
    __tablename__ = 'bank_statement'

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key='persons.id')
    friend_id: Optional[int] = Field(default=None, foreign_key='friends.id')
    value: int
    date: str
    from_card: str
