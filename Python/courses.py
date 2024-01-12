#Zachary Taylor
#COP2500C
#Assignment #6: Course Selection (courses.py)
#Date: 7/5/2022

#adds an element to a prepared array that follows the logic that, at the start, is filled with strings called "empty". As the array is filled up, it will return a boolean for whether or not it has room for more elements
def addToArray(classList, k):
  #this loop searches for an empty slot and then fills it
  for x in range(0, 6, 1):
    if classList[x] == "empty":
      classList[x] = k
      break
  #a boolean must be returned so that the lack of room left can be signaled
  if classList[5] != 'empty':
    return False
  else:
    return True

#removes an element from a full array by shuffling the remaining elements one step forward in the array
def removeFromArray(classList, target):
  #target must be decremented since the user selects a number based on 1-6 whereas the        program's array is based on 0-5
  target = target - 1
  for x in range(target, 5, 1):
    if (x == 4):
      classList[x+1] = "empty"
    else:
      classList[x] = classList[x+1]

#prints the array in the desired formatted manner
def printClassList(classList):
  i = 0
  while(classList[i] != "empty"):
    print("%d. %s\n" %(i+1, classList[i]))
    i+= 1
    if i >= 6:
      break

print("Welcome to class registration!")
#classList is initialized with 6 strings of "empty" so that untouched slots can be identified and filled
classList = ["empty", "empty", "empty", "empty", "empty", "empty"]
k = "x"
#since the loop needs to run until the user exits the program, the input collection and output will be looped until the exit command is given
while(k != "EXIT"):
  k = input("Enter a course code:\n")
  if k == "EXIT":
    break
  roomLeft = addToArray(classList, k)
  printClassList(classList)
  while(roomLeft == False):
    print("You have registered for too many courses. Please pick one to delete.\n")
    k = input("Enter a number between 1 and 6.\n")
    if k == "EXIT":
      break
    if k > 6 or k < 1:
      continue
    else:
      removeFromArray(classList, k)
      roomLeft = True
  if k == "EXIT":
    break
print("Goodbye")