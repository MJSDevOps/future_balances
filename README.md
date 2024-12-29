- - # Financial Forecasting Script

    A Python-powered financial forecasting tool crafted for freelancers, this application offers a fresh approach to short-term financial planning. Unlike traditional budgeting apps that rely on past spending habits, this tool focuses on future projections by allowing users to input anticipated income and planned expenses.

    ## Key Features
    - Effortless Transaction Tracking: Log and categorize income and expenses in just a few clicks.
    - CSV Export: Save transaction histories in CSV format for deeper analysis or record-keeping.
    - Short-Term Balance Projections: Plan ahead by forecasting your account balance based on expected financial activity.
      
    ## Benefits
    - Plan with Precision: Gain insights into your future financial standing, helping you make smarter decisions about saving and spending.
    - Tailored for Freelancers: With variable income being a common challenge, this tool provides more accurate short-term financial insights, enabling better decision-making around spending, saving, or increasing income.
    - Less Reliable over Time: While projections naturally become less accurate the further they extend, you can mitigate this by:
      - Treating savings contributions as planned expenses to buffer against unexpected costs.
      - Adopting conservative income estimates, reducing reliance on overly optimistic predictions for long-term planning.
    - Intuitive and Accessible: The user-friendly CLI ensures anyone can streamline their financial planning without hassle.
    - A Learning Experience for Python Enthusiasts: As one of my first practicle Python projects, this tool is designed to be educational.
      - Every section of the code is thoroughly explained, making it easy for other beginners to learn and customize.
      - It’s an ideal project for anyone looking to explore practical Python applications that adapt to real-world data changes.
        

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