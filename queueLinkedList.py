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
            self.front = value
        else:
            self.rear.next_node = value
        self.rear = value
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            e = self.front.get_data()
            self.front = self.front.next_node
        self.size -= 1
        if self.isEmpty():
            self.rear = None
        return e

    def top_elment(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.front.get_data()

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def traverse(self):
        p = self.front
        while(p):
            print(p.get_data(), end="-->")
            p = p.next_node
        print()


# QueueImp = QueueLinkedList()
# QueueImp.enqueue(10)
# QueueImp.enqueue(20)
# print(len(QueueImp))
# print(QueueImp.dequeue())
# print(QueueImp.isEmpty())
# print(QueueImp.dequeue())
# print(QueueImp.isEmpty())
# QueueImp.enqueue(40)
# print(QueueImp.top_elment())
# QueueImp.enqueue(50)
# print(len(QueueImp))
# print(QueueImp.dequeue())
# QueueImp.enqueue(60)
# QueueImp.enqueue(70)
# QueueImp.traverse()
