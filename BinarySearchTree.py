from queueLinkedList import QueueLinkedList


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
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


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
x.maketree(20, a, a)
y.maketree(30, a, a)
z.maketree(10, x, y)
print("Inorder")
z.traverse_inorder(z.root)
print("\nPreorder")
z.traverse_preorder(z.root)
print("\nPostorder")
z.traverse_postorder(z.root)
print('\nLevel Order')
z.levelorderTravseral()
