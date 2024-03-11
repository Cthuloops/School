#this program determines cost of driving based on a car's mpg and the price of gase per gallon

#asking user for input
mpg = float(input('What is your car\'s gas mileage? '))

gas_price = float(input('What is the cost of a gallon of gas? '))

#performing calculations for 20, 75, and 500 miles
miles_20 = (20 / mpg) * gas_price
miles_75 = (75 / mpg) * gas_price
miles_500 = (500 / mpg) * gas_price

#displaying results
print(f'{miles_20:.2f} {miles_75:.2f} {miles_500:.2f}')