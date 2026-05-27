# Prompt user for the total amount received
total_amount = float(input("Enter the total amount received for the job: "))

# Split the amount evenly between you and two friends (3 people total)
split_amount = total_amount / 3

# Display the amount each person will receive formatted as currency
print(f"Each person will receive: ${split_amount:.2f}")
