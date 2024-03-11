#this program takes 4 numbers and prints formatted versions of the product and average

#asking user for input
num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
num3 = float(input('Enter num3: '))
num4 = float(input('Enter num4: '))

#printing product and average as ints
print(f'{(num1 * num2 * num3 * num4):.0f} {(num1 + num2 + num3 + num4) / 4:.0f}')

#printing product and average as floats to 3 points
print(f'{(num1 * num2 * num3 * num4):.3f} {(num1 + num2 + num3 + num4) / 4:.3f}')