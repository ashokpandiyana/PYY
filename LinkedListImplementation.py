class Node:
    # __slots__ = '_element', '_next'

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


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def traverse(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.get_data())
            curr_node = curr_node.next_node

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
        else:
            self.tail.next_node = last
        self.tail = last
        # curr_node = self.head
        # while(curr_node):
        #     curr_node = curr_node.next_node
        # curr_node.next_node = Node(data)

        self.size += 1

    def addAtFirst(self, data):
        value = Node(data)
        if(self.head):
            value.next_node = self.head
            self.head = value
        else:
            self.head = self.tail = value
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

    def removeFirst(self):
        if self.isEmpty():
            return "List is empty"
        else:
            e = self.head.get_data()
            self.head = self.head.next_node
            self.size -= 1
            if self.isEmpty():
                self.tail = None
            return e

    def removeLast(self):
        if self.isEmpty():
            print("List is Empty")
            return
        p = self.head
        i += 1
        while i < self.size - 1:
            p = p.next
            i += 1
        self.tail = p
        p = p.next_node
        e = p._element
        self.tail.next_node = None
        self.size -= 1

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

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


node1 = Node(4)
node2 = Node(3)
node1.next_node = node2

singllyLinkedList = LinkedList()
singllyLinkedList.head = node1
singllyLinkedList.tail = node2
singllyLinkedList.addAtFirst(5)
singllyLinkedList.addAtLast(6)
singllyLinkedList.addAtAny(7, 4)
singllyLinkedList.traverse()
print(singllyLinkedList.removeFirst())
print("---")
singllyLinkedList.traverse()
print("---")
print(singllyLinkedList.removeAny(2))
singllyLinkedList.traverse()


# print(node1.get_data())
# print(node1.get_nextNode().get_data())
