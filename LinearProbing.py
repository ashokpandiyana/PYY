class HashLinearProbe:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size

    def hashcode(self, key):
        return key % self.hashtable_size

    def lprobe(self, data):
        i = self.hashcode(data)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != 0:
            j += 1
        return (i+j) % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        if self.hashtable[i] == 0:
            self.hashtable[i] = element
        else:
            i = self.lprobe(element)
            self.hashtable[i] = element

    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != key:
            if self.hashtable[(i+j) % self.hashtable_size] == 0:
                return True
            j += 1
        return True

    def display(self):
        print(self.hashtable)


H = HashLinearProbe()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(93)
H.insert(34)
H.insert(86)
H.insert(28)
H.display()
