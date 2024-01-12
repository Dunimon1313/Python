#Zachary Taylor
#COP2500C Concepts in Computer Science
#Assignment #1: Problem A: Reflection Pond Measurements
#Date: 7/5/2022

#pi represents the mathematical value of Pi
pi = 3.14

#half is used as 1/2
half = .5

#Print statement asking for user's input of radius
print("Enter the radius of the pond.")

#radius is the number entered by the user, should be between 1 - 100 inclusive
radius = float(input())

#the radius is collected, and used in the formula below to calculate the area
A = half*pi*(radius*radius)

#prints the area calculated from the collected input
print("area = %d"%(A))