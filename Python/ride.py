#Zachary Taylor
#COP2500C
#Assignment #1: Problem B: Knightro's Vehicles
#Date: 7/5/2022

import turtle

t = turtle.Turtle()

#positions and draws the hot air balloon
t.pencolor("red")
t.penup()
t.setpos(0, -50)
t.pendown()
t.circle(125)
#positions and draws the basket
t.pencolor("blue")
t.penup()
t.setpos(-25, -95)
t.pendown()
t.right(0)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
#positions and draws strings tieing basket to balloon
t.pencolor("black")
t.forward(46)
t.penup()
t.setpos(25, -47)
t.pendown()
t.backward(46)
#positions and draws the decorations on the balloon
t.pencolor("purple")
#draws upper band
t.penup()
t.setpos(-98, 3)
t.pendown()
t.right(90)
t.forward(200)
#draws lower band
t.penup()
t.setpos(-98, 148)
t.pendown()
t.forward(200)
#draws many pointed snowflake
t.penup()
t.setpos(-70, 80)
t.pendown()
for i in range(36):
  t.forward(150)
  t.right(170)
  if i % 2 == 1:
    t.pencolor("blue")
  else:
    t.pencolor("green")