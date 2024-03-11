#CTI-110
#P4HW2 - Salary Calculator
#Harley Coughlin
#11/07/2023
#



#keeping totals of employee amount, OT pay, regular pay, gross amount
total_employees = 0
overtime_paid = 0.0
regular_paid = 0.0
total_gross = 0.0

while True:
    #prompts for employee info
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    #setting escape
    if employee_name == 'Done':
       break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    print()
    
    #calc OT hours and pay rate
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay_rate = pay_rate * 1.5
    else:
        overtime_hours = 0
        overtime_pay_rate = 0

    #calc ot and regular pay
    overtime_pay = overtime_hours * overtime_pay_rate
    regular_pay = (hours_worked - overtime_hours) * pay_rate
    gross_pay = overtime_pay + regular_pay
    
    #add to totals
    total_employees += 1
    overtime_paid += overtime_pay
    regular_paid += regular_pay
    total_gross += gross_pay

    #print results
    print(f"Employee name:      {employee_name}\n")
    print("Hours Worked     Pay Rate    OverTime    OverTime Pay    RegHour Pay     Gross Pay")
    print("----------------------------------------------------------------------------------")
    print(f"{hours_worked:<16.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:.2f}\n")

#printing totals
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${overtime_paid:.2f}")
print(f"Total amount paid for regular hours: ${regular_paid:.2f}")
print(f"Total amount pain in gross: ${total_gross:.2f}")
