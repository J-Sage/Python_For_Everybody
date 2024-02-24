total = 0
count = 0
max_number = None
min_number = None

while True:
    user_input = input("Please input a numerical number: ")

    if user_input.lower() == "done":
        break

    try:
        number = float(user_input)
        total += number
        count += 1

        if max_number is None or max_number < number:
            max_number = number

        if min_number is None or min_number > number:
            min_number = number

    except ValueError:
        print("Bad value: Please check your value and try again")

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Max: {max_number}")
print(f"Min: {min_number}")