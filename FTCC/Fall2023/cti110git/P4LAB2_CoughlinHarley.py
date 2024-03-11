num1 = int(input())
num2 = int(input())

if (num1 <= num2):
    while num1 <= num2:
        print(f'{num1}', end=' ')
        num1 += 5
    print()
elif (num1 > num2):
    print("Second integer can't be less than the first.")