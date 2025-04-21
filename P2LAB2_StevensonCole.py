#StevensonCole
#4/10/2025
#P2LAB2
#Write a program that creates a dictionary

cars = {'Camaro' :18.21, 'Prius' :52.36, 'Model S' :110, 'Siverado' :26}

#Get keys
keys = cars.keys()

print(keys)

#Get user input
car_name = input('Enter a vehicle to see its MPG:')

#Get mpg for car
car_mpg = cars[car_name]
print(f'The {car_name} gets {car_mpg} mpg.')

#Get miles from user
miles_driven = float(input(f'How many miles will you drive the {car_name}?'))

#Calculate
gals_needed = miles_driven/car_mpg

#Display results
print(f'{gals_needed:.2f} gallon(s) of gas are needed to drive the {car_name}{miles_driven: .1f} miles')
