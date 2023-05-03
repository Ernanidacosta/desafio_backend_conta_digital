from typing import Optional

from pydantic import BaseModel

class Person(BaseModel):
    id: Optional[int] = None
    user_id = str
    first_name = str
    birthday = str
    password = str
    username = str

class Friends(BaseModel):
    id: Optional[int] = None
    first_name = str
    birthday = str
    username = str

class Card(BaseModel):
    id: Optional[int] = None
    card_id = str
    title = str
    pan = str
    expiry_mm = str
    expiry_yyyy = str
    security_code = str
    date = str