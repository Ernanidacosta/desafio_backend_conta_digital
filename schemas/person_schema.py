from typing import Optional

from pydantic import BaseModel


class PersonSchemaBase(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    birthday: str
    username: str
    user_id: str

    class Config:
        orm_mode = True


class PersonSchemaCreate(PersonSchemaBase):
    password: str


class PersonSchemaUpdate(PersonSchemaBase):
    first_name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[str]
    username: Optional[str]
    user_id: Optional[str]
    password: Optional[str]
