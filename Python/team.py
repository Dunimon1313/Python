#Zachary Taylor
#COP2500C
#Assignment #2: Problem B: The Better Team (team.py)
#Date: 7/12/2022

#initialize and collect user input
ucfRanking = int(input("What is UCF's ranking?\n"))
number1 = int(input("What is team #1's ranking?\n"))
number2 = int(input("What is team #2's ranking?\n"))

#for and against are used to keep track of how ucf will score against the other teams
ucfFor = 0
ucfAgainst = 0

#increments ucf's score by seeing if ucf's rank is lower or higher than current #1 and #2 teams
if(ucfRanking < number1):
  ucfFor += 1
if(ucfRanking < number2):
  ucfFor += 1
if(ucfRanking > number1):
  ucfAgainst += 1
if(ucfRanking > number2):
  ucfAgainst += 1

#decision tree for who is best team. determined by who has lowest rank (lower = better)
if (ucfRanking < number1):
  if (ucfRanking < number2):#case for if 
    print("UCF's record is %d-%d\n" %(ucfFor, ucfAgainst))
    print("Best Team: UCF\n")
if (number1 < ucfRanking):
  if (number1 < number2):
    print("UCF's record is %d-%d\n" %(ucfFor, ucfAgainst))
    print("Best Team: Team #1\n")
if (number2 < ucfRanking):
  if (number2 < number1):
    print("UCF's record is %d-%d\n" %(ucfFor, ucfAgainst))
    print("Best Team: Team #2\n")