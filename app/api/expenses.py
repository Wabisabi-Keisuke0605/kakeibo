from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import extract


from app.models import Expense
from app.schemas import ExpenseCreate, ExpenseResponse
from app.database import get_db


api = APIRouter(prefix="/expenses", tags=["expenses"])


@api.post("", response_model=ExpenseCreate)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(
        amount=expense.amount,
        category=expense.category,
        date=expense.date
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@api.get("", response_model=list[ExpenseResponse])
def get_expenses(
    year: int | None = None,
    month: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Expense)

    if year:
        query = query.filter(extract("year", Expense.date) == year)
    if month:
        query = query.filter(extract("month", Expense.date) == month)

        return query.order_by(Expense.date.desc()).all()