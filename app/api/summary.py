from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import extract, func


from app.database import get_db
from app.models import Income, Expense
from app.schemas import SummaryResponse


api = APIRouter(prefix="/summary", tags=["summary"])


@api.get("", response_model=list[SummaryResponse])
def get_summary(db: Session = Depends(get_db)):

    income_query = (
        db.query(
            extract("year", Income.date).label("year"),
            extract("month", Income.date).label("month"),
            func.sum(Income.amount).label("income")
        )
        .group_by(
            extract("year", Income.date),
            extract("month", Income.date)
        )
        .all()
    )

    expense_query = (
        db.query(
            extract("year", Expense.date).label("year"),
            extract("month", Expense.date).label("month"),
            func.sum(Expense.amount).label("expense")
        )
        .group_by(
            extract("year", Expense.date),
            extract("month", Expense.date)
        )
        .all()
    )


    income_dict = {(int(r.year), int(r.month)): r.income for r in income_query}
    expense_dict = {(int(r.year), int(r.month)): r.expense for r in expense_query}


    all_keys = set(income_dict.keys()) | set(expense_dict.keys())


    result = []
    for year, month in sorted(all_keys):
        total_income = income_dict.get((year, month), 0)
        total_expense = expense_dict.get((year, month), 0)
        result.append(SummaryResponse(
            year=year,
            month=month,
            total_income=total_income,
            total_expense=total_expense,
            balance=total_income - total_expense
        ))
    return result

