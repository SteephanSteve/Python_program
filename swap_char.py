#!usr/bin/python

s=list(raw_input())
for i in range(len(s)):
    if not i%2==0:
        t=s[i-1]
        s[i-1]=s[i]
        s[i]=t
print ''.join(s)
