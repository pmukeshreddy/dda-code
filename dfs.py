graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["F"],
    "F":[]
}
vis = set()

def dfs(visted,graph,node):
    if node is not visted:
        print(node)
        visted.add(node)

        for neg in graph[node]:
               dfs(visted,graph,neg)


dfs(vis,graph,"A")