# Rewritten Python Script for Financial Forecasting

import pandas as pd

import os

from datetime import datetime, timedelta



# Create a directory for CSV storage

data_dir = "data"

try:

    os.makedirs(data_dir, exist_ok=True)

    print(f"Directory '{data_dir}' created successfully or already exists.")

except OSError as e:

    print(f"Error creating directory '{data_dir}': {e}")

    exit(1)



class AccountManager:

    VALID_TRANSACTION_TYPES = ["Credit", "Debit", "Transfer"]



    def __init__(self, name, initial_balance):

        self.name = name

        self.balance = initial_balance

        self.transactions = pd.DataFrame(columns=["Date", "Description", "Amount", "Transaction_Type"])

        print(f"Initialized AccountManager for {self.name} with balance ${self.balance:.2f}")



    def add_transaction(self, date, description, amount, transaction_type):

        print(f"Adding transaction: {date}, {description}, {amount}, {transaction_type}")

        if transaction_type not in self.VALID_TRANSACTION_TYPES:

            raise ValueError(f"Invalid transaction type: {transaction_type}. Must be one of {self.VALID_TRANSACTION_TYPES}.")



        transaction = {

            "Date": pd.to_datetime(date, errors='coerce'),

            "Description": description,

            "Amount": amount,

            "Transaction_Type": transaction_type

        }

        if pd.isna(transaction["Date"]):

            raise ValueError("Invalid date format for transaction.")



        self.transactions = pd.concat([self.transactions, pd.DataFrame([transaction])], ignore_index=True)

        print(f"Transaction added: {transaction}")



        if transaction_type == "Credit":

            self.balance += amount

        elif transaction_type == "Debit":

            self.balance -= amount



        print(f"Updated balance: ${self.balance:.2f}")



    def export_to_csv(self):

        print("Exporting transactions to CSV...")

        if self.transactions.empty:

            print("No transactions to export.")

            return



        csv_file = os.path.join(data_dir, f"{self.name}_transactions.csv")



        try:

            self.transactions.to_csv(csv_file, index=False)

            print(f"Transactions exported to {csv_file}")

        except IOError as e:

            print(f"Error writing to file '{csv_file}': {e}")



    def predict_balance(self, days_ahead, start_date=None):

        print(f"Predicting balance {days_ahead} days ahead...")

        if start_date:

            start_date = pd.to_datetime(start_date, errors='coerce')

            if pd.isna(start_date):

                start_date = datetime.now()

        else:

            start_date = datetime.now()



        future_date = start_date + timedelta(days=days_ahead)

        print(f"Balance forecast for {future_date.strftime('%Y-%m-%d')}: ${self.balance:.2f}")



# Example usage of the AccountManager class

def main():

    print("Starting main function...")

    account = AccountManager("Checking", 3000)



    try:

        account.add_transaction("2024-01-05", "Paycheck", 1500, "Credit")

        account.add_transaction("2024-01-08", "Utilities", -200, "Debit")

        account.add_transaction("2024-01-15", "Groceries", -150, "Debit")

    except ValueError as e:

        print(f"Error adding transaction: {e}")



    account.export_to_csv()

    account.predict_balance(30, start_date="2024-01-01")

    print("Main function completed.")



if __name__ == "__main__":

    main()

