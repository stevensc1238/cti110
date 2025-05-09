#StevensonCole
#5/2/2025
#P5LAB
#program will simulate a customer using a self-checkout machine using user-defined functions

import random

def disperse_change(change):
    
    #converting value to an integer
    change = round(change * 100)

    #determine how many coins are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    if num_dollars > 0:
        if num_dollars == 1:
            print(f'{num_dollars} Dollar')
        else:
            print(f'{num_dollars} Dollars')

    if num_quarters > 0:
        if num_quarters == 1:
            print(f'{num_quarters} Quarter')
        else:
            print(f'{num_quarters} Quarters')

    if num_dimes > 0:
        if num_dimes == 1:
            print(f'{num_dimes} Dime')
        else:
            print(f'{num_dimes} Dimes')

    if num_nickels > 0:
        if num_nickels == 1:
            print(f'{num_nickels} Nickel')
        else:
            print(f'{num_nickels} Nickels')

    if num_pennies > 0:
        if num_pennies == 1:
            print(f'{num_pennies} Penny')
        else:
            print(f'{num_pennies} Pennies')

def main():
    #logic goes here

    #generate amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f'You owe ${amount_owed:.2f}')

    #create variable to rep money put in machine
    money_in = float(input('How much cash will you put in the self-checkout? '))

    #calculate change owed to customer
    change = money_in - amount_owed
    print(f'Change is: ${change:.2f}\n')

    #call the disperse_change function
    disperse_change(change)
    

#call the main function
main()
