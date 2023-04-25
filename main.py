from grafos import Grafo

grafo = Grafo()
n = int(input("Digite o número de arestas: "))

for i in range(n):
    v1 = input(f"digite o valor do nó {i+1}: ")
    v2 = input("digite o valor do nó sink: ")
    grafo.cria_linha(v1,v2)


grafo.printa_grafo()
