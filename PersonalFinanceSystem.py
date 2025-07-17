from FinanceManager import FinanceManager
from Transaction import Transaction


def main() -> object:
    financeM = FinanceManager()
    
    print(" ")
    print("Welcome to the Personal Finance Management System.")


    while True:
        print("1. Add Transaction")
        print("2. Generate Report")
        print("3. Filter by Category")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Get Top Expenses")
        print("7. Get Category Summary")
        print("8. Exit")

        #getting input from user
        choice = input("Select an option: ")

        if choice == '1':
            date = input("Enter transaction details:Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            typeOfTransaction = input("Type (income/expense): ")
            category = input("Category: ")
            transaction = Transaction(date, amount, typeOfTransaction, category)
            financeM.addTransaction(transaction)

        elif choice == '2':
            print("Generating report...")
            financeM.generateReport()

        elif choice == '3':
            category = input("Enter a category to filter by: ")
            transactions = financeM.filterByCategory(category)
            for t in transactions:
                t.displayInfo()

        elif choice == '4':
            filename = input("Enter a filename to save : ")
            financeM.saveToFile(filename)

        elif choice == '5':
            filename = input("Enter a filename to load: ")
            financeM.loadFromFile(filename)

        elif choice == '6':
            n = int(input("Enter number of top expenses that you want to get: "))
            top_expenses = financeM.getTopExpenses(n)
            for t in top_expenses:
                t.displayInfo()

        elif choice == '7':
            summary = financeM.getCategorySummary()
            for category, amounts in summary.items():
                print(f"Category: {category}, Income: {amounts['income']}, Expense: {amounts['expense']}")

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
