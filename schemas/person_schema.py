from typing import Optional

from pydantic import BaseModel as SCBaseModel


class PersonSchema(SCBaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    birthday: str
    password: str
    username: str
    user_id: str

    class Config:
        orm_mode = True
