class CarbonCalculator:
    
    CARBON_LEVELS = {
        "fuel":         ("High",        "🔴"),
        "electricity":  ("High",        "🔴"),
        "shopping":     ("Medium-High",  "🟠"),
        "food":         ("Medium",      "🟡"),
        "transport":    ("Medium",      "🟡"),
        "other":        ("Low",         "🟢")
    }

    @staticmethod
    def get_carbon_level(category):
        category = category.lower()
        if category in CarbonCalculator.CARBON_LEVELS:
            level, emoji = CarbonCalculator.CARBON_LEVELS[category]
            return f"{emoji} {level}"
        return "🟢 Low"

    @staticmethod
    def get_summary(expenses):
        counts = {"High": 0, "Medium-High": 0, "Medium": 0, "Low": 0}
        for expense in expenses:
            level, _ = CarbonCalculator.CARBON_LEVELS.get(
                expense.category, ("Low", "🟢")
            )
            counts[level] += 1
        return counts