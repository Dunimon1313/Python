#Zachary Taylor
#COP2500C
#Assignment #4: Turtle Shapes (Functions)
#Date: 7/26/2022

#import necessary libraries
import turtle

#This functions relates to summer vacation because... it draws an umbrella, which keeps you from getting sun-burn
def drawUmbrella(x, y):
  #initialize drawing object and set position of pen
  t = turtle.Turtle()
  t.penup()
  t.setpos(x, y+100)
  t.pendown()
  #draw stick
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(5)
  t.left(90)
  t.forward(100)
  #draw canvas
  t.left(90)
  t.forward(50)
  t.left(180)
  t.forward(100)
  t.left(180)
  t.forward(100)
  t.right(90)
  for x in range(180):
    t.forward(.88)
    t.right(1)

#This functions relates to summer vacation because... it draws a cooler to keep your drinks cool
def drawCooler(x, y):
  #initialize drawing object and set position of pen
  t = turtle.Turtle()
  t.penup()
  t.setpos(x, y)
  t.pendown()
  #draws the body of the cooler
  t.forward(20)
  t.left(90)
  t.forward(20)
  t.left(90)
  t.forward(20)
  t.left(90)
  t.forward(20)
  t.left(180)
  #draws the handle of the cooler
  t.forward(15)
  t.right(90)
  t.forward(25)
  t.left(90)
  t.forward(10)
  t.left(90)
  t.forward(30)
  t.left(90)
  t.forward(10)
  t.left(90)
  t.forward(5)

  
drawUmbrella(-50,-20)
drawCooler(0,-20)