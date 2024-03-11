# this program checks whether a year is a leap year and then returns the amount
# of days in February.
# 11/15/2023
# CTI-110 P5LAB - days in feb
# Harley Coughlin
#

def days_in_feb(user_year):
    if (user_year % 100 == 0):
        if (user_year % 400 == 0):
            return 29
        else:
            return 28
    elif (user_year % 4 == 0):
        return 29
    else:
        return 28

keep_going = 'y'
while keep_going != 'n':
    user_year = int(input("Enter a year: "))
    print(f"{user_year} has {days_in_feb(user_year)} days in February.")
    keep_going = input("Do you want to enter another year? (y or n)")
    continue
