try:
    score = float(input("Please input your score to receive your grade: "))

except:
    print("Invalid")
    exit()

if 0.9 <= score <= 1.0:
    grade = "A"

elif 0.8 <= score <= 0.9:
    grade = "B"

elif 0.7 <= score <= 0.8:
    grade = "C"

elif 0.6 <= score <= 0.7:
    grade = "D"

elif score < 0.6:
    grade = "F"

else:
    print("Invalid score!")


print(f"Your grade is {grade}")

