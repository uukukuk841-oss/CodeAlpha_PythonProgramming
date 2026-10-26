import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
    "AMZN": 190.00,
}


def get_positive_quantity():
    """Ask for a whole-number quantity greater than zero."""
    while True:
        value = input("Enter quantity: ").strip()
        try:
            quantity = int(value)
            if quantity > 0:
                return quantity
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def save_report(holdings, total_value):
    """Save the portfolio details to a CSV file."""
    filename = "portfolio_report.csv"

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock Symbol", "Price per Share", "Quantity", "Investment Value"])

        for symbol, quantity in holdings.items():
            price = STOCK_PRICES[symbol]
            writer.writerow([symbol, f"{price:.2f}", quantity, f"{price * quantity:.2f}"])

        writer.writerow([])
        writer.writerow(["Total Portfolio Value", "", "", f"{total_value:.2f}"])

    print(f"\nReport saved successfully as '{filename}'.")


def main():
    holdings = {}

    print("=" * 48)
    print("             STOCK PORTFOLIO TRACKER")
    print("=" * 48)
    print("Sample stock prices (USD per share):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f}")

    print("\nEnter the stocks you own.")
    print("Type DONE when you have finished.\n")

    while True:
        symbol = input("Stock symbol: ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Stock not found in the sample list. Please choose a listed symbol.")
            continue

        quantity = get_positive_quantity()
        holdings[symbol] = holdings.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    if not holdings:
        print("\nNo stocks were entered. Nothing to calculate.")
        return

    print("\n" + "-" * 58)
    print(f"{'SYMBOL':<12}{'PRICE':>12}{'QUANTITY':>12}{'VALUE':>16}")
    print("-" * 58)

    total_value = 0.0
    for symbol, quantity in holdings.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_value += value
        print(f"{symbol:<12}${price:>10.2f}{quantity:>12}${value:>14.2f}")

    print("-" * 58)
    print(f"{'TOTAL INVESTMENT':<36}${total_value:>14.2f}")

    save_choice = input("\nSave this report as CSV? (y/n): ").strip().lower()
    if save_choice == "y":
        save_report(holdings, total_value)
    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
