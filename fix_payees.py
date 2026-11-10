import datetime
import time
import uuid
from ynab_sync.ynab.api import YnabAPI
import os

from ynab_sync.constants import ENV_YNAB_BUDGET_ID, ENV_YNAB_TOKEN

if __name__ == "__main__":
    ynab_token: str = os.getenv(ENV_YNAB_TOKEN, "")
    ynab_budget_id = uuid.UUID(os.getenv(ENV_YNAB_BUDGET_ID, ""))

    print(ynab_budget_id)
    ynab_api = YnabAPI(access_token=ynab_token)

    transactions = ynab_api.get_transactions_by_category(
        budget_id=ynab_budget_id,
        category_id=uuid.UUID("cc36a031-ac5f-4717-91c1-a108166b7d46"),
        since_date=datetime.date(year=2019, month=1, day=1),
    )

    for transaction in transactions["data"]["transactions"]:
        if (
            transaction["type"] == "transaction"
            and transaction["payee_id"] == "8fc14337-74e8-4d0e-9515-b2a7ef0c35e9"
            and transaction["import_payee_name"].lower().startswith("prisma")
        ):
            print(
                transaction["id"],
                transaction["date"],
                transaction["amount"],
                transaction["payee_name"],
                transaction["import_payee_name"],
            )

            response = ynab_api.update_transaction_payee_id(
                budget_id=ynab_budget_id,
                transaction_id=transaction["id"],
                payee_id=uuid.UUID("c2f8abf7-4013-465c-899a-5e039e4eb078"),
            )
            time.sleep(0.1)
