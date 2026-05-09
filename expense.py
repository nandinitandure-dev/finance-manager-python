class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_list(self):
        return [self.amount, self.category, self.date, self.description]

    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount} - {self.description}"  