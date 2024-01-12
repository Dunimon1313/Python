#Zachary Taylor
#COP2500C
#Assignment #3: Problem B: Icons.py
#Date: 7/5/2022

#import necessary libraries
import turtle

#initialize drawing object
t = turtle.Turtle()

#positions pen for start of drawing
t.penup()
t.setpos(0, 0)
t.pendown()

#draws flower with edges' color based on evens and odds
for i in range(36):
    t.forward(150)
    t.right(170)
    if i % 2 == 1:
        t.pencolor("blue")
    else:
        t.pencolor("red")

#resets loop variable
i = 0

#positions pen for start of next figure
t.penup()
t.setpos(35, 63)
t.pendown()

#draws hexagon with colors based on evens and odds
for i in range(6):
    t.pensize(10)
    t.forward(80)
    t.right(60)
    if i % 2 == 1:
        t.pencolor("green")
    else:
        t.pencolor("orange")
