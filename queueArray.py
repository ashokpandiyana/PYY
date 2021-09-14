class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.data.pop(0)

    def top(self):
        if self.isEmpty():
            return
        return self.data[0]

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def traverse(self):
        for i in range(len(self.data)):
            print(self.data[i])


queueImp = Queue() 
queueImp.enqueue(10)
queueImp.enqueue(20)
print(len(queueImp))
print(queueImp.pop())
print(queueImp.isEmpty())
print(queueImp.pop())
print(queueImp.isEmpty())
queueImp.push(40)
print(queueImp.top())
queueImp.push(50)
print(len(queueImp))
print(queueImp.pop())
queueImp.push(60)
queueImp.push(70)
queueImp.traverse()
