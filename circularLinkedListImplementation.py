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


class CircularSinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def traverse(self):
        curr_node = self.head
        i = 0
        while(i < self.size):
            print(curr_node.get_data(), end="-->")
            curr_node = curr_node.next_node
            i += 1
        print()

    def search(self, data):
        count = 0
        curr_node = self.head
        while(curr_node):
            if (curr_node.get_data() == data):
                return count
            curr_node = curr_node.next_node
            count += 1
        return "Not Found"

    def addAtLast(self, data):
        last = Node(data)
        if self.isEmpty():
            self.head = last
            last.next_node = last
        else:
            last.next_node = self.tail.next_node
            self.tail.next_node = last
        self.tail = last
        self.size += 1

    def addAtFirst(self, data):
        value = Node(data)
        if self.isEmpty():
            value.next_node = value
            self.head = value
            self.tail = value
        else:
            self.tail.next_node = value
            value.next_node = self.head
            self.head = value
        self.size += 1

    def addAtAny(self, data, position):
        value = Node(data)
        i = 1
        p = self.head
        while i < position - 1:
            p = p.next_node
            i += 1
        value.next_node = p.next_node
        p.next_node = value
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return "List is empty"
        else:
            e = self.head.get_data()
            self.tail.next_node = self.head.next_node
            self.head = self.head.next_node
            self.size -= 1
            if self.isEmpty():
                self.tail = None
                self.head = None
            return e

    def removeLast(self):
        if self.isEmpty():
            return "List is Empty"
        p = self.head
        i += 1
        while i < self.size - 1:
            p = p.next
            i += 1
        self.tail = p
        p = p.next_node
        e = p.get_data()
        self.tail.next_node = self.head
        self.size -= 1
        return e

    def removeAny(self, position):
        p = self.head
        i = 1
        while i < position - 1:
            p = p.next_node
            i += 1
        e = p.next_node.get_data()
        p.next = p.next_node.next_node
        self.size -= 1
        return e


circularLinkedList = CircularSinglyLinkedList()
circularLinkedList.addAtLast(6)
circularLinkedList.addAtLast(8)
circularLinkedList.addAtFirst(3)


circularLinkedList.traverse()
