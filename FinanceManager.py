import csv
from Transaction import Transaction

class FinanceManager:
    # Storing every transaction into an empty list
    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        # Adding a new transaction to the transactions list
        self.transactions.append(transaction)
        print("Transaction added successfully.")

    def generateReport(self):

        # Sum of all income
        total_income = 0
        for t in self.transactions:
            if t.typeOfTransaction == "income":
                total_income += t.amount

        # Sum of all expenses
        total_expense = 0
        for t in self.transactions:
            if t.typeOfTransaction == "expense":
                total_expense += t.amount

        total_savings = total_income - total_expense

        print(f"Total Income:  ${total_income}")
        print(f"Total Expenses: ${total_expense}")
        print(f"Total Savings: ${total_savings}")

    def filterByCategory(self, category):
        # Creating an empty list to store filtered transactions
        filtered_transactions = []

        for t in self.transactions:
            if t.category == category:
                filtered_transactions.append(t)

        return filtered_transactions


    def saveToFile(self, filename):

        #writing csv file like a Dictionary to get every headers
        with open(filename, "w", newline="") as new_file:
            fieldnames = ['Date', 'Amount', 'Type', 'Category']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()

            for t in self.transactions:
                row = {'Date': t.date, 'Amount': t.amount, 'Type': t.typeOfTransaction, 'Category': t.category}
                csv_writer.writerow(row)

    def loadFromFile(self, filename):
        with open(filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                date = row['Date']
                amount = float(row['Amount'])
                typeOfTransaction = row['Type']
                category = row['Category']

                #entering a new transaction to the transaction array
                transaction = Transaction(date, amount, typeOfTransaction, category)
                self.transactions.append(transaction)

    def getTopExpenses(self, n):
        # Initialize an empty list to hold expense transactions
        expenses = []

        # Loop through all transactions and add expenses to the list
        for t in self.transactions:
            if t.typeOfTransaction == "expense":
                expenses.append(t)

        #sorting array depends on amount as descending order
        expenses.sort(key=lambda x: x.amount, reverse=True)

        #as long as n is less than size of the expenses , program will be executed
        if not n>len(expenses):

            top_expenses = expenses[:n]
        return top_expenses





    def getCategorySummary(self):
        summary = {}


        for t in self.transactions:
            if t.category not in summary:
                summary[t.category] = {"income": 0, "expense": 0}

            # Setting the Transaction type
            if t.typeOfTransaction == "income":

                #getting key, value with amount of them
                summary[t.category]["income"] += t.amount
            elif t.typeOfTransaction == "expense":
                summary[t.category]["expense"] += t.amount

        return summary


# Example usage
if __name__ == "__main__":
    #object of the FinanceManager class
    fm = FinanceManager()

    # Adding some transactions
    tr1 = Transaction("2024-12-14", 1000.0, "expense", "food")
    tr2 = Transaction("2024-12-15", 500.0, "income", "salary")

    fm.addTransaction(tr1)
    fm.addTransaction(tr2)

    fm.generateReport()

    #Saving transactions to the file
    fm.saveToFile("transactions.csv")

    #Loading transactions from the file
    fm.loadFromFile("transactions.csv")
    fm.generateReport()
