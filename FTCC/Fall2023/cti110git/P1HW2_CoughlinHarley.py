#This is a program the calculates and displays travel expenses
#Today is 09/28/2023
#CTI-110 P1HW2 Travel Expense
#Harley Coughlin
#Following is the pseudocode for the program
#Display program description
#ask user to enter their budget
#ask user to enter travel destination
#ask user for amount they will spend on gas
#ask user for amount they will spend on accomadation
#ask user for amount they will spend on food
#add expenses
#subtract expenses from budget
#display results

#displaying program description
print('This program calculates and displays travel expenses')

#asking user for budget
trip_budget = int(input('Enter Budget: '))

#asking user for destination
travel_destination = input('Enter your travel destination: ')

#asking user for gas amount
amount_gas = int(input('How much do you think you will spend on gas? '))

#asking user for amount spent on accomadation
amount_accomadation = int(input('Approximately, how much will you need for accomodation/hotel? '))

#asking user for amount spent on food
amount_food = int(input('Last, how much do you need for food? '))

#adding expenses together
expenses = amount_gas + amount_accomadation + amount_food

#subtracting expenses from budget
balance = trip_budget - expenses

#displaying results
print('------------Travel Expenses------------')

#display location and budget
print('Location:', travel_destination, '\nInitial Budget:', trip_budget, '\n')

#display expenses
print('Fuel:', amount_gas, '\nAccomodation:', amount_accomadation, '\nFood:', amount_food, '\n')

#display remaining budget
print('Remaining Balance:', balance)