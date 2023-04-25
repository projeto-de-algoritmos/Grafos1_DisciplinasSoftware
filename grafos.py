
class Grafo:
    def __init__(self):
        self.graph = {}

    def cria_linha(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        self.graph[v1].append(v2)
        #self.graph[v2].append(v1)
    
    def printa_grafo(self):
        for v in self.graph:
            if self.graph[v]:
                print(v, end=": ")
                for adj in self.graph[v]:
                    print(adj, end=" ")
                print()

