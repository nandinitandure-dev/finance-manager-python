def total_expense(expenses):
    return sum(e.amount for e in expenses)


def category_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount
    return summary


def monthly_report(expenses):
    report = {}
    for e in expenses:
        month = e.date[:7]
        report[month] = report.get(month, 0) + e.amount
    return report


def generate_report_file(expenses):
    with open("report.txt", "w") as f:
        f.write("===== REPORT =====\n\n")
        f.write(f"Total: ₹{total_expense(expenses)}\n\n")

        f.write("Category-wise:\n")
        for cat, amt in category_summary(expenses).items():
            f.write(f"{cat}: ₹{amt}\n")

    print("✅ Report saved as report.txt")