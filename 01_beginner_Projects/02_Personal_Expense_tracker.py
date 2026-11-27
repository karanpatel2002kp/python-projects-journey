expenses = []

while True:
    print("==== PERSONAL====")
    print("1.Add Expense")
    print("2.view Expense")
    print("3.Total Expense")
    print("4.Exit")

    choice = int(input("enter your option:"))
    
    if choice == 1:
        expense_name = input("enter your expense name:")
        amount = float(input("enter your Amount:"))
        category = input("enter your Category:")
        expense = {
            "name": expense_name,
            "amount": amount,
            "category": category
        }
        expenses.append(expense)
        print("Add expense")
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses found")
        else:
            print("=== Your Expenses ===")
            for expense in expenses:
                print("Name:", expense["name"])
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("------------------")

        print("view expenses")
    elif choice == 3:
        total = 0
        for expense in expenses:
            total += expense["amount"]

        print("total expenses",total)
    elif choice == 4:
        print("exit")
        break
    else:
        print("Invalid choice")





