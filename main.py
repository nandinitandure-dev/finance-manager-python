from file_manager import load_expenses, save_expenses, backup_data
from menu import show_menu, add_expense, view_expenses, search_expenses
from reports import category_summary, monthly_report

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == '2':
            view_expenses(expenses)

        elif choice == '3':
            category_summary(expenses)

        elif choice == '4':
            monthly_report(expenses)

        elif choice == '5':
            search_expenses(expenses)

        elif choice == '6':
            backup_data()

        elif choice == '7':
            save_expenses(expenses)
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()