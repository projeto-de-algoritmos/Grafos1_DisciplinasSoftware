import tkinter as tk

from grafos import Grafo

grafo = Grafo()
grafo.graph = {'Cálculo 1': ['Cálculo 2','Probabilidade e Estatística Aplicada em Engenharia'],
               'Probabilidade e Estatística Aplicada em Engenharia':[],
               'Cálculo 2': ['Métodos Numéricos para engenharia'],
               'Métodos Numéricos para engenharia': [],
               'Algoritmos e Programação de Computadores': ['Orientação a Objetos', 'Desenvolvimento de Software','Estrutura de Dados 1'],
               'Desenho Industrial Assistido por Computador':['Interação Humano computador'],
               'Desenvolvimento de Software':[],
               'Engenharia e Ambiente':[],
               'Introdução a Engenharia':[],
               'Física 1':[],
               'Física Experimental 1':[],
               'Introdução à Algebra Linear':['Teoria de Eletrônica Digital 1','Prática de Eletrônica Digital 1'],
               'Teoria de Eletrônica Digital 1':['Fundamentos de Arquiteturas de Computadores'],
               'Pratica de Eletrônica Digital 1':[],
               'Humanidades e Cidadania':[],
               'Engenharia Econômica':['Gestão da Produção e Qualidade'],
               'Orientação a Objetos':['Projeto Integrador 1','Métodos de Desenvolvimento de Software','Paradigmas de Programação'],
               'Matemática Discreta':['Matemática Discreta 2'],
               'Gestão da Produção de Qualidade':['Qualidade de Software 1'],
               'Métodos de Desenvolvimento de Software':['Requisitos de Software','Interação Humano Computador','Testes de Software'],
               'Estrutura de Dados 1':['Estrutura de Dados 2','Compiladores 1','Projeto de Análise de Algoritmos'],
               'Fundamentos de Arquiteturas de Computadores':['Fundamentos de Sistemas Operacionais'],
               'Matemática Discreta 2':['Sistema de Banco de Dados 1'],
               'Projeto Integrador 1':['Projeto Integrador 2'],
               'Interação Humano Computador':['Qualidade de Software'],
               'Requisitos de Software':['Arquitetura de Desenho de Software'],
               'Sistema de Banco de Dados 1':['Sistema de Banco de Dados 2'],
               'Fundamentos de Sistemas Operacionais':['Fundamentos de Redes de Computadores','Fundamentos de Sistemas Embarcados'],
               'Compiladores 1':['Paradigmas de Programação'],
               'Estrutura de Dados 2':['Programação para Sistemas Paralelos e Distribuídos'],
               'Qualidade de Software':[],
               'Testes de Software':['Técnicas de Programação em Plataformas Emergentes','Gerência de Configuração e Evolução de Software'],
               'Arquitetura de Desenho de Software':['Paradigmas de Programação'],
               'Fundamentos de Redes de Computadores':['Programação para Sistemas Paralelos e Distribuídos'],
               'Sistemas de Banco de Dados 2':[],
               'Projeto de Análise de Algoritmos':[],
               'Técnicas de Programação em Plataformas Emergentes':['Engenharia de Produto de Software'],
               'Paradigmas de Programação':[],
               'Fundamentos de Sistemas Embarcados':[],
               'Programação para Sistemas Paralelos e Distribuídos':[],
               'Optativa':[],
               'Optativa':[],
               'Engenharia de Produto de Software':['Projeto Integrador 2'],
               'Gerência de Configuração e Evolução de Software':[],
               'Optativa':[],
               'Estágio Supervisionado':[],
               'Optativa':[],
               'Optativa':[],
               'Optativa':[],
               'Trabalho de Conclusão de Curso 1':['Trabalho de Conclusão de Curso 2'],
               'Optativa':[],
               'Optativa':[],
               'Projeto Integrador 2':[],
               }



#grafo.printa_grafo()

root = tk.Tk()
root.title("Buscador de disciplinas de software")
titulo = tk.Label(root, text="Bem vindo ao buscador de matérias de Engenharia de Software", font=("Times New Roman", 20))
titulo.pack()


texto = "\n\nEste programa foi desenvolvido em Python e utiliza o algoritmo BFS (Busca em Largura) em um grafo de disciplinas do curso de Engenharia de Software. Cada disciplina é um vértice e as conexões entre as disciplinas são arestas. O objetivo é encontrar todos os pré-requisitos de uma disciplina especificada. O algoritmo BFS percorre o grafo em largura, visitando todos os vértices de mesma profundidade antes de ir para o próximo nível. Ele começa pela disciplina especificada (disciplina 1), adiciona todos os seus pré-requisitos à fila e visita todos os pré-requisitos adicionados à fila, adicionando os pré-requisitos desses pré-requisitos à fila e assim por diante. Esse processo continua até que todos os pré-requisitos tenham sido visitados. O resultado é a lista de todas as disciplinas que devem ser cursadas antes da disciplina especificada (Disciplina 2).\n\n"

texto_label = tk.Label(root, text=texto,justify="center", wraplength=600, font=("Times New Roman", 14))
texto_label.pack()

source_label = tk.Label(root, text="Digite a disciplina 1:", font=("Times New Roman", 14))
source_label.pack()
source_entry = tk.Entry(root)
source_entry.pack()

end_label = tk.Label(root, text="\nDigite a disciplina 2:", font=("Times New Roman", 14))
end_label.pack()
end_entry = tk.Entry(root)
end_entry.pack()

espaco = tk.Label(root, text="\n")
espaco.pack()

def bfs():
    source = source_entry.get()
    end = end_entry.get()
    path = grafo.bfs(source, end)
    if path == None:
        janela = tk.Toplevel(root)
        janela.geometry("100x50")
        Caminho_label = tk.Label(janela, text=f"Caminho não existente")
        Caminho_label.pack()
    else:
        janela = tk.Toplevel(root)
        janela.geometry("900x50")
        caminho = " -> ".join(path)
        Caminho_label = tk.Label(janela, text=f"Caminho: {caminho}")
        Caminho_label.pack()
        

bfs_button = tk.Button(root, text="Mostrar caminho de 1 para 2", command=bfs )

root.geometry("900x600")

bfs_button.pack()
root.mainloop()

