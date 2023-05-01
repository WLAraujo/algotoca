import igraph as ig
import random
import numpy as np
import math
import collections
from itertools import chain, combinations
from graphcol.gulosos import Gulosos

class Exatos:

  """
  Classe que contém a implementação dos algoritmos exatos para coloração de grafos,
  """
    
  def cromatico_lawler(grafo):
    """
    Função que devolve o número cromático de um grafo. Como se trata de uma função de devolve o valor
    exato deve ser usada com cautela, pois para instâncias a partir de 10 vértices já é possível que
    o tempo de exeução da função ultrapasse 10 minutos. Por isso recomendamos uso em pequenas instâncias
    """

    def powerset(iterable):
      s = list(iterable)
      return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    n_vertices = grafo.vcount()
    lista_subgrafos = list(powerset(range(n_vertices)))
    X = dict.fromkeys(lista_subgrafos)
    unitarios = [subgrafo for subgrafo in lista_subgrafos if len(subgrafo) == 1]
    arestas_grafo = grafo.get_edgelist()
    X[()] = 0
    for subgrafo in unitarios:
      X[subgrafo] = 1
    for subgrafo in lista_subgrafos:
      if X[subgrafo] is None:
        X[subgrafo] = n_vertices
        vertices_subgrafo = list(subgrafo)
        arestas_subgrafo = [(x,y) for (x,y) in arestas_grafo if (x in vertices_subgrafo) and (y in vertices_subgrafo)]
        conjuntos_independentes_maximais = ig.Graph(arestas_grafo).induced_subgraph(vertices_subgrafo).maximal_independent_vertex_sets()
        if conjuntos_independentes_maximais == [()]:
          X[subgrafo] = 1
        for conjunto_independente_maximal in conjuntos_independentes_maximais:
          conjunto_ajustado = [vertices_subgrafo[i] for i in list(conjunto_independente_maximal)]
          vertices_limpos = set(subgrafo) - set(conjunto_ajustado)
          X[subgrafo] = min(X[subgrafo], X[tuple(sorted(vertices_limpos))] + 1)
          
    return X[lista_subgrafos[(2**n_vertices)-1]]

def dsatur_exato(grafo):
  """
  Função usada como interface do algoritmo dsatur exato, usada na
  primeira que começa a recursão que implementa o backtracking. A coisa
  mais importante que essa função faz é criar um primeira solução do dsatur 
  """
  numero_vertices = grafo.vcount()
  lista_adjacencias = grafo.get_adjlist()
  lista_arestas = grafo.get_edgelist()
  primeira_coloracao = Gulosos.dsatur(grafo).vs["cor"]
  melhor_resultado = len(set(primeira_coloracao))

  def dsatur_recursao(grafo, melhor_geral, coloracao = [], vertices_coloridos = []):
    """
    Função usada nas chamadas recursivas do Dsatur exato, funcionando como o
    backtracking do algoritmo
    """

    if vertices_coloridos == []:
      vertices_coloridos = numero_vertices * [0]

    melhor = melhor_geral
    melhor_grafo = grafo.copy()
    coloracao_original = coloracao.copy()
    vertices_coloridos_original = vertices_coloridos.copy()
    vertices_n_coloridos = vertices_coloridos.count(0)
    vertices_tentados = []
    tentativas_coloracao = 0

    while tentativas_coloracao < vertices_n_coloridos:

      vertices_coloridos = vertices_coloridos_original.copy()
      coloracao = coloracao_original.copy()

      if coloracao == []:
        vertices_coloridos = numero_vertices * [0]
        vertices_coloridos_auxiliar = vertices_coloridos
        grau_saturacao = FuncAux.atualiza_grau_sat(lista_adjacencias, vertices_coloridos)
        vertice_maior_grau = FuncAux.seleciona_vertice_dsatur(grau_saturacao, vertices_coloridos)
        cor = {vertice_maior_grau}
        coloracao = [cor]
        vertices_coloridos[vertice_maior_grau] = 1
        grafo.vs[vertice_maior_grau]['cor'] = coloracao.index(cor)
      else:
        grau_saturacao = FuncAux.atualiza_grau_sat(lista_adjacencias, vertices_coloridos)
        vertice_maior_grau = FuncAux.seleciona_vertice_dsatur(grau_saturacao, vertices_coloridos, vertices_tentados)
        for cor in coloracao:
          if FuncAux.conjunto_independente(lista_arestas, cor.union({vertice_maior_grau})):
            cor.add(vertice_maior_grau)
            grafo.vs[vertice_maior_grau]['cor'] = coloracao.index(cor)
            vertices_coloridos[vertice_maior_grau] = 1
            break
        if vertices_coloridos[vertice_maior_grau] == 0:
          cor = {vertice_maior_grau}
          coloracao.append(cor)
          grafo.vs[vertice_maior_grau]['cor'] = coloracao.index(cor)
          vertices_coloridos[vertice_maior_grau] = 1

      qntd_cores = len(coloracao)

      if vertices_coloridos.count(1) < numero_vertices and qntd_cores < melhor_geral:
        melhor, grafo = dsatur_recursao(grafo, melhor_geral, coloracao, vertices_coloridos)
        vertices_tentados.append(vertice_maior_grau)
        tentativas_coloracao = tentativas_coloracao+1
        if melhor < melhor_geral:
          melhor_geral = melhor
          melhor_grafo = grafo.copy()
        continue

      if vertices_coloridos.count(1) == numero_vertices and qntd_cores < melhor_geral:
        melhor_geral = qntd_cores
        melhor_grafo = grafo.copy()
        return melhor_geral, melhor_grafo

      if qntd_cores >= melhor:
        vertices_tentados.append(vertice_maior_grau)
        tentativas_coloracao = tentativas_coloracao+1
        continue

    return melhor_geral, melhor_grafo

  melhor, grafo = dsatur_recursao(grafo, melhor_resultado)

  return grafo

