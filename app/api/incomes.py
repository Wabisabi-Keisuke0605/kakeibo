from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import extract


from app.models import Income
from app.schemas import IncomeCreate, IncomeResponse
from app.database import get_db


api = APIRouter(prefix="/incomes", tags=["incomes"])


@api.post("", response_model=IncomeResponse)
def create_income(income: IncomeCreate, db: Session = Depends(get_db)):
    new_income = Income(
        amount=income.amount,
        category=income.category,
        date=income.date
    )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income


@api.get("", response_model=list[IncomeResponse])
def get_incomes(
    year: int | None = None,
    month: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Income)

    if year:
        query = query.filter(extract("year", Income.date) == year)
    if month:
        query = query.filter(extract("month", Income.date) == month)

        return query.order_by(Income.date.desc()).all()
