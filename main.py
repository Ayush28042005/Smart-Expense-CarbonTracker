from tracker import Tracker

def main():
    tracker = Tracker()

    VALID_CATEGORIES = ["fuel", "transport", "food", "electricity", "shopping", "other"]

    while True:
        print("\n=== Smart Expense + Carbon Footprint Tracker ===")
        if tracker.current_user:
            print(f"    Active User: 👤 {tracker.current_user.name}")
        print("1. Add User")
        print("2. Select User")
        print("3. Add Expense")
        print("4. View My Expenses")
        print("5. View Carbon Footprint Report")
        print("6. View All Users")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            name = input("Enter user name: ").strip()
            tracker.add_user(name)

        elif choice == "2":
            name = input("Enter user name to select: ").strip()
            tracker.select_user(name)

        elif choice == "3":
            if not tracker.current_user:
                print("❌ Please select a user first!")
                continue
            description = input("Enter expense description: ").strip()
            try:
                amount = float(input("Enter amount (₹): ").strip())
            except ValueError:
                print("❌ Invalid amount! Please enter a number.")
                continue
            print(f"Categories: {', '.join(VALID_CATEGORIES)}")
            category = input("Enter category: ").strip().lower()
            if category not in VALID_CATEGORIES:
                print(f"❌ Invalid category! Choose from: {', '.join(VALID_CATEGORIES)}")
                continue
            tracker.add_expense(description, amount, category)

        elif choice == "4":
            tracker.view_expenses()

        elif choice == "5":
            tracker.view_carbon_report()

        elif choice == "6":
            tracker.view_all_users()

        elif choice == "7":
            print("👋 Goodbye! Keep tracking your carbon footprint! 🌍")
            break

        else:
            print("❌ Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()