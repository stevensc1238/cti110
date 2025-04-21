#StevensonCole
#4/11/2025
#P2HW2
#---------------------------------------------
#Pseudocode:
#1. Ask the user to enter six test grades, one for each module.
#2. Store these grades in a list called 'grades'.
#3. Use built-in functions to find:
#    - the lowest grade
#    - the highest grade
#    - the sum of grades
#    - the average (sum divided by number of grades)
#4. Display the results in a formatted output that matches the given example.
#---------------------------------------------

#Step 1 & 2: Input grades and store in a list
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

grades = [grade1, grade2, grade3, grade4, grade5, grade6]

#Step 3: Perform calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

#Step 4: Display results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest}")
print(f"{'Highest Grade:':<20}{highest}")
print(f"{'Sum of Grades:':<20}{total}")
print(f"{'Average:':<20}{average:.2f}")
print("---------------------------------------")
