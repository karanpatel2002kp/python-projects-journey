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
    print("Add expense")
elif choice ==2:
    print("view expenses")
elif choice ==3:
    print("total expenses")
elif choice == 4:
    print("exit")
else:
    print("Invalid choice")



