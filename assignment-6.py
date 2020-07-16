num=int(input("please enter a number   :  "))
b=[]
c=[]
for i in range(2,num):
    for ii in range(1,num):
        if i%ii+i%ii+i%ii<2:
            b.append(i)
for i in b:
    if b.count(i)<3:
        c.append(i)
print(set(c))
 