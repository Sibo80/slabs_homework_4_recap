"""This program calculates transaction averages."""

import data_utils
import random
import datetime


def main():
    """Generate transactions and display their average."""

    transactions = []

    for number in range(5):
        amount = random.randint(50, 500)
        transactions.append(amount)

    today = datetime.date.today()

    average_value = data_utils.calculate_average(transactions)

    formatted_average = data_utils.format_currency(average_value)

    print("Date:", today)
    print("Transactions:", transactions)
    print("Average:", formatted_average)


if __name__ == "__main__":
    main()
