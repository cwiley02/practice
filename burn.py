# Own code demonstrating knowledge for elif statements

wind = int(input())

# For example, the safe wind speed for burning brush is considered to be less than 10 mph (miles per hour). 

if wind == 0:
    print("Very safe, indeed")
elif wind < 10:
    print("Safe to burn")
elif wind >= 10:
    print ("Do not burn")
