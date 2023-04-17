
class Grafo:
    def __init__(self):
        self.graph = {}

    def cria_linha(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

"""class no:
    def __init__(self, data):
        self.data = data
        self.adj = 
        self.next = None

class Lista:
    def __init__(self):
        self.head = None

    def adiciona(self, data):
        new_no = no(data)
        if self.head is None:
            self.head = new_no
            return
        last_no = self.head
        while last_no.next:
            last_no = last_no.next
        last_no.next = new_no

    def print_lista(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end='')
            if current_node.next:
                print(' -> ', end='')
            else:
                print(' -> NULL')
            current_node = current_node.next
    
    def clear(self):
        self.head = None
"""