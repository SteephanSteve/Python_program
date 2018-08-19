#!/usr/bin/python

s=raw_input()
s=s.replace(' ','')
for i in s:
    if not i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
      print "no"
      break
else:
    print "yes"
