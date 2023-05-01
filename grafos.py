from collections import deque

class Grafo:
    def __init__(self):
        self.graph = {}

    '''def cria_linha(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        self.graph[v1].append(v2)
        #self.graph[v2].append(v1) -> para grafos não direcionados'''
    
    '''def printa_grafo(self):
        for v in self.graph:
            if self.graph[v]:
                print(v, end=": ")
                for adj in self.graph[v]:
                    print(f"{adj} ")
                print()
            else:
                print(f"{v}: NULL")'''
    
    '''def reverte(self):
        grafo_reverso = Grafo()
        for v in self.graph:
            for adj in self.graph[v]:
                grafo_reverso.cria_linha(adj, v)
        return grafo_reverso'''

    def bfs(self, v_saida, v_chegada):
        fila = deque()
        visitados = []

        fila.append((v_saida, [v_saida]))

        while fila:
            no, caminho = fila.popleft()

            if no == v_chegada:
                return caminho

            if no not in visitados:
                visitados.append(no)
                for adj in self.graph[no]:
                    if adj not in visitados:
                        fila.append((adj, caminho + [adj]))

        return None

