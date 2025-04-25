#StevensonCole
#04/25/2025
#P4LAB1a
#Using turtle graphics, and either a while or for loop, write a program that draws a square and a triangle

#import library
import turtle

#create the turtle windoe and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#set turtle options
pen.pensize(4)
pen.pencolor('green')
pen. shape('arrow')

#code to draw shapes
for side in range(4):
    pen.forward(200)
    pen.left(90)

#while loop 3x execute
sides = 3

while sides > 0:
    pen.forward(200)
    pen.left(120)
    sides = sides - 1

#wait for user to close window
win.mainloop()
