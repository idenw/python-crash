number = int(input("please enter a number    :"))
test = [1]
for i in range(2,number+1):
    if not number%i:
        test.append(i) 
if len(test)>2 or number==1:               
    print(f"{number} is not a prime number.") 
else:    
    print(f" {number} is a prime number.")