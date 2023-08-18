import os
from uuid import UUID

from pydantic import Field
from pydantic.dataclasses import dataclass

from ynab_sync.constants import (
    ENV_GOCARDLESS_ACCOUNT_ID,
    ENV_GOCARDLESS_SECRET_ID,
    ENV_GOCARDLESS_SECRET_KEY,
    ENV_YNAB_ACCOUNT_ID,
    ENV_YNAB_BUDGET_ID,
    ENV_YNAB_TOKEN,
)


@dataclass
class GocardlessCredentials:
    gocardless_secret_id: str = Field(
        default_factory=lambda: os.getenv(ENV_GOCARDLESS_SECRET_ID, "")
    )
    gocardless_secret_key: str = Field(
        default_factory=lambda: os.getenv(ENV_GOCARDLESS_SECRET_KEY, "")
    )


@dataclass
class YnabCredentials:
    ynab_token: str = Field(default_factory=lambda: os.getenv(ENV_YNAB_TOKEN, ""))


@dataclass
class YnabConfig:
    ynab_budget_id: UUID = Field(
        default_factory=lambda: UUID(os.getenv(ENV_YNAB_BUDGET_ID, ""))
    )
    ynab_account_id: UUID = Field(
        default_factory=lambda: UUID(os.getenv(ENV_YNAB_ACCOUNT_ID, ""))
    )


@dataclass
class GocardlessConfig:
    gocardless_account_id: UUID = Field(
        default_factory=lambda: UUID(os.getenv(ENV_GOCARDLESS_ACCOUNT_ID, ""))
    )


@dataclass
class YnabSyncConfig(
    GocardlessCredentials,
    GocardlessConfig,
    YnabCredentials,
    YnabConfig,
):
    ...


def read_config():
    pass
