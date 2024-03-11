#CTI-110
#P3HW2 - Salary
#Harley Coughlin
#10/21/23

#ask for employee name
#ask for number of hours
#ask for pay rate
#calculate overtime, ot/regular pay, and gross pay
#display results

#ask for name, hours, pay rate
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#calculating overtime hours/ot pay rate
overtime_hours = hours_worked - 40
overtime_pay_rate = pay_rate * 1.5

#calculating overtime pay and regular pay
overtime_pay = overtime_hours * overtime_pay_rate
regular_pay = (hours_worked - overtime_hours) * pay_rate
gross_pay = (overtime_pay + regular_pay)

#separating prompts from results
print("----------------------------------")
print(f"Employee name:      {employee_name}\n")
print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<16.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:.2f}")