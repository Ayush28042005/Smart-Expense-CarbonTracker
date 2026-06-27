import json
from user import User

class Tracker:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.users = []
        self.current_user = None
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.users = [User.from_dict(u) for u in data["users"]]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")  # debug line
            self.users = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({"users": [u.to_dict() for u in self.users]}, f, indent=4)

    def add_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                print(f"❌ User '{name}' already exists!")
                return
        user = User(name)
        self.users.append(user)
        self.save_data()
        print(f"✅ User '{name}' added successfully!")

    def select_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                self.current_user = user
                print(f"✅ Switched to user: {user.name}")
                return
        print(f"❌ User '{name}' not found!")

    def add_expense(self, description, amount, category):
        if not self.current_user:
            print("❌ No user selected! Please select a user first.")
            return
        expense = self.current_user.add_expense(description, amount, category)
        self.save_data()
        from carbon_calculator import CarbonCalculator
        carbon = CarbonCalculator.get_carbon_level(category)
        print(f"✅ Expense added!")
        print(f"   💰 Amount: ₹{amount}")
        print(f"   🌍 Carbon Footprint: {carbon}")

    def view_expenses(self):
        if not self.current_user:
            print("❌ No user selected!")
            return
        from report import Report
        r = Report(self.current_user)
        r.generate_expense_report()

    def view_carbon_report(self):
        if not self.current_user:
            print("❌ No user selected!")
            return
        from report import Report
        r = Report(self.current_user)
        r.generate_carbon_report()

    def view_all_users(self):
        if not self.users:
            print("❌ No users found!")
            return
        print("\n=== All Users ===")
        for i, user in enumerate(self.users, 1):
            active = " <-- (Active)" if (self.current_user and user.name == self.current_user.name) else ""
            print(f"{i}. {user.name} | Expenses: {len(user.expenses)} | Total: ₹{user.get_total_spent()}{active}")