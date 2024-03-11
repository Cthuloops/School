is_leap_year = False
   
input_year = int(input('Enter a 4 digit year: '))

#% 100 to check if turn of century
if input_year % 100 == 0:
    if input_year % 400 == 0:
        is_leap_year = True
#if it's not turn of century normal check to see if leap or not
elif input_year % 4 == 0:
    is_leap_year = True

if is_leap_year == True:
    print(f'{input_year} - leap year')
else:
    print(f'{input_year} - not a leap year')