from queueLinkedList import QueueLinkedList


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def maketree(self, e, left, right):
        self.root = Node(e, left.root, right.root)

    def traverse_inorder(self, troot):
        if troot:
            self.traverse_inorder(troot.left)
            print(troot.data, end="  ")
            self.traverse_inorder(troot.right)

    def traverse_preorder(self, troot):
        if troot:
            print(troot.data, end="  ")
            self.traverse_preorder(troot.left)
            self.traverse_preorder(troot.right)

    def traverse_postorder(self, troot):
        if troot:
            self.traverse_postorder(troot.left)
            self.traverse_postorder(troot.right)
            print(troot.data, end="  ")

    def levelorderTravseral(self):
        Q = QueueLinkedList()
        t = self.root
        print(t.data, end=" ")
        Q.enqueue(t)
        while not Q.isEmpty():
            t = Q.dequeue()
            if t.left:
                print(t.left.data, end=" ")
                Q.enqueue(t.left)
            if t.right:
                print(t.right.data, end=" ")
                Q.enqueue(t.right)

    def count(self, troot):
        if troot:
            x = self.count(troot.left)
            y = self.count(troot.right)
            return x + y + 1
        return 0

    def height(self, troot):
        if troot:
            x = self.height(troot.left)
            y = self.height(troot.right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

    def searchIterative(self, key):
        troot = self.root
        while troot:
            if key == troot.data:
                return True
            elif key < troot.data:
                troot = troot.left
            elif key > troot.data:
                troot = troot.right
        return False

    def searchRecursive(self, troot, key):
        if troot:
            if key == troot.data:
                return True
            elif key < troot.data:
                return self.searchRecursive(troot.left, key)
            elif key > troot.data:
                return self.searchRecursive(troot.right, key)
        else:
            return False

    def insertionIterative(self, troot, e):
        temp = None
        while troot:
            temp = troot
            if e == troot.data:
                return
            elif e < troot.data:
                troot = troot.left
            elif e > troot.data:
                troot = troot.right
        n = Node(e)
        if self.root:
            if e < temp.data:
                temp.left = n
            else:
                temp.right = n
        else:
            self.root = n

    def insertionRecursive(self, troot, e):
        if troot:
            if e < troot.data:
                troot.left = self.insertionRecursive(troot.left, e)
            elif e > troot.data:
                troot.right = self.insertionRecursive(troot.right, e)
        else:
            n = Node(e)
            troot = n
        return troot


# B = BinarySearchTree()
# B.insertionIterative(B.root, 50)
# B.insertionIterative(B.root, 30)
# B.insertionIterative(B.root, 80)
# B.insertionIterative(B.root, 10)
# B.insertionIterative(B.root, 30)
# B.insertionIterative(B.root, 40)
# B.insertionIterative(B.root, 60)
# B.traverse_inorder(B.root)


B = BinarySearchTree()
B.root = B.insertionRecursive(B.root, 50)
B.insertionRecursive(B.root, 30)
B.insertionRecursive(B.root, 80)
B.insertionRecursive(B.root, 10)
B.insertionRecursive(B.root, 30)
B.insertionRecursive(B.root, 40)
B.insertionRecursive(B.root, 60)
B.traverse_inorder(B.root)

print(B.searchIterative(60))
print(B.searchIterative(10))
print(B.searchIterative(70))
print(B.searchRecursive(B.root, 50))
print(B.searchRecursive(B.root, 70))
