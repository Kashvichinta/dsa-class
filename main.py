expenses=[]
def show_menu():
    print("Expenses Tracker")
    print("1.Add expense")
    print("2.View Expense")
    print("3.Exit")
def add_expense():
    name=input("Enter Expense name: ")   
    try:
        amount=float(input("Enter Amount:"))
    except ValueError:
        print("Inavalid amount!Please enter a number:")
        return
    expense={
        "name":name,
        "amount":amount
    }       
    expenses.append(expense)
    print("Expense added successfully")
def view_expenses():
    if not expenses:
        print("No expenses found")
        return
    print("---Expenses list---")
    total=0
    for expense in expenses:
        print(f"{expense['name']} - {expense['amount']}")
        total+=expense["amount"]
    print(f"Total Expense:{total}")    
def main():
    while True:
        show_menu()
        choice=input("enter choice:")
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            print("exiting...Thank You")
        else:
            print("invalid choice...Try again")

if __name__=="__main__":
    main()

    
