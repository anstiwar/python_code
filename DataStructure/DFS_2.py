# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

# graph1 = {
#     'A' : ['B','S'],
#     'B' : ['A'],
#     'C' : ['D','E','F','S'],
#     'D' : ['C'],
#     'E' : ['C','H'],
#     'F' : ['C','G'],
#     'G' : ['F','S'],
#     'H' : ['E','G'],
#     'S' : ['A','C','G']
# }


def dfs(graph,node,visited=[]):
    if node not in visited:
        visited.add(node)
        if node in graph:
            for neighbour in graph[node]:
                dfs(visited,graph,neighbour)
            return visited


if __name__=="__main__":
    dfs(graph,"A")
