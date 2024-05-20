print("Enter principle amount of a CD")
principle = float(input())
print("Enter the number of years for the CD")
years = int(input())
intrest_rate = 0
if principle > 10000 and years == 5: intrest_rate = 0.06
elif 50000 <= principle <= 100000 and years == 10:
 intrest_rate = 0.05
elif 50000 <= principle <= 100000 and years == 10:
 intrest_rate = 0.04
else:
  intrest_rate = 0.02
intrest = principle * intrest_rate
print("Principle: ", principle)
print("Intrest Rate: ", intrest_rate)
print("Intrest: ", intrest)


#elif principle 50000 <= 10000 and years == 10: intrest_rate = 0.05
#elif principle 50000 <= 10000 and years == 5:  intrest_rate = 0.04
#else intrest_rate = 0.02
#intrest = principle * intrest_rate
#print("Principle: ", principle)
#print("Intrest Rate: ", intrest_rate)
#print("Intrest: ", intrest)
#I keep getting a strange syntax error that I can't seem to pinpoint, you can try and run the code and see for yourself, but Replit's debugger hasn't been much help in identifying the issue.