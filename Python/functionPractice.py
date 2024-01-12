#Zachary Taylor
#COP2500C
#Assignment 4A
#Date: 7/26/2022

# Assignment 4A
# Directions
# Fill out each function.   Only write within the function you are editing

# In this function you will add the two numbers together
# If the numbers are the same, multiple the two numbers together.
def function1(a, b):
  if(a==b):
    return a*b
  else:
    return a+b
    
# If b is true then return the value of A, If it is false return double the value of A
def function2(a, b):
  if(b==True):
    return a
  else:
    return 2*a

# if A and B are both True then return True, If A is true and B is False return True, return false for everything else.
def function3(a, b):
  if(a == True and b == True):
    return True
  elif(a == True and b == False):
    return True
  else:
    return False
# Do not edit anything below this point
def main():
    print("Testing Function #1")
    print("Answer: 7, Your Answer:", function1(3, 4))
    print("Answer: 16, Your Answer:", function1(4, 4))
    print("Answer: 8, Your Answer:", function1(5, 3))
    print()
    print("Testing Function #2")
    print("Answer: 3, Your Answer:", function2(3, True))
    print("Answer: 4, Your Answer:", function2(2, False))
    print("Answer: 9, Your Answer:", function2(9, True))
    
    print()
    print("Testing Function #3")
    print("Answer: True, Your Answer:", function3(True, False))
    print("Answer: False, Your Answer:", function3(False, True))
    print("Answer: True, Your Answer:", function3(True, True))
    print("Answer: False, Your Answer:", function3(False, False))
main()