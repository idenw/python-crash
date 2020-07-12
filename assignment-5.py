fibo = []
for i in range(-2, 8) :
    if i < 0 : fibo.append(1)
    else : fibo.append(fibo[i] + fibo[i+1])
fibo