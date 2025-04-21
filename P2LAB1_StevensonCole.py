#StevensonCole
#4/10/2025
#P2LAB1
#Write a program that will calculate the diameter, circumference, and area of a circle, given the radius via user input
import math

#Get radius from user
radius = float(input('What is the radius of the circle?: '))

#calculate circ, diameter and area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display results
print(f'The diameter of the circle is {diam: .1f}')
print(f'The circumference of the circle is {cir: .2f}')
print(f'The area of the circle is {area: .3f}')
