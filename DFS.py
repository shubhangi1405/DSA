class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = [[0 for i in range(9)] for j in range(9)]

    def create(self):
        self.v = int(input("Enter no of vertices: "))
        self.e = int(input("Enter no of edges: "))

        for i in range(self.e):
            print(f"Enter edge {i + 1}:")
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            w = int(input("Enter weight: "))

            self.G[u][v] = w
            self.G[v][u] = w

    def display(self):
        print("\nAdjacency Matrix:")
        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return -1
        return self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return -1
        return self.items[-1]


def dfs(ob, start):
    visited = [False] * ob.v
    s = Stack()

    s.push(start)

    while s.top() != -1:
        u = s.pop()

        if visited[u] == False:
            print(u, end=" ")
            visited[u] = True

            # Push adjacent vertices
            for v in range(ob.v - 1, -1, -1):
                if ob.G[u][v] != 0 and visited[v] == False:
                    s.push(v)


# Main program
g = Graph()

g.create()
g.display()

start = int(input("\nEnter start vertex for DFS: "))

print("DFS traversal:")
dfs(g, start)
