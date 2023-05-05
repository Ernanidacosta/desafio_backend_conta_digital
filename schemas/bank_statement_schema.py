from typing import Optional

from pydantic import BaseModel as SCBaseModel


class BankStatementSchema(SCBaseModel):
    id: Optional[int]
    user_id: str
    friend_id: str
    value: int
    from_card: str

    class Config:
        orm_mode = True
