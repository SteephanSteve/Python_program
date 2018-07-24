#!usr/bin/python

n=int(input())
s=raw_input()
r=[]
for i in range(n):
    if s[i].lower() not in "aeiou":
        r.append(s[i])
r=''.join(r)
print r[::-1]
