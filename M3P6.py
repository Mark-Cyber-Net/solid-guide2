# Prompt user for the purchase price per share
purchase_price = float(input("Enter the purchase price per share: "))

# Prompt user for the current stock price
current_price = float(input("Enter the current stock price: "))

# Prompt user for the quantity of stock
quantity = int(input("Enter the quantity of stock: "))

# Compute the value increase or decrease using the given formula
value_change = (current_price - purchase_price) * quantity

# Display the result formatted to two decimal places
if value_change >= 0:
    print(f"Value increase: ${value_change:.2f}")
else:
    print (f"Value decrease: ${abs(value_change):.2f} (You are losing money)")
