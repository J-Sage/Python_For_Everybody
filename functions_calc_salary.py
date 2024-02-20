try:
    hours = float(input("Please enter the amount of hours worked: "))
    rate = float(input("Please enter your hourly rate: "))

    def compu_rate(h,r):
        salary_calc = h * r
        return salary_calc

    def compute_overtime(h,r):
        overtime = float(hours - 40)
        over_time_comp = (rate * 1.5) * overtime
        overtime_pay = (hours - overtime) * rate + over_time_comp
        return  overtime_pay

except:
    print("Please check that you have inputted the correct values and try again")

if hours <= 40:
    total_salary = compu_rate(hours,rate)
    print(total_salary)

elif hours > 40:
    total_salary = compute_overtime(hours,rate)
    print(total_salary)


