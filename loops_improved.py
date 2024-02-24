# Initialize variables to keep track of the total sum and count of numbers
total = 0
count = 0

# Create an infinite loop using 'while True'
while True:
    # Prompt the user to input a number (or type 'done' to quit)
    user_input = input("Please enter a number (or 'done' to quit): ")

    # Check if the user wants to exit the loop
    if user_input.lower() == "done":
        break  # Exit the loop if 'done' is entered

    try:
        # Convert the user input to a float (assuming it's a valid number)
        number = float(user_input)
        total += number  # Add the number to the total
        count += 1  # Increment the count of valid numbers
    except ValueError:
        # Handle the case where the input cannot be converted to a float
        print("Please check your input (enter a valid number)")

# Calculate the average (if valid numbers were entered)
if count > 0:
    avg = total / count
    print(f"The Total: {total}\nThe Count: {count}\nThe Avg: {avg:.2f}")
else:
    print("No valid numbers entered.")
