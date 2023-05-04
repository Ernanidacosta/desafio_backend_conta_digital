from typing import Optional
from sqlmodel import Field, SQLModel


class FriendsModel(SQLModel, table=True):
    __tablename__ = 'friends'

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    birthday: str
    username: str
    user_id: str
