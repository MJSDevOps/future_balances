# Financial Forecasting Script

This project provides a Python-based financial forecasting tool to manage transactions and predict future balances. It supports adding transactions, exporting them to CSV, and calculating projected account balances.

## Features

- Add transactions with details such as date, description, amount, and type (Credit, Debit, Transfer).
- Automatically updates account balance based on transactions.
- Exports transaction history to a CSV file.
- Predicts future balances based on a user-defined number of days ahead.

## Requirements

- Python 3.8+
- Libraries:
  - `pandas`
  - `os`
  - `datetime`

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd financial_forecasting
   ```
3. Install the required dependencies:
   ```bash
   pip install pandas
   ```

## Usage

1. Run the script:
   ```bash
   python financial_forecasting.py
   ```
2. Example interactions:
   - Add transactions:
     The script provides examples for adding transactions such as a paycheck, utilities, and groceries.
   - Export transactions to CSV:
     Transactions are saved in the `data` directory as a CSV file named `<account_name>_transactions.csv`.
   - Predict balance:
     Provides a forecasted balance for a given number of days from the specified start date.

## Example

### Input
```python
account = AccountManager("Checking", 3000)
account.add_transaction("2024-01-05", "Paycheck", 1500, "Credit")
account.add_transaction("2024-01-08", "Utilities", -200, "Debit")
account.predict_balance(30, start_date="2024-01-01")
```

### Output
```
Starting main function...
Adding transaction: 2024-01-05, Paycheck, 1500, Credit
Transaction added: {'Date': Timestamp('2024-01-05 00:00:00'), 'Description': 'Paycheck', 'Amount': 1500, 'Transaction_Type': 'Credit'}
Updated balance: $4500.00
Predicting balance 30 days ahead...
Balance forecast for 2024-01-31: $4500.00
```

## Directory Structure

```
financial_forecasting/
├── data/                     # Contains exported CSV files
├── financial_forecasting.py  # Main Python script
└── README.md                 # Documentation
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

