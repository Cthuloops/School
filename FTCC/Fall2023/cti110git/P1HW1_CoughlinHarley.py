#ask user for an integer
user_num = int(input('Enter integer:\n'))

#performing operations on the entered int
num_squared = user_num * user_num
num_cubed = num_squared * user_num

#printing results of operations
print('You entered:', user_num)
print(user_num, 'squared is', num_squared)
print('And', user_num, 'cubed is', num_cubed,'!!')

#asking user for another int
user_num2 = int(input('Enter another integer:\n'))

#performing operations on new and old int
num_sum = user_num + user_num2
num_product = user_num * user_num2

#printing results of operations
print(user_num, '+', user_num2, 'is', num_sum)
print(user_num, '*', user_num2, 'is', num_product)