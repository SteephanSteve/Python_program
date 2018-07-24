#!usr/bin/python

a,b=raw_input().split(" ")
c=0
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            c+=1
if c==1:
    print "yes"
else:
    print "no"
