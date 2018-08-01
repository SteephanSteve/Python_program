#!/usr/bin/python

def perm(s,f,l):
   if f==l:
      print ''.join(s)
   else:
      for i in range(f,l+1):
         s[i],s[f]=s[f],s[i]
         perm(s,f+1,l)
         s[f],s[i]=s[i],s[f]
s=list(raw_input())
perm(s,0,len(s)-1)
   

