#Zachary Taylor
#COP2500C
#Assignment #7: Strings
#Date: 7/5/2022

def printCourseList(clist):
  comparatorList = list()
  #output varies on number of classes
  if comparatorList == clist:
    #when number classes equals 0
    print("You aren't currently taking any courses.\n\n")
  else:
    #when there is any number of classes
    print("You are currently taking these courses:")
    for x in range(0, len(clist), 1):
      print("\t%d. %s" %(x+1, clist[x]))
    print("\n")

def inputFormatter(strIn):
  #removes all whitespaces from string, leaving the commas as a way to differintiate between courses
  x = strIn.lower()
  y = str()
  for c in range(len(x)):
    if (x[c].isalpha()) or (x[c] == ","):
      y = y +x[c]
  return y

def courseAdd(blist, dstr):
  tempList = list()
  tempstr = str()
  a = 0
  
  #stores each class from the input
  for x in range(len(dstr)):
    if(dstr[x] != ','):
      #adds each character to tempstr to build the word
      tempstr = tempstr + dstr[x]
    else:
      #once a  ',' has been reached, tempstr is added to tempList to save that phrase
      tempstr = tempstr.title()
      tempList.append(tempstr)
      #tempstr is reset to continue the process
      tempstr = ''
  tempstr = tempstr.title()
  tempList.append(tempstr)
  #checks if any of the entered classes is repeated in the master list
  for y in range(0, len(tempList), 1):
    for z in range(0, len(blist), 1):
      if tempList[y] == blist[z]:
        #if any input is repeated, then that input is marked with a unique string that          #will later be used for identification. a keeps track of how many times to             #call .remove, this matters because using .remove more times than the string           #to be deleted exists will cause an error
        tempList[y] = "JimmyJohnsIsHavingASale"
        a+=1
  #removes repeats
  for q in range(a):
    tempList.remove("JimmyJohnsIsHavingASale")
  #templist is now free of repeats, and is added to the master list
  for w in range(0, len(tempList), 1):
    blist.append(tempList[w])
  return blist

# math,physics,  SCIENCE, Sociology ,english,CompSci,  psychology
# compsci
# Pyhsics, English, science

def courseDrop(alist, bstr):
  tempList = list()
  tempstr = str()
  #stores each class from the input
  for x in range(len(bstr)):
    if(bstr[x] != ','):
      #adds each character to tempstr to build the word
      tempstr = tempstr + bstr[x]
    else:
      #once a  ',' has been reached, tempstr is added to tempList to save that phrase
      tempstr = tempstr.title()
      tempList.append(tempstr)
      #tempstr is reset to continue the process
      tempstr = ''
  tempstr = tempstr.title()
  tempList.append(tempstr)
  #all instances matching user's input for deletion are found and marked with a unique   string
  a = 0
  #checks for the existence of specified classes and marks them with a unique string
  for j in range(0, len(tempList), 1):
    for i in range(0, len(alist), 1):
      if (alist[i] == tempList[j]):
        alist[i] = ""
        a+=1
        break 
  #desired deletions occur
  for d in range(a):
    alist.remove("")
  return alist

#initialize a list to hold correctly formatted input
courseList = list()

#loop infinitely until number of courses = desired amount
while(True):
  #print formatted list
  printCourseList(courseList)
  #if number of courses is insufficient or too much, collect more classes from user for adding or removing
  if (len(courseList) < 5):
    desiredCourses = input("What courses would you like to take? ")
    #input collected must be formatted before being added to list
    formattedInput = inputFormatter(desiredCourses)
    #add input to list in desired format
    courseList = courseAdd(courseList, formattedInput)
  elif(len(courseList) > 5):
    desiredCourses = input("What courses would you like to drop? ")
    #input collected must be formatted before being added to list
    formattedInput = inputFormatter(desiredCourses)
    #remove input from list in desired format
    courseList = courseDrop(courseList, formattedInput)
  else:
    break

print("Done!\n")