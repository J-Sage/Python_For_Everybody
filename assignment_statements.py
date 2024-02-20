# This program asks the user for the width and height of a rectangle
# and prints the type of some expressions involving them

# Ask the user for the width and convert it to a float
rectangle_width = float(input("Please input the width: "))

# Ask the user for the height and convert it to a float
rectangle_height = float(input("Please input the height: "))

# Print the type of the expression rectangle_width // 2
print(type((rectangle_width // 2)))

# Print the type of the expression rectangle_width / 2.0
print(type((rectangle_width / 2.0)))

# Print the type of the expression rectangle_height / 3
print(type((rectangle_height / 3)))

# Print the type of the expression 1 + 2 * 5
print(type((1 + 2 * 5)))
