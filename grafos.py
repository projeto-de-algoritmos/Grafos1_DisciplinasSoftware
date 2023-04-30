from collections import deque

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
                    print(f"{adj} ")
                print()
            else:
                print(f"{v}: NULL \n")
    
    def bfs(self, v_saida, v_chegada):
        queue = deque()
        visited = set()

        queue.append((v_saida, [v_saida]))

        while queue:
            node, path = queue.popleft()

            if node == v_chegada:
                return path

            if node not in visited:
                visited.add(node)
                for adj in self.graph[node]:
                    if adj not in visited:
                        queue.append((adj, path + [adj]))

        return None

