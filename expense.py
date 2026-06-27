from datetime import datetime

class Expense:
    def __init__(self, description, amount, category):
        self.description = description      # What was bought
        self.amount = amount                # How much spent (in ₹)
        self.category = category.lower()    # fuel, transport, food etc.
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M")  # Auto timestamp

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        expense = cls(data["description"], data["amount"], data["category"])
        expense.date = data["date"]
        return expense

    def __str__(self):
        return f"[{self.date}] {self.description} | ₹{self.amount} | Category: {self.category}"