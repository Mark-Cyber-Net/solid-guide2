# Prompt user for the first exam score
exam1 = float(input("Enter the first exam score: "))

# Prompt user for the second exam score
exam2 = float(input("Enter the second exam score: "))

# Calculate the weighted total score
total_score = (exam1 * 0.60) + (exam2 * 0.40)

# Display the formatted total score
print(f"The total score is: {total_score:.2f}")