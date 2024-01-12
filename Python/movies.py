#Zachary Taylor
#COP2500C
#Assignment #2: Problem A - Movie Going (movies.py)
#Date: 7/5/2022
defaultTicket = 15.00
discountTicket = 12.50
singleTicketPrice = 0.00
bulkDiscount = .1
studentDiscount = .15
total = 0.00
beforeDiscountTotal = 0.00
discountApplied = 0.00

#collect input
before5 = int(input("Are you going to a movie before 5:00pm? (1 - Yes, 0 - No)\n"))
numInGroup = int(input("How many people are going?\n"))
student = int(input("Are you a student? (1 - Yes, 0 - No)\n"))

#apply time pricing
if (before5 == 1):
  singleTicketPrice = discountTicket
  beforeDiscountTotal = singleTicketPrice*numInGroup
else:
  singleTicketPrice = defaultTicket
  beforeDiscountTotal = singleTicketPrice*numInGroup

#apply discounts
if (student == 1):
  discountApplied = discountApplied + studentDiscount
if (numInGroup >= 5):
  discountApplied = discountApplied + bulkDiscount

#convert discounts from a percentage into a monetary amount
discountApplied = discountApplied*beforeDiscountTotal
#subtract the difference from the discounts to get the total left
total = beforeDiscountTotal - discountApplied

#print output of price calculator
formattedTotal = "{:.2f}".format(total)
print("The group’s price is $",formattedTotal,".\n")