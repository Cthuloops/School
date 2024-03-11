#This program calculates and displays travel expenses (nicely aligned)
#10/07/2023
#CTI-110 P2HW1 - Travel
#Harley Coughlin

#Display program description
#ask user to enter their budget
#ask user to enter travel destination
#ask user for amount they will spend on gas
#ask user for amount they will spend on accomadation
#ask user for amount they will spend on food
#add expenses
#subtract expenses from budget
#display results (nicely formatted)

#displaying program description
print('This program calculates and displays travel expenses.')

#user prompts
trip_budget = int(input('Enter Budget: '))
travel_destination = input('Enter your travel destination: ')
amount_gas = int(input('How much do you think you will spend on gas? '))
amount_accomadation = int(input('Approximately, how much will you need for accomodation/hotel? '))
amount_food = int(input('Last, how much do you need for food? '))

#adding expenses together
expenses = amount_gas + amount_accomadation + amount_food

#subtracting expenses from budget
balance = trip_budget - expenses

#displaying results
print('------------Travel Expenses------------')
print(f'Location:           {travel_destination}')
print(f'Initial Budget:     ${trip_budget:.1f}')
print(f'Fuel:               ${amount_gas:.1f}')
print(f'Accomodation:       ${amount_accomadation:.1f}')
print(f'Food:               ${amount_food:.1f}')
print('---------------------------------------\n')
print(f'Remaining Balance:  ${balance:.1f}')