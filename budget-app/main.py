class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        balance = 0

        for item in self.ledger:
            balance += item["amount"]

        return balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")

        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        result = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]

            result += f"{description:<23}{amount:>7.2f}\n"

        result += f"Total: {self.get_balance():.2f}"

        return result


def create_spend_chart(categories):
    spending = []

    for category in categories:
        total = 0

        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])

        spending.append(total)

    total_spent = sum(spending)
    percentages = []

    for amount in spending:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int(amount / total_spent * 100)

        percentages.append((percentage // 10) * 10)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:3}| "

        for percentage in percentages:
            if percentage >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    chart += "    " + "---" * len(categories) + "-\n"

    longest_name = max(
        (len(category.name) for category in categories),
        default=0
    )

    for position in range(longest_name):
        chart += "     "

        for category in categories:
            if position < len(category.name):
                chart += category.name[position] + "  "
            else:
                chart += "   "

        if position < longest_name - 1:
            chart += "\n"

    return chart
