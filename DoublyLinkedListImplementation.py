class Node:

    def __init__(self, data, next_node=None):
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
