try:
    # Get user input for hours worked and hourly rate
    hours = float(input("Please enter the amount of hours worked: "))
    rate = float(input("Please enter your hourly rate: "))

    # Define functions to compute salary
    def compu_rate(h, r):
        return h * r

    def compute_overtime(h, r):
        overtime = max(0, h - 40)  # Calculate overtime hours
        over_time_comp = (rate * 1.5) * overtime
        overtime_pay = (h - overtime) * rate + over_time_comp
        return overtime_pay

    # Determine whether to calculate regular or overtime pay
    if hours <= 40:
        total_salary = compu_rate(hours, rate)
    else:
        total_salary = compute_overtime(hours, rate)

    # Print the calculated salary
    print(f"Your total salary is {total_salary} RMB")

except ValueError:
    print("Please check that you have inputted the correct numeric values and try again.")