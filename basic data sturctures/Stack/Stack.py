class stack():
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
    
"""

s=Stack()
4
​
5
print(s.isEmpty())
6
s.push(4)
7
s.push('dog')
8
print(s.peek())
9
s.push(True)
10
print(s.size())
11
print(s.isEmpty())
12
s.push(8.4)
13
print(s.pop())
14
print(s.pop())
15
print(s.size())
"""