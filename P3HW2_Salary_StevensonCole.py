#StevensonCole
#4/23/2025
#P3HW2
#assess student understanding of decision structures

'''
1. **Initialize variables**:  
   - Set `total_overtime_pay` to 0  
   - Set `total_regular_pay` to 0  
   - Set `total_gross_pay` to 0  

2. **Start infinite loop**:  
   - Repeat the following steps until the loop is manually terminated.

3. **Get user input**:  
   - Prompt user for `employee_name`.  
   - Prompt user for `hours_worked`.  
   - Prompt user for `pay_rate`.

4. **Calculate pay**:  
   - **If `hours_worked` > 40**:  
     - Set `overtime_hours` to `hours_worked - 40`.  
     - Set `regular_pay` to `40 * pay_rate`.  
     - Set `overtime_pay` to `overtime_hours * (pay_rate * 1.5)`.  
   - **Else**:  
     - Set `overtime_hours` to 0.  
     - Set `regular_pay` to `hours_worked * pay_rate`.  
     - Set `overtime_pay` to 0.  
   - Set `gross_pay` to `regular_pay + overtime_pay`.

5. **Display employee details**:  
   - Print a separator line.  
   - Print employee name.  
   - Print formatted table showing `hours_worked`, `pay_rate`, `overtime_hours`, `overtime_pay`, `regular_pay`, and `gross_pay`.
'''

#create variables
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    #get employee name
    employee_name = input("Enter employee's name: ")

    #get hours worked and pay rate
    hours_worked = float(input(f"Enter number of hours worked: "))
    pay_rate = float(input(f"Enter employee's pay rate: "))

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

    #display employee details
    print('-------------------------------------')
    print(f"Employee name: {employee_name}")
    print("\nHours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<16}{pay_rate:<12}{overtime_hours:<12}{overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:<.2f}\n")

