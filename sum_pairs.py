#!usr/bin/python

n,k=raw_input().split(" ")
a=raw_input().split(" ")
n=int(n)
k=int(k)
a=map(int,a)
c=0
for i in range(n):
    for j in range(i,n):
        if a[i]+a[j]==k:
            c+=1
            break
if c:
    print "YES"
else:
    print "NO"
