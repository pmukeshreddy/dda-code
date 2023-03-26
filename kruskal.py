class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    def find(self,parent,i):
        if parent[i] == i:
            return i
        else:
            return self.find(self,parent,parent[i])

    def apply_union(self,parnent,rank,x,y):

        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        
