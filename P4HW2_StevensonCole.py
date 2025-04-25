#StevensonCole
#4/25/2025
#P4HW2
#create program that will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

'''
BEGIN Payroll Calculator Program

INITIALIZE total_overtime_pay, total_regular_pay, total_gross_pay to 0
INITIALIZE employee_count to 0

PRINT "Welcome to the Payroll Calculator!"

WHILE True
    INPUT employee_name
    IF employee_name IS "Done"
        BREAK the loop

    INPUT hours_worked
    INPUT pay_rate

    IF hours_worked > 40
        SET overtime_hours = hours_worked - 40
        SET regular_pay = 40 * pay_rate
        SET overtime_pay = overtime_hours * (pay_rate * 1.5)
    ELSE
        SET overtime_hours = 0
        SET regular_pay = hours_worked * pay_rate
        SET overtime_pay = 0
    END IF

    SET gross_pay = regular_pay + overtime_pay

    PRINT employee_name, hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay

    INCREMENT total_overtime_pay by overtime_pay
    INCREMENT total_regular_pay by regular_pay
    INCREMENT total_gross_pay by gross_pay
    INCREMENT employee_count by 1
END WHILE

PRINT "Summary of Payroll Calculations"
PRINT total_overtime_pay, total_regular_pay, total_gross_pay, employee_count

END Program
'''

#create variables
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    #get employee name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break  #exit loop when user inputs 'Done'

    #get hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    #calculate pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0

    gross_pay = regular_pay + overtime_pay

    #display individual employee details
    print(f"\nEmployee name: {employee_name}")
    print("\nHours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<16}{pay_rate:<12}{overtime_hours:<12}{overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:<.2f}\n")

    #update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

#display summary
print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
