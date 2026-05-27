# Prompt user for the student's last name
last_name = input("Enter the student's last name: ")

# Prompt user for the midterm score
midterm = float(input("Enter the midterm score (0-100): "))

# Prompt user for the final exam score
final_exam = float(input("Enter the final exam score (0-100): "))

# Compute total exam points (40% of midterm + 60% of final)
total_points = (midterm * 0.40) + (final_exam * 0.60)

# Display student last name and total exam points formatted to 2 decimal places
print(f"Student Last Name: {last_name}")
print(f"Total Exam Points: {total_points:.2f}")