class Graph:
    def __init__(self):
        self.v=0
        self.e=0
        self.G=[[0 for i in range(9)] for j in range(9)]

    def create(self):
        self.v=int(input("Enter no of vertices:-"))
        self.e=int(input("Enter no of edges:-"))

        for i in range(self.e):
            print(f"Entrer edge {i+1}:")
            u=int(input("Enter start vertex:"))
            v=int(input("Enter end vertex:"))
            w=int(input("Enter Weight:"))
            self.G[u][v]=self.G[v][u]=w

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()
g=Graph()
g.create()
g.display()
