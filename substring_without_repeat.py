#!/usr/bin/python

s=raw_input()
a=[]
c=0
for i in s:
    if not i in a:
        c+=1
        a.append(i)
    else:
        break
print c