class FuncAux:
  '''
  Classe que contém funções auxiliares usadas pelos algoritmos gulosos.
  '''
  def conjunto_independente(lista_arestas, subconjunto_vertices):
    '''
    Função que pega a lista de arestas de um grafo e um subconjunto de seus vértices e
      verifica se esse subconjunto é conjunto independente de vértices.
    
    Parameters:
    lista_arestas (list): Lista das arestas do grafo, cada aresta
      deve ser representada por uma tupla
    subconjunto_vertices (list): Subconjunto de vértices do grafo original
      qual deseja-se saber se o subconjunto de vértices passado forma
      ou não conjunto independente

    Returns:
    resultado: Retorna True se o subconjunto é independente,
      retorna False se não for
    '''
    for vertice_a in subconjunto_vertices:
        for vertice_b in subconjunto_vertices:
            if ((vertice_a, vertice_b) or (vertice_b, vertice_a)) in lista_arestas:
                return False
    return True

  def atualiza_grau_sat(lista_adjacencias, vertices_coloridos):
    ''' 
    Função que devolve uma lista de grau de saturação, usada durante a execução do algoritmo DSatur.

    Parameters:
    lista_arestas (list): Lista das listas de adjacências de cada vértice.
    cores_vertice (list) : Lista com os vértices que já foram coloridos.

    Returns:
    list: Devolve a lista com o grau de saturação de cada vértice.
    '''
    grau_saturacao = len(vertices_coloridos) * [0]
    for vertice in range(len(vertices_coloridos)):
        for vertice_adjacente in lista_adjacencias[vertice]:
            if vertices_coloridos[vertice_adjacente] != 0:
                grau_saturacao[vertice] += 1
    return grau_saturacao

  def seleciona_vertice_dsatur(grau_saturacao, vertices_coloridos, vertices_tentados = []):
    ''' 
    Função que recebe uma lista com o grau de saturação de todos os
      vértices de um grafo e devolve o vértice com maior grau de saturação.
    Caso haja mais de um vértice com maior grau de saturação o vértice devolvido
      é aletaório entre esses vértices de maior grau.

    Parameters:
    grau_saturacao (list): Lista com os graus de saturação de cada vértice.
    vertices_tentados (list): Vértices que no nó atual já tentou-se colorir

    Returns:
    int: Devolve inteiro que indica qual vértice ainda não colorido o com maior grau de saturação no grafo.
    '''
    vertices_n_coloridos_grau_max = []
    grau_max = 0
    for vertice in range(len(vertices_coloridos)):
      if vertice not in vertices_tentados and vertices_coloridos[vertice] == 0:
            if grau_saturacao[vertice] == grau_max:
                vertices_n_coloridos_grau_max.append(vertice)
            elif grau_saturacao[vertice] > grau_max:
                vertices_n_coloridos_grau_max.clear()
                vertices_n_coloridos_grau_max.append(vertice)
                grau_max = grau_saturacao[vertice]
    vertice_escolhido = random.choice(vertices_n_coloridos_grau_max)
    return vertice_escolhido