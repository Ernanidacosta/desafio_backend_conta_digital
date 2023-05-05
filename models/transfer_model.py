from sqlalchemy import Column, Integer, String
from core.configs import settings



class TransferModel(settings.DBBaseModel):
    __tablename__ = 'transfer'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: str = Column(String(100))
    friend_id: str = Column(String(100))
    total_to_transfer: int = Column(Integer)
    billing_card: str = Column(String(100))

