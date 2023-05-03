from core.configs import settings

from sqlalchemy import Column, Integer, String, ForeignKey


class BankStatementModel(settings.DBBaseModel):
    __tablename__ = 'bank_statement'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("persons.id"))
    friend_id = Column(Integer, ForeignKey("friends.id"))
    value: int = Column(Integer)
    date: str = Column(String(100))
    from_card: str = Column(String(100))
