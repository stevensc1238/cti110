#StevensonCole
#4/25/025
#P4LAB2
#write code that displays information to users using loops


'''
Get integer from user
Determine if integer is positive or negative
If number is positive, display multification table
If number is negative, tell user program can't accept it
If yes, rerun program
If no, end program
'''

run_again = 'yes'

while run_again != 'no':

    user_num = int(input('\nEnter an integer: '))

    if user_num >= 0:
        #display multiplication for input value and range (1-12)
        for item in range(1, 13):
            print(f'{user_num} * {item} = {user_num * item}')
    else:
        print('\nThis program does not handle negative numbers.')

    run_again = input('\nWould you like to run the program again? ')

#loop has broken. User entered 'no'
print('\nExiting program...')
