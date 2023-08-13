TEST_YNAB_REQUEST_TRANSACTIONS = """{
  "transactions": [
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-01",
      "amount": 400000,
      "payee_name": "XXXX XXXXX",
      "memo": "Withdrawal from savings target Vero\\nhailinto",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:400000:2023-08-01:1"
    },
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-01",
      "amount": -25470,
      "payee_name": "LIDL HELSINKI HELSINKI",
      "memo": "OSTOPVM  230731\\nMF NRO 74500000000000000000336     \\nVARMENTAJA 400",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:-25470:2023-08-01:1"
    },
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-03",
      "amount": -15000,
      "payee_name": "",
      "memo": "PAYMENT Alderaan Coffe",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:-15000:2023-08-03:1"
    },
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-03",
      "amount": 45000,
      "payee_name": "MON MOTHMA",
      "memo": "For the support of Restoration of the Republic foundation",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:45000:2023-08-03:1"
    },
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-03",
      "amount": -15000,
      "payee_name": "",
      "memo": "PAYMENT Alderaan Coffe",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:-15000:2023-08-03:2"
    },
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-04",
      "amount": 45000,
      "payee_name": "MON MOTHMA",
      "memo": "For the support of Restoration of the Republic foundation",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:45000:2023-08-04:1"
    },
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-11",
      "amount": -15000,
      "payee_name": "",
      "memo": "PAYMENT Alderaan Coffe",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:-15000:2023-08-11:1"
    },
    {
      "account_id": "93ec6d1f-7d75-48de-85b4-d9caec4807c8",
      "date": "2023-08-11",
      "amount": 45000,
      "payee_name": "MON MOTHMA",
      "memo": "For the support of Restoration of the Republic foundation",
      "cleared": "cleared",
      "approved": false,
      "import_id": "YNAB:45000:2023-08-11:1"
    }
  ]
}"""

