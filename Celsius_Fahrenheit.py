# Use int() to get the user's choice as a number
try:
    user_choice = int(input("Please press (1) to convert Celsius to Fahrenheit or press to (2) to convert Fahrenheit to Celsius: "))
except:
    print("Please enter a valid choice and try again")
    # Exit the program if the input is invalid
    exit()

# Use == to compare the user's choice with numbers
if user_choice == 1:
    # Use float() to get the Celsius value as a number
    try:
        celsius_value = float(input("Please input your Celsius value: "))
    except:
        print("Please enter a valid temperature and try again")
        # Exit the program if the input is invalid
        exit()
    # Use the formula to convert Celsius to Fahrenheit
    fehrenheit_value = (celsius_value * 1.8) + 32
    # Use f-strings to format the output
    print(f"{celsius_value}°C converted is {fehrenheit_value}°F")

# Use elif to check the second option
elif user_choice == 2:
    # Use float() to get the Fahrenheit value as a number
    try:
        fehrenheit_value = float(input("Please input your Fehrenheit value: "))
    except:
        print("Please enter a valid temperature and try again")
        # Exit the program if the input is invalid
        exit()
    # Use the formula to convert Fahrenheit to Celsius
    celsius_value = (fehrenheit_value - 32) * (5/9)
    # Use f-strings to format the output
    print(f"{fehrenheit_value}°F converted is {celsius_value}°C")

# Use else to handle any other input
else:
    print("Exiting")

