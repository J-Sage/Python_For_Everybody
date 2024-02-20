# Ask the user for their name and surname
name = input("Please enter your name: ")
sur_name = input("Please input your surname: ")

# Print a welcome message with their name and surname
print(f"Welcome {name} {sur_name}")

# Ask the user if they want to calculate their gross salary
ans = input("Would you like to calculate your gross salary")

# If the user answers yes or y, in any case
if ans.upper() in ["YES", "Y"]:
    # Try to get the hours and rate from the user and calculate the gross pay
    try:
        # Ask the user for the amount of hours worked
        hours = input("Please enter the amount of hours: ")
        # Ask the user for the hourly rate
        rate = input("Please input your hourly rate: ")
        # Convert the hours and rate to floats and multiply them
        gross_pay = float(hours) * float(rate)
        # Print the gross pay rounded to the nearest integer
        print(f"Your gross pay is {round(gross_pay)}")
    # If there is an error in the input or conversion, print a message
    except:
        print("Please check that you have entered the correct values")
# If the user answers anything else, print a thank you message
else:
    print("Thank you")
