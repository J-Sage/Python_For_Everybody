# Initialize variables to keep track of the total, count, maximum, and minimum values
total = 0
count = 0
max_number = float('-inf')  # Initialize max_number with negative infinity
min_number = float('inf')   # Initialize min_number with positive infinity

# Continue prompting the user for input until they type "done"
while True:
    user_input = input("Please input a numerical number (or 'done' to finish): ")

    # Check if the user wants to exit the loop
    if user_input.lower() == "done":
        break

    try:
        # Convert the input to a float
        number = float(user_input)
        total += number
        count += 1

        # Update max_number and min_number if necessary
        max_number = max(max_number, number)
        min_number = min(min_number, number)

    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid numerical value.")

# Display the calculated results
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Max: {max_number}")
print(f"Min: {min_number}")
