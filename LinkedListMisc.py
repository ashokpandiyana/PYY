from LinkedListImplementation import LinkedList

Q = LinkedList()
Q.addAtLast(1)
Q.addAtLast(2)
Q.addAtLast(2)
Q.addAtLast(1)

Q.traverse()

# Palindrome LinkedList use Fast & Slow Pointer


def Palindrome(Q):
    fast = Q.head
    slow = Q.head
    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node
    prev = None
    # while slow:
    return


Palindrome(Q)
