total = 0
count = 0

while True:
    user_input = (input("Please enter a number (or 'done' to quit): "))

    try:
        if user_input.lower() == "done":
            break

        for number in user_input:
            count = float(number) + 1 - 1
            total = total + float(user_input)
            avg = total / count

    except:
        print("Please check your input")
        continue

print(f"The Total:{total}\nThe Count:{count}\nThe Avg:{avg}")
















