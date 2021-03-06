import numpy as np
from queueLinkedList import QueueLinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0 for x in range(self.vertices)]
                          for x in range(self.vertices)]
        self._visited = [0] * self.vertices

    def __str__(self):
        return str(self.adjMatrix)

    def insertEdge(self, u, v, x=1):
        self.adjMatrix[u][v] = x

    def removeEdge(self, u, v):
        self.adjMatrix[u][v] = 0

    def exist_edge(self, u, v):
        return self.adjMatrix[u][v] != 0

    def vertices_count(self):
        return self.vertices

    def edge_count(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMatrix[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self.vertices):
            print(i, end=" ")
        print()

    def edges(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMatrix[i][j] != 0:
                    print(i, '--', j)
        print()

    def outdegree(self, v):
        count = 0
        for j in range(self.vertices):
            if self.adjMatrix[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self.vertices):
            if self.adjMatrix[i][v] != 0:
                count += 1
        return count

    def display(self):
        print(self.adjMatrix)

    def BFS(self, s):
        i = s
        q = QueueLinkedList()
        visited = [0] * self.vertices
        print(i, end=" ")
        visited[i] = 1
        q.enqueue(i)
        while not q.isEmpty():
            i = q.dequeue()
            for j in range(self.vertices):
                if self.adjMatrix[i][j] == 1 and visited[j] == 0:
                    print(j, end=" ")
                    visited[j] = 1
                    q.enqueue(j)

    def DFS(self, s):
        if self._visited[s] == 0:
            print(s, end=" ")
            self._visited[s] = 1
            for j in range(self.vertices):
                if self.adjMatrix[s][j] == 1 and self._visited[j] == 0:
                    self.DFS(j)


G = Graph(7)
G.insertEdge(0, 1)
G.insertEdge(0, 5)
G.insertEdge(0, 6)
G.insertEdge(1, 0)
G.insertEdge(1, 2)
G.insertEdge(1, 5)
G.insertEdge(1, 6)
G.insertEdge(2, 3)
G.insertEdge(2, 4)
G.insertEdge(2, 6)
G.insertEdge(3, 4)
G.insertEdge(4, 2)
G.insertEdge(4, 5)
G.insertEdge(5, 2)
G.insertEdge(5, 3)
G.insertEdge(6, 3)
print(G)
print("BFS")
G.BFS(0)
print("\nDFS")
G.DFS(0)

# Unweighted undirect Graph
# G = Graph(4)
# G.display()
# print("Vertices", G.vertices_count())
# print("Edges", G.edge_count())
# G.insertEdge(0, 1)
# G.insertEdge(0, 2)
# G.insertEdge(1, 0)
# G.insertEdge(1, 2)
# G.insertEdge(2, 0)
# G.insertEdge(2, 1)
# G.insertEdge(2, 3)
# G.insertEdge(3, 2)
# G.display()
# print("Vertices", G.vertices_count())
# print("Edges", G.edge_count())
# G.edges()
# print(G.indegree(2))
# G.removeEdge(1, 2)
# print(G.exist_edge(1, 2))

# weight undirect graph
# G = Graph(4)
# G.display()
# print("Vertices", G.vertices_count())
# print("Edges", G.edge_count())
# G.insertEdge(0, 1, 26)
# G.insertEdge(0, 2, 16)
# G.insertEdge(1, 0, 26)
# G.insertEdge(1, 2, 12)
# G.insertEdge(2, 0, 16)
# G.insertEdge(2, 1, 12)
# G.insertEdge(2, 3, 8)
# G.insertEdge(3, 2, 8)
# G.display()
# print("Vertices", G.vertices_count())
# print("Edges", G.edge_count())
# G.edges()
# print(G.indegree(2))
# G.removeEdge(1, 2)
# print(G.exist_edge(1, 2))


# Directed Graph
# G = Graph(4)
# G.display()
# print("Vertices", G.vertices_count())
# G.insertEdge(0, 1)
# G.insertEdge(0, 2)
# G.insertEdge(1, 2)
# G.insertEdge(2, 3)
# G.insertEdge(2, 3)
# G.display()
# print("Vertices", G.vertices_count())
# G.edges()
# print(G.exist_edge(1, 3))
# print(G.exist_edge(1, 2))
# print(G.indegree(2))
# print(G.outdegree(2))
# G.removeEdge(1, 2)
# print(G.exist_edge(1, 2))
# G.display()
# weighted Directed Graphs
# G = Graph(4)
# G.display()
# print("Vertices", G.vertices_count())
# G.insertEdge(0, 1, 12)
# G.insertEdge(0, 2, 16)
# G.insertEdge(1, 2, 14)
# G.insertEdge(2, 3, 8)
# G.display()
# print("Vertices", G.vertices_count())
# G.edges()
# print(G.exist_edge(1, 3))
# print(G.exist_edge(1, 2))
# print(G.indegree(2))
# print(G.outdegree(2))
# G.removeEdge(1, 2)
# print(G.exist_edge(1, 2))
# G.display()
