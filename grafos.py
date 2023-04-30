
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
   
    def adiciona_arco(self, u, v):
        " Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. "
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]

    def printa_grafo(self):
        for v in self.graph:
            if self.graph[v]:
                print(v, end=": ")
                for adj in self.graph[v]:
                    print(adj, end=" ")
                print()

