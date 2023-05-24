from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings


class TransferModel(settings.DBBaseModel):
    __tablename__ = 'transfer'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    friend_id = Column(String)
    total_to_transfer = Column(Integer)
    billing_card_id = Column(Integer, ForeignKey('billing_card.id'))
    
    billing_card = relationship("BillingCardModel", back_populates="transfer")


class BillingCardModel(settings.DBBaseModel):
    __tablename__ = 'billing_card'

    id = Column(Integer, primary_key=True)
    card_id = Column(String)

    transfer = relationship("TransferModel", back_populates="billing_card")
