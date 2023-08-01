from datetime import date

from pydantic import BaseModel, Field


class YNABTransaction(BaseModel):
    account_id: str
    date: date
    amount: int
    payee_name: str | None = Field(default="")
    memo: str = Field(default="")
    cleared: str
    approved: bool
    import_id: str


class YNABTransactions(BaseModel):
    transactions: list[YNABTransaction]