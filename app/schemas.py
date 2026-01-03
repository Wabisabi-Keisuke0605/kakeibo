from datetime import date, datetime
from pydantic import BaseModel

# ----------------------------
#     収入クラス
#-----------------------------

class IncomeCreate(BaseModel):
    amount: int
    category: str
    date: date


class IncomeResponse(BaseModel):
    id: int
    amount: int
    category: str
    date: date
    created_at: datetime

    class Config:
        from_attributes = True



# ----------------------------
#     支出クラス
#-----------------------------

class ExpenseCreate(BaseModel):
    amount: int
    category: str
    date: date


class ExpenseResponse(BaseModel):
    id: int
    amount: int
    category: str
    date: date
    created_at: datetime

    class Config:
        from_attributes = True


# ----------------------------
#     収支サマリー
# ----------------------------

class SummaryResponse(BaseModel):
    year: int
    month: int
    total_income: int
    total_expense: int
    balance: int