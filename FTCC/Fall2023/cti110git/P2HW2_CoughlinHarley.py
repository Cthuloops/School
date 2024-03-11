#CTI-110
#P2HW2 - List
#Harley Coughlin
#10/07/2023

#ask user for grades for tests
#create list from grades
#display lowest grade, highest grade, sum of grades, and grade average

#userprompts
module_1_test = float(input('Enter grade for Module 1: '))
module_2_test = float(input('Enter grade for Module 2: '))
module_3_test = float(input('Enter grade for Module 3: '))
module_4_test = float(input('Enter grade for Module 4: '))
module_5_test = float(input('Enter grade for Module 5: '))
module_6_test = float(input('Enter grade for Module 6: '))

#creating list from score entries
test_grades_list = [module_1_test, module_2_test, module_3_test, module_4_test, module_5_test, module_6_test]

#displaying lowest grade, highest grade, sum of grades, and grade average
print('------------Results------------')
print(f'Lowest Grade:       {min(test_grades_list):.1f}')
print(f'Highest Grade:      {max(test_grades_list):.1f}')
print(f'Sum of Grades:      {sum(test_grades_list):.1f}')
print(f'Average:            {sum(test_grades_list) / len(test_grades_list):.2f}')
print('-------------------------------')

