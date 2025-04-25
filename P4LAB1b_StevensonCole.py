#StevensonCole
#04/25/2025
#P4LAB1b
#using turtle graphics, write program that displays initials

#import library
import turtle

#create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#Setup turtle options
pen.pensize(4)
pen.pencolor('green')
pen. shape('arrow')
pen.speed(2)

#code and draw horizontal base line
pen.penup()
pen.goto(-200, -100)
pen.setheading(0)
pen.pendown()
pen.forward(250)

#reset pen location
pen.penup()
pen.goto(-100, -80)

#code and draw block 'C'
pen.pendown()
for side in range(3):
    pen.backward(100)
    pen.right(90)

#reset pen location  
pen.penup()
pen.goto(-50, -80)
pen.right(90)

#code and draw block 'S'
pen.pendown()
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.penup()

#wait for user to close window
win.mainloop()
