"""
CodeAlpha - Python Programming Task 2
Project: Stock Portfolio Tracker

Description:
Calculates the total investment value using a predefined stock-price
dictionary and quantities entered by the user.
"""

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 175.00,
    "MSFT": 420.00,
    "AMZN": 190.00
}


def display_available_stocks():
    print("\nAvailable Stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f}")


def track_portfolio():
    portfolio = {}
    total_investment = 0.0

    print("=" * 50)
    print("       STOCK PORTFOLIO TRACKER - CODEALPHA")
    print("=" * 50)

    display_available_stocks()

    print("\nEnter stock details. Type 'done' when finished.\n")

    while True:
        stock = input("Enter stock symbol: ").strip().upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not available. Please choose from the listed symbols.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.\n")
                continue

        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        investment = STOCK_PRICES[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += investment

        print(f"Added {quantity} shares of {stock}.")
        print(f"Investment value: ${investment:,.2f}\n")

    print("\n" + "=" * 50)
    print("             PORTFOLIO SUMMARY")
    print("=" * 50)

    if not portfolio:
        print("No stocks were added.")
        return

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Value':<15}")
    print("-" * 49)

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        print(f"{stock:<10}{quantity:<12}${price:<11.2f}${value:<14.2f}")

    print("-" * 49)
    print(f"Total Investment Value: ${total_investment:,.2f}")

    save = input("\nSave portfolio summary to a text file? (y/n): ").strip().lower()

    if save == "y":
        with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
            file.write("CODEALPHA - STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 45 + "\n")

            for stock, quantity in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * quantity
                file.write(
                    f"{stock}: {quantity} shares x ${price:.2f} = "
                    f"${value:.2f}\n"
                )

            file.write("=" * 45 + "\n")
            file.write(f"Total Investment: ${total_investment:.2f}\n")

        print("Portfolio saved as 'portfolio_summary.txt'.")


if __name__ == "__main__":
    track_portfolio()
