from expense import Expense

class User:
    def __init__(self, name):
        self.name = name                # User's name
        self.expenses = []              # List of Expense objects

    def add_expense(self, description, amount, category):
        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        return expense

    def get_total_spent(self):
        return sum(expense.amount for expense in self.expenses)

    def to_dict(self):
        return {
            "name": self.name,
            "expenses": [expense.to_dict() for expense in self.expenses]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"])
        user.expenses = [Expense.from_dict(e) for e in data["expenses"]]
        return user

    def __str__(self):
        return f"👤 {self.name} | Total Expenses: {len(self.expenses)} | Total Spent: ₹{self.get_total_spent()}"
    