class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.data[-1]

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def traverse(self):
        for i in range(len(self.data)):
            print(self.data[i])


stackImp = Stack()
stackImp.push(10)
stackImp.push(20)
print(len(stackImp))
print(stackImp.pop())
print(stackImp.isEmpty())
print(stackImp.pop())
print(stackImp.isEmpty())
stackImp.push(40)
print(stackImp.top())
stackImp.push(50)
print(len(stackImp))
print(stackImp.pop())
stackImp.push(60)
stackImp.push(70)
stackImp.traverse()
