import numpy as np


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = np.zeros((vertices, vertices))

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
