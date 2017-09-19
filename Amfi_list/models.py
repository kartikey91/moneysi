from extensions import *
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum, Date, DECIMAL

class AmfiList(Base):
    __tablename__ = 'amfi_list'
    amfi_id = Column(String(300), primary_key=True)
    date = Column(Date, primary_key=True)
    fund_house = Column(String(300))
    fund_name = Column(String(300))
    investment_plan = Column(String(300))
    sales_channel = Column(String(300))
    dividend_period = Column(String(300))
    nav = Column(DECIMAL)

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        serialized_obj = {}
        for column in self.__table__.columns:
                serialized_obj[column.key] = self[column.key]
        return serialized_obj