# TODO: add response that inline with ynab request
TEST_YNAB_RESPONSE_TRANSACTIONS = """{
  "data": {
    "transaction_ids": [
      "44a08db0-09d7-4a6b-82c2-f44b580345b4",
      "37f1b344-394c-4090-a139-07f41f8eb96f",
      "425f42de-f1ea-456e-b281-26f418972362",
      "9f157eee-a9aa-4108-ad64-1b8fef9a0cb5",
      "49b2f14d-e465-4ec0-a7c8-abc7ef52f5f5",
      "889a4108-0ab4-4985-a678-9e06df8d2827"
    ],
    "duplicate_import_ids": [
      "YNAB:-15000:2023-08-02:1",
      "YNAB:-15000:2023-08-02:2",
      "YNAB:45000:2023-08-02:1",
      "YNAB:45000:2023-08-02:2",
      "YNAB:45000:2023-08-02:3",
      "YNAB:-15000:2023-08-02:3",
      "YNAB:-15000:2023-08-01:1",
      "YNAB:45000:2023-08-01:1",
      "YNAB:-15000:2023-08-01:2",
      "YNAB:45000:2023-08-01:2",
      "YNAB:-15000:2023-08-01:3",
      "YNAB:45000:2023-08-01:3"
    ],
    "transactions": [
      {
        "id": "425f42de-f1ea-456e-b281-26f418972362",
        "date": "2023-08-11",
        "amount": -15000,
        "memo": "PAYMENT Alderaan Coffe",
        "cleared": "cleared",
        "approved": false,
        "flag_color": null,
        "account_id": "ba3ec939-e9a9-4386-ab65-3d45bf3ce0b3",
        "account_name": "API Test",
        "payee_id": null,
        "payee_name": null,
        "category_id": null,
        "category_name": "Uncategorized",
        "transfer_account_id": null,
        "transfer_transaction_id": null,
        "matched_transaction_id": null,
        "import_id": "YNAB:-15000:2023-08-11:2",
        "import_payee_name": "",
        "import_payee_name_original": null,
        "debt_transaction_type": null,
        "deleted": false,
        "subtransactions": []
      },
      {
        "id": "44a08db0-09d7-4a6b-82c2-f44b580345b4",
        "date": "2023-08-11",
        "amount": -15000,
        "memo": "PAYMENT Alderaan Coffe",
        "cleared": "cleared",
        "approved": false,
        "flag_color": null,
        "account_id": "ba3ec939-e9a9-4386-ab65-3d45bf3ce0b3",
        "account_name": "API Test",
        "payee_id": null,
        "payee_name": null,
        "category_id": null,
        "category_name": "Uncategorized",
        "transfer_account_id": null,
        "transfer_transaction_id": null,
        "matched_transaction_id": null,
        "import_id": "YNAB:-15000:2023-08-11:1",
        "import_payee_name": "",
        "import_payee_name_original": null,
        "debt_transaction_type": null,
        "deleted": false,
        "subtransactions": []
      },
      {
        "id": "49b2f14d-e465-4ec0-a7c8-abc7ef52f5f5",
        "date": "2023-08-11",
        "amount": -15000,
        "memo": "PAYMENT Alderaan Coffe",
        "cleared": "cleared",
        "approved": false,
        "flag_color": null,
        "account_id": "ba3ec939-e9a9-4386-ab65-3d45bf3ce0b3",
        "account_name": "API Test",
        "payee_id": null,
        "payee_name": null,
        "category_id": null,
        "category_name": "Uncategorized",
        "transfer_account_id": null,
        "transfer_transaction_id": null,
        "matched_transaction_id": null,
        "import_id": "YNAB:-15000:2023-08-11:3",
        "import_payee_name": "",
        "import_payee_name_original": null,
        "debt_transaction_type": null,
        "deleted": false,
        "subtransactions": []
      },
      {
        "id": "37f1b344-394c-4090-a139-07f41f8eb96f",
        "date": "2023-08-11",
        "amount": 45000,
        "memo": "For the support of Restoration of the Republic foundation",
        "cleared": "cleared",
        "approved": false,
        "flag_color": null,
        "account_id": "ba3ec939-e9a9-4386-ab65-3d45bf3ce0b3",
        "account_name": "API Test",
        "payee_id": "13f7ae57-4650-4e91-889a-c9504f50d18e",
        "payee_name": "MON MOTHMA",
        "category_id": null,
        "category_name": "Uncategorized",
        "transfer_account_id": null,
        "transfer_transaction_id": null,
        "matched_transaction_id": null,
        "import_id": "YNAB:45000:2023-08-11:1",
        "import_payee_name": "MON MOTHMA",
        "import_payee_name_original": null,
        "debt_transaction_type": null,
        "deleted": false,
        "subtransactions": []
      },
      {
        "id": "889a4108-0ab4-4985-a678-9e06df8d2827",
        "date": "2023-08-11",
        "amount": 45000,
        "memo": "For the support of Restoration of the Republic foundation",
        "cleared": "cleared",
        "approved": false,
        "flag_color": null,
        "account_id": "ba3ec939-e9a9-4386-ab65-3d45bf3ce0b3",
        "account_name": "API Test",
        "payee_id": "13f7ae57-4650-4e91-889a-c9504f50d18e",
        "payee_name": "MON MOTHMA",
        "category_id": null,
        "category_name": "Uncategorized",
        "transfer_account_id": null,
        "transfer_transaction_id": null,
        "matched_transaction_id": null,
        "import_id": "YNAB:45000:2023-08-11:3",
        "import_payee_name": "MON MOTHMA",
        "import_payee_name_original": null,
        "debt_transaction_type": null,
        "deleted": false,
        "subtransactions": []
      },
      {
        "id": "9f157eee-a9aa-4108-ad64-1b8fef9a0cb5",
        "date": "2023-08-11",
        "amount": 45000,
        "memo": "For the support of Restoration of the Republic foundation",
        "cleared": "cleared",
        "approved": false,
        "flag_color": null,
        "account_id": "ba3ec939-e9a9-4386-ab65-3d45bf3ce0b3",
        "account_name": "API Test",
        "payee_id": "13f7ae57-4650-4e91-889a-c9504f50d18e",
        "payee_name": "MON MOTHMA",
        "category_id": null,
        "category_name": "Uncategorized",
        "transfer_account_id": null,
        "transfer_transaction_id": null,
        "matched_transaction_id": null,
        "import_id": "YNAB:45000:2023-08-11:2",
        "import_payee_name": "MON MOTHMA",
        "import_payee_name_original": null,
        "debt_transaction_type": null,
        "deleted": false,
        "subtransactions": []
      }
    ],
    "server_knowledge": 195
  }
}
"""
