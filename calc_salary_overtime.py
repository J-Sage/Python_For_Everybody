# Initialize a variable to control the loop
keep_going = "y"

# Start the loop
while keep_going == "y":
    # Get the input from the user
    try:
        hours = float(input("Please input the amount of hours worked: "))
        rate = float(input("Please input your pay rate: "))
    except:
        print("Error: Please ensure that your values are correct")
        # Exit the loop if the input is invalid
        break

    # Calculate the pay based on the hours and rate
    if hours <= 40:
        gross_salary = (hours * rate)
        print(f"Your salary is {gross_salary}RMB")
    elif hours > 40:
        overtime = float(hours - 40)
        over_time_comp = (rate * 1.5) * overtime
        gross_salary = (hours - overtime) * rate + over_time_comp
        print(f"Your salary is {gross_salary}RMB")


    # Ask the user if they want to continue
    keep_going = input("Do you want to continue? (y/n): ")

# End the loop
print("Thank you for using this program.")


