import csv
import os
from expense import Expense

FILE_PATH = "data/expenses.csv"

# ✅ LOAD DATA FROM CSV
def load_expenses():
    expenses = []

    if not os.path.exists(FILE_PATH):
        return expenses

    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header

        for row in reader:
            date, category, amount, description = row
            expenses.append(Expense(amount, category, date, description))

    return expenses


# ✅ SAVE DATA TO CSV
def save_expenses(expenses):
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])

        for exp in expenses:
            writer.writerow(exp.to_list())


# ✅ BACKUP DATA
def backup_data():
    import shutil
    from datetime import datetime

    backup_file = f"backups/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    shutil.copy(FILE_PATH, backup_file)
    print(f"Backup created: {backup_file}")