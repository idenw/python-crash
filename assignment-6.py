b=[]
c=[]
for i in range(0,101):
    for ii in range(1,101):
        if i%ii+i%ii+i%ii<2:
            b.append(i)
for i in b:
    if b.count(i)<3:
        c.append(i)
print(set(c))
 