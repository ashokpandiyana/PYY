class Heap:
    def __init__(self):
        self.max_size = 10
        self.csize = 0
        self.data = [-1] * self.max_size

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def insert(self, e):
        if self.csize == self.max_size:
            return "No space in Heap"
            return
        self.csize += 1
        hi = self.csize
        while hi > 1 and e > self.data[hi//2]:
            self.data[hi] = self.data[hi//2]
            hi = hi // 2
        self.data[hi] = e

    def max(self):
        if self.isEmpty():
            return "Heap is Empty"
        return self.data[1]

    def deleteMax(self):
        e = data[1]
        data[1] = data[self.csize]
        data[csize] = None
        self.csize -= 1
        i = 1
        j = i * 2
        while j <= self.csize:
            if data[j] < data[j + 1]:
                j += 1
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
                i = j
                j = i * 2
            else:
                break


s = Heap()
s.insert(25)
s.insert(3)
s.insert(2)
s.insert(27)
s.insert(18)
print(s.data)
