# Prompt user for the stock ticker symbol
ticker = input("Enter the stock ticker symbol (e.g., MSFT):")

# Prompt user for the number of shares
shares = int(input("Enter the number of shares: "))

# Prompt user for the cost per share
cost_per_share = float(input("Enter the cost per share: "))

# Compute the total amount invested
amount_invested = shares * cost_per_share

# Display the result formatted to two decimal places for currency
print(f"Amount invested in {ticker.upper()}: ${amount_invested:.2f}")
