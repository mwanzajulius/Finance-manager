class Transaction:

    #Constructor to initialize all attributes. And checks their data types.
    def __init__(self, date, amount, typeOfTransaction, category):

        if isinstance(date, str) :
            self.date = date
        else:
            raise ValueError("Date must be YYYY-MM-DD string format ")

        if isinstance(amount, (int , float)):
            self.amount = float(amount)
        else:
            raise ValueError("Amount must be numeric")

        if isinstance(typeOfTransaction, str) and (typeOfTransaction == "income" or typeOfTransaction == "expense"):
            self.typeOfTransaction = typeOfTransaction
        else:
            raise ValueError("Type must be 'income' or 'expense'")

        if isinstance(category, str):
            self.category = category
        else:
            raise ValueError("Category must be string datatype")


    def displayInfo(self):
        print(f"Date: {self.date}, Amount: {self.amount}, Type: {self.typeOfTransaction}, Category: {self.category}")

#Testing an object
tr1 = Transaction("2024-12-14", 1000.0, "expense", "food")
tr1.displayInfo()
