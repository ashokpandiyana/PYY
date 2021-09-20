from LinkedListImplementation import LinkedList


class HashChain:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size
        for i in range(self.hashtable_size):
            self.hashtable[i] = LinkedList()

    def hashcode(self, key):
        return key % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        self.hashtable[i].insertSorted(element)

    def search(self, key):
        i = self.hashcode(element)
        return self.hashtable[i].search(key)

    def display(self):
        for i in range(self.hashtable_size):
            print('[', i, ']', end=" ")
            self.hashtable[i].traverse()
        print()


h = HashChain()
h.insert(23)
h.insert(46)
h.insert(56)
h.insert(68)
h.display()
