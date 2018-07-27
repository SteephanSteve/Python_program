#!usr/bin/python

n=int(input())
l=raw_input().split(" ")
n-=1
while n>=0:
    print l[n],
    if n>0:
        print "->",
    n-=1

    
