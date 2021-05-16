# graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSMethod(self,v,visited):
        visited.add(v)
        print(f"{v},")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSMethod(neighbour,visited)

    def DFS(self):
        visited=set()

        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSMethod(vertex,visited)


if __name__=="__main__":
    g=Graph()
    g.addEdge("A","B")
    g.addEdge("A","C")
    g.addEdge("B","D")
    g.addEdge("B","E")
    g.addEdge("C","F")
    g.addEdge("E","F")

    g.DFS()
