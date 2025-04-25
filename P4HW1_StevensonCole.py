#StevensonCole
#04/24/2025
#P4HW1
#Write a program using a loop

"""
Program: Grade Calculator with Score Drop

Pseudocode:
1. Prompt the user for the number of scores they want to enter.
2. Initialize an empty list to store the scores.
3. Loop from 1 to the number of scores:
    a. Prompt the user to enter a score.
    b. Validate that the score is between 0 and 100.
       - If not, display an error and prompt again until valid.
    c. Append the valid score to the list.
4. After collecting all scores:
    a. Find the lowest score in the list.
    b. Make a copy of the list and remove the lowest score from the copy.
5. Calculate the average of the modified list (excluding the lowest score).
6. Determine the letter grade based on the average:
    - A for 90 and above
    - B for 80-89
    - C for 70-79
    - D for 60-69
    - F for below 60
7. Display the following:
    - Lowest score dropped
    - Modified list
    - Average score (rounded to 2 decimal places)
    - Final letter grade
8. Format output for correct spacing and align : under the 'R' in "Results"
"""

score_num = int(input('How many scores do you want to enter? '))
print()

#Empty list
scores = []

for num in range(1, score_num  + 1):
    #collect scores
    score = float(input('Enter score #' + str(num)+ ': '))
    #Eval entry
    while score < 0 or score > 100:
        print('\nINVALID SCORE ENTERED!!!!')
        print('Score should be between 0 and 100')
        score = float(input('Enter score #' + str(num) +' again: '))

    scores.append(score)
    #Find lowest score and remove

lowest = min(scores)
scores_mod = scores.copy()
#drop lowest
scores_mod.remove(lowest)
#calc avg
avg = sum(scores_mod)/ len(scores_mod)

#determine letter grade
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"\n--------------Results--------------")
print(f"{'Lowest Score' .ljust(14)}: {lowest}")
print(f"{'Modified List' .ljust(14)}: {scores_mod}")
print(f"{'Scores Average' .ljust(14)}: {avg:.2f}")
print(f"{'Grade' .ljust(14)}: {grade}")
print(f"-----------------------------------")
