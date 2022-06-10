import igraph
import random
import numpy as np
from algotoca.grafos.coloracao.gulosos import Gulosos

class Metaheuristicas:
    """
    Classe com funções que executam algoritmos de coloração que usam metaheurísticas.
    """

    def tabucol(grafo, solucao_inicial=None, tabu=5, iteracoes_min=20, iteracoes_max=50, cores_max = None):
        """
        Função usada para devolver uma coloração do grafo passado como parâmetro
        usando o algoritmo Coloração Tabu. A função realiza uma exploração do espaço de soluções
        impróprio e devolve a primeira melhor solução viável encontrada. Caso não seja encontrada solução
        viável com os parâmetros passados será retornada uma mensagem indicando isso e o grafo com 
        uma coloração imprópria. 

        Parameters:
        grafo (igraph.Graph): Objeto grafo do pacote igraph
        solucao_inicial (list): Lista de inteiros que deve possuir uma coloração inicial do grafo passado.
                                Caso não seja passado uma solução aleatória será construída.
        tabu (int): Valor tabu, quantidade de iterações que um movimento permanecerá na lista tabu. O valor
                    padrão é 5.
        iteracoes_min (int): Número mínimo de iterações que o algoritmo deve realizar antes da solução ser devolvida.
        iteracoes_max (int): Número mínimo de iterações que o algoritmo pode realizar antes da solução ser devolvida.
        cores_max (int): Número de cores máximo que deve ser considerado durante a construção da solução. Caso não seja
                         passado um valor, será usada a quantidade de vértices do grafo.
    
        Returns:
        igraph.Graph: Retorna o mesmo grafo, porém, com adição da label "cor",
        para acessá-la use grafo.vs["cor"]
        """

        if isinstance(grafo, igraph.Graph) is False:
            raise Exception("O grafo passado como parâmetro deve pertencer à classe igraph.Graph.")

        if cores_max == None:
            cores_max = grafo.vcount()
        else:
            if isinstance(cores_max, int) is False:
                raise("O parâmetro cores_max deve ser um int.") 

        def criar_solucao_inicial(grafo):
            """
            Função usada para criar uma solução inicial caso essa não seja passada na chamada da função TabuCol.
            Por ser um algoritmo que trabalha no espaço de soluções impróprias, a solução gerada aqui é totalmente
            feita de forma aleatória.
            """
            for vertice in range(grafo.vcount()):
                cor_aleatoria = random.choice(list(range(cores_max)))
                grafo.vs[vertice]["cor"] = cor_aleatoria
            return grafo
        
        if solucao_inicial == None:
            grafo = criar_solucao_inicial(grafo)
        else:
            if isinstance(solucao_inicial, list) is False:
                raise Exception("A solução inicial passada deve estar no formato de uma lista de inteiros com tamanho igual à quantidade de vértices do grafo.")
            if len(solucao_inicial) != grafo.vcount():
                raise Exception("O tamanho da lista de solução inicial deve ser igual à quantidade de vértices do grafo.")
            if all([isinstance(cor, int) for cor in solucao_inicial]) is False:
                raise Exception("Todos os elementos da solução inicial passada devem ser inteiros.")
            if max(solucao_inicial) > grafo.vcount():
                raise Exception("Na solução inicial passada não deve ter um inteiro maior que a quantidade de vértices do grafo.")
            cores_max = len(set(solucao_inicial))
            grafo.vs["cor"] = solucao_inicial

        lista_cores = list(range(cores_max))

        lista_tabu = np.zeros((grafo.vcount(), len(lista_cores)))

        def cria_lista_auxiliar(grafo):
            """
            Função que cria e atualiza a lista auxiliar usada no algoritmo de Coloração Tabu.
            Essa lista mantém a referência de quantos vértices de uma cor X são vizinhos de um vértice Y.
            """
            lista_auxiliar = np.zeros((grafo.vcount(), len(lista_cores)))
            lista_arestas = grafo.get_edgelist()
            for v_1, v_2 in lista_arestas:
                lista_auxiliar[v_1][grafo.vs[v_2]["cor"]] += 1
                lista_auxiliar[v_2][grafo.vs[v_1]["cor"]] += 1
            return lista_auxiliar
        lista_auxiliar = cria_lista_auxiliar(grafo)

        def cria_lista_colisoes(grafo):
            """
            Função que devolve uma lista com as colisões no grafo. Cada elemento da lista é uma 
            tupla com a aresta causadora da colisão.
            """
            lista_arestas = grafo.get_edgelist()
            colisoes = []
            for v_1, v_2 in lista_arestas:
                if grafo.vs[v_1]["cor"]==grafo.vs[v_2]["cor"]:
                    colisoes.append((v_1,v_2))
            return colisoes        
        lista_colisoes = cria_lista_colisoes(grafo)

        def movimento(grafo, lista_cores, lista_tabu, lista_auxiliar, lista_colisoes, tabu, iteracao):
            """
            Função que realiza um movimento de exploração dentro do algoritmo de Coloração Tabu.
            A função envolve selecionar um vértice para explorar soluções vizinhas relacionadas à troca de cor desse vértice,
            calcular o custo de cada movimento e verificar qual o próximo movimento.
            """
            if not lista_colisoes:
                vertice_selecionado = random.choice(list(range(grafo.vcount())))
            else:
                vertice_selecionado = random.choice(list(random.choice(lista_colisoes)))
            cor_inicial = grafo.vs[vertice_selecionado]["cor"]

            melhor_colisoes = len(lista_colisoes)
            cor_movimento = cor_inicial
            for cor in lista_cores:
                if cor != cor_inicial and lista_tabu[vertice_selecionado][cor] <= iteracao:
                    grafo.vs[vertice_selecionado]["cor"] = cor
                    colisoes = len(lista_colisoes) + lista_auxiliar[vertice_selecionado][cor] - lista_auxiliar[vertice_selecionado][cor_inicial]
                    if colisoes <= melhor_colisoes:
                        melhor_colisoes = colisoes
                        cor_movimento = cor
            if cor_movimento == cor_inicial:
                cor_movimento = random.choice(lista_cores)
            lista_tabu[vertice_selecionado][cor_inicial] = tabu + iteracao
            grafo.vs[vertice_selecionado]["cor"] = cor_movimento
            return grafo, lista_tabu

        iteracoes = 1
        melhor_coloracao = grafo.vcount()
        melhor_grafo = grafo
        if isinstance(iteracoes_min, int) is False:
            raise("O número de iterações mínimo deve ser um inteiro.")
        while(len(lista_colisoes) > 0 or iteracoes < iteracoes_min):
            if iteracoes > iteracoes_max:
                break
            grafo, lista_tabu = movimento(grafo, lista_cores, lista_tabu, lista_auxiliar, lista_colisoes, tabu, iteracoes)
            iteracoes += 1
            lista_colisoes = cria_lista_colisoes(grafo)
            lista_auxiliar = cria_lista_auxiliar(grafo)
            if len(set(grafo.vs["cor"])) < melhor_coloracao and len(lista_colisoes) == 0:
                melhor_coloracao = len(set(grafo.vs["cor"]))
                melhor_grafo = grafo

        if len(lista_colisoes) > 0:
            print("Não foi possível encontrar solução viável com os parâmetros passados.")      

        return melhor_grafo

    def hill_climbing(grafo):
        """
        Função usada para devolver uma coloração do grafo passado como parâmetro
        usando o algoritmo Hill Climbing.

        Parameters:
        grafo (igraph.Graph): Objeto grafo do pacote igraph
    
        Returns:
        igraph.Graph: Retorna o mesmo grafo, porém, com adição da label "cor",
        para acessá-la use grafo.vs["cor"]
        """
        grafo_sol_inicial = Gulosos().dsatur(grafo)

        qtd_cores = len(set(grafo_sol_inicial))

        tabela_viabilidade = np.zeros((grafo.vcount(), qtd_cores))
        lista_auxiliar = np.zeros((grafo.vcount(), qtd_cores))
        lista_arestas = grafo.get_edgelist()
        for v_1, v_2 in lista_arestas:
            lista_auxiliar[v_1][grafo.vs[v_2]["cor"]] += 1
            lista_auxiliar[v_2][grafo.vs[v_1]["cor"]] += 1
        lista_auxiliar[lista_auxiliar < 0] = -1
        lista_auxiliar[lista_auxiliar == 0] = 1 
        
        
        


        
