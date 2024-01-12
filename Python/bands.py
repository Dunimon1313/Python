#Zachary Taylor
#COP2500C
#Assignment #3: UCF Bands
#Date: 7/5/2022

#ask user for input
firstBandOut = int(input("When will the first band come out?\n"))
numBands = int(input("How many bands will be playing tonight?\n"))


#time keeps track of when the next band is coming out
time = firstBandOut

#this loop will ask the user for the length each band will play, and then output when each band will start
for i in range(1, numBands+1, 1):
  playLength = int(input("How long does band number %d play?\n" %i))
  print("Band #%d came out at %d minutes." %(i, time))
  time = time + playLength
#since there are no more bands, time now contains the total time played
print("The total set ended at %d minutes." %time)