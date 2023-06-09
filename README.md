
# Buscador de disciplinas FGA

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0032821  |  Lorenzo de Lima Alves dos Santos |
| 19/0124989  |  Amanda Fernandes custodio |

## Sobre 
Este trabalho tem como objetivo traçar disciplinas do curso de Engenharia de Software da Universidade de Brasília, com intuito de facilitar a visualização das matérias em sua grade, mantendo organização e clareza em cada requisitos que cada matéria possui dentro do curso de Engenharia de Software.

## Objetivos 

-  Traçar rotas entres matérias, mostrando pré requisitos para cada um.<br>
-  Mostrar com clareza as matérias a serem concluídas e as que ainda não foram concluídas dentro do curso. <br>
-  Demonstrar a sequência de matéria a ser realizada a partir de uma matéria finalizada.<br>

## Screenshots
<p align="center">
 <img src= assets/BuscadorMaterias.jpg alt="Buscador de disciplinas FGA"/>  <br> <br>
 <img src= assets/ListaMaterias.jpg alt="Buscador de disciplinas FGA"/>  <br> <br>
 <img src= assets/CaminhoNaoExiste.jpeg alt="Buscador de disciplinas FGA"/>  <br> <br> <br>
</p>

## Instalação 
**Linguagem**: Python 3<br>

É necessária a instalação da linguagem python 3 em sua máquina para que o projeto funcione perfeitamente, assim como uma IDE de sua preferência (VS Code é o melhor recomendado).

## Uso 
Essa aplicação tem como principal objetivo mostrar os pré-requisitos para a matéria solicitada como disciplina específica(disciplina 1) e assim, através de uma Busca em largura, vai adicionando todos os pré-requisistos em uma fila, logo após visitar todos os pré requisitos, retorna uma lista de todas as matérias que precisam ser finalizadas até a disciplina seguinte(disciplina 2).
