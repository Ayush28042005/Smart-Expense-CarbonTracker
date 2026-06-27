# 💰 Smart Expense + Carbon Footprint Tracker

A Python-based command-line application that helps users track their daily expenses while also calculating the carbon footprint of each expense based on its category.

---

## ✨ Features

- Add multiple users
- Switch between users
- Add expenses with category (fuel, transport, food, electricity, shopping, other)
- Auto carbon footprint calculation per expense
- View detailed expense report with carbon levels
- View full carbon footprint summary with smart tips
- Auto timestamp on every expense
- Persistent storage using JSON

---

## 🌍 Carbon Footprint Categories

| Category | Carbon Level |
|---|---|
| Fuel | 🔴 High |
| Electricity | 🔴 High |
| Shopping | 🟠 Medium-High |
| Food | 🟡 Medium |
| Transport | 🟡 Medium |
| Other | 🟢 Low |

---

## 🧠 OOP Concepts Used

| Concept | Where Used |
|---|---|
| Classes & Objects | Expense, User, CarbonCalculator, Report, Tracker |
| Constructors | Every class uses `__init__` |
| Encapsulation | Data stored inside class attributes |
| Composition | User contains Expense objects |
| Abstraction | Tracker hides all logic and file handling |
| Static Methods | CarbonCalculator uses `@staticmethod` |
| Class Methods | `from_dict()` used in all classes |

---

## 📁 Project Structure

```
Smart-Expense-Carbon-Tracker/
│
├── expense.py              → Expense class
├── carbon_calculator.py    → CarbonCalculator class
├── user.py                 → User class
├── report.py               → Report class
├── tracker.py              → Main Tracker class
├── main.py                 → Entry point and menu
└── data.json               → Persistent JSON storage
```

---

## 🚀 How To Run

```bash
python main.py
```

No external libraries required. Just Python 3.x!

---

## 👨‍💻 Author

**Ayush Saini**
B.Tech CSE-AIML | 3rd Year
