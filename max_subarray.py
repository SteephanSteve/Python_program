#!usr/bin/python

n=int(input())
l=raw_input().split(" ")
l=map(int,l)
l.sort()
s=[]
for i in range(n):
    if l[i]>0:
        s.append(l[i])
if n==len(s):
    print sum(s)
elif not s:
    print l[n-1]
else:
    print sum(s)

 
