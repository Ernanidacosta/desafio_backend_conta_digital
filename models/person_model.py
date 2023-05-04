from typing import Optional
from sqlmodel import Field, SQLModel


class PersonModel(SQLModel, table=True):
    __tablename__ = 'persons'

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    birthday: str
    password: str
    username: str
    user_id: str
