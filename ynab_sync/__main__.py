import argparse
import os
from datetime import date
from uuid import UUID

from ynab_sync.constants import (
    ENV_GOCARDLESS_ACCOUNT_ID,
    ENV_GOCARDLESS_SECRET_ID,
    ENV_GOCARDLESS_SECRET_KEY,
    ENV_YNAB_ACCOUNT_ID,
    ENV_YNAB_BUDGET_ID,
    ENV_YNAB_TOKEN,
)

from .cli import upload

COMMANDS = {
    "upload": upload,
}


def add_upload_arguments(parser: argparse.ArgumentParser):
    upload_parser.add_argument(
        "--ynab-token",
        action="store",
        type=str,
        required=False,
        help="YNAB Access Token",
    )

    upload_parser.add_argument(
        "--ynab-budget-id",
        action="store",
        type=UUID,
        required=False,
        help="YNAB Budget ID",
    )

    upload_parser.add_argument(
        "--ynab-account-id",
        action="store",
        type=UUID,
        required=False,
        help="YNAB Account ID",
    )

    upload_parser.add_argument(
        "--gocardless-secret-id",
        action="store",
        type=str,
        required=False,
        help="GoCardless Secret ID",
    )

    upload_parser.add_argument(
        "--gocardless-secret-key",
        action="store",
        type=str,
        required=False,
        help="GoCardless Secret key",
    )

    upload_parser.add_argument(
        "--gocardless-account-id",
        action="store",
        type=UUID,
        required=False,
        help="GoCardless Account ID",
    )

    upload_parser.add_argument(
        "--date-from",
        action="store",
        type=date.fromisoformat,
        required=False,
        help="Date from which you want transactions to be uploaded",
    )

    upload_parser.add_argument(
        "--date-to",
        action="store",
        type=date.fromisoformat,
        required=False,
        help="Date from which you want transactions to be uploaded",
    )

    upload_parser.set_defaults(
        ynab_token=os.environ.get(ENV_YNAB_TOKEN),
        ynab_account_id=os.environ.get(ENV_YNAB_ACCOUNT_ID),
        ynab_budget_id=os.environ.get(ENV_YNAB_BUDGET_ID),
        gocardless_secret_id=os.environ.get(ENV_GOCARDLESS_SECRET_ID),
        gocardless_secret_key=os.environ.get(ENV_GOCARDLESS_SECRET_KEY),
        gocardless_account_id=os.environ.get(ENV_GOCARDLESS_ACCOUNT_ID),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "YNAB Sync",
    )

    subparsers = parser.add_subparsers(dest="command")
    upload_parser = subparsers.add_parser("upload")

    add_upload_arguments(upload_parser)

    args = parser.parse_args()
    print(args)

    handler = COMMANDS[args.command]
    del args.command

    handler(**args.__dict__)

    # gocardless = subparsers.add_parser("gocardless")
