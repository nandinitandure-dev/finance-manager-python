from expense import Expense
from utils import validate_amount, validate_date
from file_manager import save_expenses
from reports import (
    category_summary,
    monthly_report,
    generate_report_file,
)

def show_menu():
    print("\n===== FINANCE MANAGER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Monthly Report")
    print("5. Generate Report File")
    print("6. Search")
    print("7. Exit")


def add_expense(expenses):
    amount = validate_amount(input("Enter amount: "))
    if amount is None:
        print("❌ Invalid amount")
        return

    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("❌ Invalid date")
        return

    desc = input("Enter description: ")

    expenses.append(Expense(amount, category, date, desc))
    save_expenses(expenses)

    print("✅ Added!")


def view_expenses(expenses):
    for e in expenses:
        print(e)


def search_expenses(expenses):
    k = input("Search keyword: ").lower()
    found = False
    for e in expenses:
        if k in e.category.lower() or k in e.description.lower():
            print(e)
            found = True
    if not found:
        print("❌ Not found")


def run_menu(expenses):
    while True:
        show_menu()
        c = input("Choice: ")

        if c == '1':
            add_expense(expenses)
        elif c == '2':
            view_expenses(expenses)
        elif c == '3':
            for k, v in category_summary(expenses).items():
                print(k, ":", v)
        elif c == '4':
            for k, v in monthly_report(expenses).items():
                print(k, ":", v)
        elif c == '5':
            generate_report_file(expenses)
        elif c == '6':
            search_expenses(expenses)
        elif c == '7':
            break
        else:
            print("Invalid")