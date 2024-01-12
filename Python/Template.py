#Zachary Taylor
#7-8-2022
#COP2500C
#Lab 2 Challenge 3

# Lab 2 Template
# Ask for input
location = input("Where would you like to go?\n")
if (location == "Beach"):
    #asks for number of beach balls and prints a statement on whether or not they       have enough
    confirmation = int(input("How many beach balls do you have?\n"))
    if confirmation >= 5:
      print("You are well prepared.\n")
    else:
      print("Are you sure you have enough?\n")
if (location == "Theme Park"):
    #asks for how many parks the user plans to visit and creates an itinerary
    confirmation = int(input("How many parks are you going to?\n"))
    for i in range(1, confirmation, 1):
      print("Day ",i,", Park ",i,"\n")
if (location == "Science Center"):
    #asks if the user is ready to leave
    confirmation = input("Are you ready to leave?\n")
    while(confirmation != "Ready"):
      confirmation = input("Are you ready to leave?\n")
    