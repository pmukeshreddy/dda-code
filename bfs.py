graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["F"],
    "F":[]
}

visited = []
queue = []


def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:

        s = queue.pop(0)
        print(s,end=" ")

        for neg in graph[s]:


            if neg is not visited:
               visited.append(neg)
               queue.append(neg)

bfs(visited,graph,"A")