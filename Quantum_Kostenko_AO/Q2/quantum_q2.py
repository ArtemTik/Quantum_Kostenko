import numpy as np


class Graph:
 
    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph
 
    def DFS(self, i, j):
        if i < 0 or i >= len(self.graph) or j < 0 or j >= len(self.graph[0]) or self.graph[i][j] != 1:
            return
 
        # mark it as visited
        self.graph[i][j] = -1

        # We count neighbors from 4 sides: north, south, west, east
        self.DFS(i, j + 1)
        self.DFS(i, j - 1)
        self.DFS(i + 1, j)
        self.DFS(i - 1, j)
 
    def countIslands(self):
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 1:
                    self.DFS(i, j)
                    count += 1 
        return count
 
 
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

values = np.random.randint(0, 2, row*col)
graph = np.array(values).reshape(row, col)
print(graph)
 
g = Graph(row, col, graph)
 
print("Number of islands is:", g.countIslands())
