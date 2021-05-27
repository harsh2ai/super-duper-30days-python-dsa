class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, ite):
        return self.item.append(ite)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]

    def size(self):
        return len(self.item)


def divideby2(decnumber):

    remstack = Stack()

    while decnumber > 0:
        rem = decnumber % 2
        remstack.push(rem)
        decnumber = decnumber // 2
    binstr = ""
    while not remstack.isEmpty():
        binstr = binstr + str(remstack.pop())

    return print(binstr)


divideby2(20)
