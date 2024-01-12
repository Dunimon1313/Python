#Zachary Taylor
#COP2500C
#Assignment #5: Problem A
#Date: 7/26/2022

import math

#function declarations
def solveForFirstRoot(a,b,c):
  #quadratic function: (-b+sqrt(b*b-4*a*c))/(2*a)
  y = math.sqrt((b*b-4*a*c))
  x = (-b+y)/(2*a)
  return x

def solveForSecondRoot(a,b,c):
  #quadratic function: (-b-sqrt(b*b-4*a*c))/(2*a)
  y = math.sqrt((b*b-4*a*c))
  x = (-b-y)/(2*a)
  return x

def findNumberOfRoots(a,b,c):
  #uses the determinant to find number of roots, and returns that number
  numRoots = (b*b)-(4*a*c)
  if numRoots > 0:
    return 2
  elif numRoots == 0:
    return 1
  else:
    return 0
    
#main
print("======================Root Solver======================")
a = float(input("\nEnter coefficient a: "))
b = float(input("\nEnter coefficient b: "))
c = float(input("\nEnter coefficient c: "))

#find number of roots to determine correct OOP
numRoots = findNumberOfRoots(a,b,c)

if numRoots == 2:
  #there are two unique roots, so they both must be found
  root1 = solveForFirstRoot(a,b,c)
  root2 = solveForSecondRoot(a,b,c)
  print("That quadratic has two roots: %d and %d" %root1,root2)
elif numRoots == 1:
  #there is only one unique root, so solveForFirst or Second can be used here
  root1 = solveForFirstRoot(a,b,c)  
  print("That quadratic has one root: %d" %root1)
else:
  #there is a complex root, and this application doesn't solve for those
  print("Sorry, that quadratic has complex roots.")