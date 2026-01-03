from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.api import incomes, expenses, summary

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="家計管理API",
    description="収入・支出を記録し、収支を可視化するAPI",
    version="0.1.0"
)

app.include_router(incomes.api)
app.include_router(expenses.api)
app.include_router(summary.api)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}