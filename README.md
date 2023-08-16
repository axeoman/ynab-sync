
# Table of Contents

1.  [Before you start, disclaimer:](#org6334dca)
2.  [Usage (Not that friendly yet, sorry!)](#org7ea30ab)
    1.  [Docker usage](#org8d49098)
    2.  [Getting budget and account ids](#org9deac59)
3.  [Development](#org649ea06)
    1.  [API Used](#orgc927cc5)
    2.  [TODOs](#orgf92324a)
    3.  [Initial requirements](#org82afaf3)

You Need a Budget (<https://www.ynab.com/>) does not have integrations with many Europe banks (e.g. Finland OP or SPankki) but there is atleast one free API that can grab data from them: GoCardless (<https://gocardless.com/> formerly Nordigen).

This tool allows you to sync between your bank account (if it is supported by GoCardless) and upload transactions to YNAB on regular basis (e.g. crontab job could suffice). This is much better than converting CSVs from banks and upload it manually to YNAB on weekly basis.

Personally I started to use that in July 2023 for my main budget with OP and SPankki banks and not facing any issues anymore with it (have a separate cron job for each bank account that runs `upload` command 5 times per day).


<a id="org6334dca"></a>

# Before you start, disclaimer:

This tool is still in MVP state: developed poorly and fastest way possible. Alpha version I would say.

So these are things that may irritate you: 

-   Too hard to start for a non-developer (getting all thise IDs is still manual)
-   No proper packaging: docker is probably fine but has no way change date range properly (only by editing Dockerfile instead)
-   poor error handling (there are a lot of cases when you **will** encounter hard to understand errors because of a random bug, unexpected API response, etc..)


<a id="org7ea30ab"></a>

# Usage (Not that friendly yet, sorry!)

Currently in order to use the tool you need atleast Python version 3.11 and obtain these unique strings:

-   Secret ID and Secret Key from your GoCardless account (you can create one free of charge)
-   Account ID from GoCardless API connected to your bank account (listed in Step 5 in [Quick Start Guide](https://developer.gocardless.com/bank-account-data/quick-start-guide) at GoCardless docs)
-   YNAB access token (you can grab it from <https://app.ynab.com/settings/developer>)
-   YNAB Budget and Account IDs where you want to import data: <https://api.ynab.com/v1#/Budgets/getBudgets> and <https://api.ynab.com/v1#/Accounts/getAccounts> call could help with that (consult <https://api.ynab.com/> if needed)

Clone this repository:

    git clone https://github.com/axeoman/ynab-sync.git

Install with pip:

    python -m pip install .

After getting all what is needed and installing requirements (`pip install -r requirements.txt`) you can use `upload`
command in order to download transactions from GoCardless Account and upload them to YNAB budget/account:

    ynab-sync upload --ynab-token=$YNAB_TOKEN --ynab-budget-id=$YNAB_BUDGET_ID --ynab-account-id=$YNAB_ACCOUNT_ID --gocardless-secret-id=$GOCARDLESS_SECRET_ID --gocardless-secret-key=$GOCARDLESS_SECRET_KEY --gocardless-account-id=$GOCARDLESS_ACCOUNT_ID --date-from=`date -d '-7 day' '+%Y-%m-%d'` 


<a id="org8d49098"></a>

## Docker usage

Probably fastest way to use it in any environment is to use docker container (that is how I currently use it for myself).

-   clone this repository (or grab latest release if it's broken)

    git clone https://github.com/axeoman/ynab-sync.git

-   Store you credentials in `.env` file e.g. `sandbox.env` ([example](https://github.com/axeoman/ynab-sync/blob/main/bank.example.env)) and run following commands
-   Build docker container

    docker build -t ynab-sync .

-   Run docker container. Note: it will grab all transactions from 7 days before current date (consult [Dockerfile](https://github.com/axeoman/ynab-sync/blob/main/Dockerfile) for details)

    docker run --env-file=sandbox.env --rm ynab-sync


<a id="org9deac59"></a>

## Getting budget and account ids

There are three commands that can help you with getting nessesary identifiers (probably buggy, but still)

-   `gocardless banks` - list of banks that needed for next step (auth)
-   `gocardless generate_bank_auth_link` - creates http link in order to auth with your bank
-   `gocardless list_requisition_account` - get GOCARDLESS<sub>ACCOUNT</sub><sub>ID</sub> that is nessesary for `upload` command
-   `ynab budgets` - lists budgets in your YNAB account (YNAB<sub>BUDGET</sub><sub>ID</sub>)
-   `ynab accounts` - lists accoutns in your YNAB budget (YNAB<sub>ACCOUNT</sub><sub>ID</sub>)


<a id="org649ea06"></a>

# Development

I have an e2e happy path test: feel free to submit a PR :)


<a id="orgc927cc5"></a>

## API Used

-   GoCardless (Nordigen) API: <https://developer.gocardless.com/bank-account-data/endpoints>
-   YNAB API: <https://api.ynab.com/v1#/>


<a id="orgf92324a"></a>

## TODOs

-   [X] MVP
-   [X] end-to-end automated tests based on results of MVP
-   [X] separate cli from logic
-   [ ] refactor API classes
-   [X] add usefull commands (building links, getting GoCardless and YNAB account/budget information)
-   [ ] add packaging
-   [ ] add simple interactive command that provides you with .env file and all nessesary variables to get bank data


<a id="org82afaf3"></a>

## Initial requirements

-   Upload fresh bank transactions to YNAB
-   Supported banks: OP, Spankki
-   Should be stateless
-   Runs a command (with appeal <https://github.com/larryhastings/appeal>) (can be used in cron):
    Params:
    -   YNAB auth token
    -   YNAB budget<sub>id</sub>
    -   YNAB account<sub>id</sub>
    -   secrets from GoCardless
    -   account<sub>id</sub> / name of the bank insitution to upload
    -   transactions time range
-   Command should report number of imported and duplicated transactions
-   Nice to have:
    -   command that build authorization link (might be needed every 3 months)
    -   command that provide budget<sub>id</sub>/account<sub>id</sub> information (list of available with name)

