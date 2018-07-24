#!usr/bin/python

a,b=raw_input().split(" ")
a=int(a)
b=int(b)
x=[]
c=0
for i in range(a,b+1):
    k=list(bin(i))
    del k[1]
    k=map(int,k)
    x.append(sum(k))
for i in x:
    if i>1:
       for j in range(2,i):
           if i%j==0:
               break
       else:
            c+=1
print c
