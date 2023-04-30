from grafos import Grafo

grafo = Grafo()
grafo.graph = {'cálculo 1': ['Cálculo 2','Cálculo 3'],
               'Cálculo 3':[],
               'Cálculo 2': ['Métodos Numéricos de engenharia'],
               'Métodos Numéricos de engenharia': [],
               'Algoritmos e Programação de Computadores': ['Orientação a objetos'],
               'Desenho Industrial Assistido por Computador':['Interação Humano computador'],
               'Engenharia e ambiente':[],
               'Introdução a engenharia':['Probabilidade e Estatística Aplicada à Engenharia']}



#grafo.printa_grafo()
path = grafo.bfs('cálculo 1', 'Métodos Numéricos de engenharia')
print(path)