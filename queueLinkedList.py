class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_nextNode(self, next_node):
        self.next_node = next_node

    def get_nextNode(self):
        return self.next_node


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        value = Node(data)
        if self.isEmpty():
            self.top = value
        else:
            value.next_node = self.top
            self.top = value
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            e = self.top.get_data()
            self.top = self.top.next_node
        self.size -= 1
        return e

    def top_elment(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.top.get_data()

    def isEmpty(self):
        return self.top == None

    def __len__(self):
        return self.size

    def traverse(self):
        p = self.top
        while(p):
            print(p.get_data(), end="-->")
            p = p.next_node
        print()


QueueImp = QueueLinkedList()
QueueImp.push(10)
QueueImp.push(20)
print(len(QueueImp))
print(QueueImp.pop())
print(QueueImp.isEmpty())
print(QueueImp.pop())
print(QueueImp.isEmpty())
QueueImp.push(40)
print(QueueImp.top_elment())
QueueImp.push(50)
print(len(QueueImp))
print(QueueImp.pop())
QueueImp.push(60)
QueueImp.push(70)
QueueImp.traverse()
