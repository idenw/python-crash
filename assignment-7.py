fizz=[]
buzz=[]
fizzbuzz=[]
numbers=[]
for number in range(1,101):
    if number%5==0 and number%3==0:
        fizzbuzz.append(number)    
    elif number%3==0:
        fizz.append(number)
    elif number%5==0:
        buzz.append(number)    
    else:
        numbers.append(number)
print(numbers)
for i in range(1,101):
    if i in fizz:
        print("Fizz")
    elif i in buzz:
        print("Buzz")
    elif i in fizzbuzz:
        print("FizzBuzz")
    else:
        print(i)
                
             


         