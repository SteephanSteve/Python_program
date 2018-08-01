#!usr/bin/python

n,k=raw_input().split(" ")
n=int(n)
k=int(k)
a=raw_input().split(" ")
a=map(int,a)
a.sort()
b=[]
if k in a:
   x=a.index(k)
f=a[0:x]
l=a[x+1:]
l.reverse()
for i in range(3):
   if i%2==0 and len(f)>=1:
      b.append(f.pop())
   else:
      b.append(l.pop())
for i in b:
   print i,
      
   

