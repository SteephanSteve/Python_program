#!usr/bin/python

t=raw_input()
r=""
class Stack:
    item=[]
    def _init_(self):
        self.item=item 
    def isEmpty(self):
        return self.item==[]
    def push(self,d):
        self.item.append(d)
    def pop(self):
        return self.item.pop()
s=Stack()
for c in t:
    s.push(c)
while not s.isEmpty():
    r=r+s.pop()
if t==r:
    print "yes"
else:
    print "no"
