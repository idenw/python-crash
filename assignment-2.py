print("Please enter 1 for yes, 0 for no")
chronic = bool(int(input("Do you have a severe chronic disease?, 1 or 0")))
age = bool(int(input("Are you a cigarette addict older than 75 years old? , 1 or 0")))
immune = bool(int(input("Is your immune system too weak?, 1 or 0")))
if age or chronic or immune :
    print("You are in risky group")
else:
    print("You are not in risky group")
