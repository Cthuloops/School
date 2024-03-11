#CTI-110
#P4HW1 - Score List
#Harley Coughlin
#11/05/2023
#

#asking user for amount of scores to enter
scores_amount = int(input("How many scores do you want to enter? "))

#loop for collecting scores
collected_scores = []
valid_score = True
score_number = 0
while score_number < scores_amount:
    #checking if score is being reentered
    if (valid_score):
        score = int(input(f"Enter score #{len(collected_scores) + 1}: "))
    else:
        score = int(input(f"Enter score #{len(collected_scores) + 1} again: "))
    #checking to see if the score is between 0 and 100
    if score in range(101):
        collected_scores.append(score)
        valid_score = True
        score_number += 1
    else:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        valid_score = False
        continue

#printing the results
print("----------------Results----------------")
print(f"Lowest Score   : {min(collected_scores):.1f}")

#removing the lowest score
collected_scores.remove(min(collected_scores))

print(f"Modified List  : {collected_scores}")

#averaging scores
score_sum = sum(collected_scores)
score_average = score_sum / len(collected_scores)

#displaying score average
print(f"Scores Average : {score_average:.2f}")

#letter grade
if score_average >= 90:
    letter_grade = 'A'
elif score_average >= 80:
    letter_grade = 'B'
elif score_average >= 70:
    letter_grade = 'C'
elif score_average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Grade          : {letter_grade}")
print("---------------------------------------")
