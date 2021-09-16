class Node:
    __slots__ = 'data', 'next_node', 'prev_node'

    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_nextNode(self, next_node):
        self.next_node = next_node

    def get_nextNode(self):
        return self.next_node

    def set_prevNode(self, prev_node):
        self.next_node = prev_node

    def get_prevNode(self):
        return self.prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addLast(self, data):
        value = Node(data, None, None)
        if self.isEmpty():
            self.head = value
            self.tail = value
        else:
            self.tail.next_node = value
            value.prev_node = self.tail
            self.tail = value
        self.size += 1

    def addFirst(self, data):
        value = Node(data, None, None)
        if self.isEmpty():
            self.head = value
            self.tail = value
        else:
            value.next_node = self.head
            self.head.prev_node = value
            self.head = value
        self.size += 1

    def addAny(self, data, position):
        value = Node(data, None, None)
        p = self.head
        i = 0
        while i < position - 1:
            p = p.next_node
            i += 1
        value.next_node = p.next_node
        p.next_node.prev_node = value
        p.next_node = value
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return "List is Empty"
        else:
            e = self.head.get_data()
            self.head = self.head.next_node
            self.head.prev_node = None
        self.size -= 1
        if self.isEmpty():
            self.tail = None
        return e

    def removeLast(self):
        if self.isEmpty():
            return "List is Empty"
        else:
            e = self.tail.get_data()
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.size -= 1
        return e

    def removeAny(self, position):
        if self.isEmpty():
            return "List is Empty"
        else:
            p = self.head
            i = 0
            while i < position:
                p = p.next_node
                i += 1
            e = p.next_node.get_data()
            p.next_node = p.next_node.next_node
            p.next_node.prev_node = p
            self.size -= 1
            return e

    def traverse(self):
        p = self.head
        while(p):
            print(p.get_data(), end="-->")
            p = p.next_node
        print()

    def traverse_reverse(self):
        p = self.tail
        while(p):
            print(p.get_data(), end="-->")
            p = p.prev_node
        print()


L = DoublyLinkedList()
L.addLast(10)
L.addLast(12)
L.addLast(13)
print(L.size)
L.addFirst(8)
L.traverse()
L.traverse_reverse()
