from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

from app.database import Base



class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
