#!/usr/bin/python

a,b=raw_input().split(' ')
for i in range(len(a)):
   if i<len(a)-1: 
      if a[i]+a[i+1] in b:
         print "yes"
         break
else:
    print "no"


