number = (input("Please enter a positive integer number     :"))
while number.isnumeric()==False:
    print("Unaccepted entry!)")
    number = (input("Please enter a positive integer number     :"))
number= int(number)
box =[int(x) for x in str(number)] 
p=0
for i in box:
    p += (i**len(box))
if p==number:
    print("It is a n-Armstong number")
else:
    print("It is not a n-Armstong number")