from carbon_calculator import CarbonCalculator

class Report:
    def __init__(self, user):
        self.user = user                # The user this report belongs to

    def generate_expense_report(self):
        print(f"\n=== Expense Report for {self.user.name} ===")
        if not self.user.expenses:
            print("❌ No expenses found!")
            return
        for expense in self.user.expenses:
            carbon = CarbonCalculator.get_carbon_level(expense.category)
            print(f"{expense} | Carbon: {carbon}")
        print(f"\n💰 Total Spent: ₹{self.user.get_total_spent()}")

    def generate_carbon_report(self):
        print(f"\n=== Carbon Footprint Report for {self.user.name} ===")
        if not self.user.expenses:
            print("❌ No expenses found!")
            return
        counts = CarbonCalculator.get_summary(self.user.expenses)
        print(f"🔴 High Impact:         {counts['High']} expenses")
        print(f"🟠 Medium-High Impact:  {counts['Medium-High']} expenses")
        print(f"🟡 Medium Impact:       {counts['Medium']} expenses")
        print(f"🟢 Low Impact:          {counts['Low']} expenses")

        total = len(self.user.expenses)
        high = counts["High"] + counts["Medium-High"]
        if total > 0:
            percentage = round((high / total) * 100)
            print(f"\n⚠️  {percentage}% of your expenses have Medium-High or High carbon impact!")
            if percentage >= 50:
                print("🌍 Tip: Try using public transport and reduce fuel usage!")
            else:
                print("✅ Great job! You have a relatively low carbon footprint!")

    def __str__(self):
        return f"📊 Report for {self.user.name}"