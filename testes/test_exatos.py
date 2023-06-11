import igraph
import sys
import os
import pytest
from graphcol.exatos import Exatos
from graphcol.exatos import Gulosos
from grafos_aleatorios import gerar_grafo, coloracao_viavel
import random
from itertools import chain, combinations

@pytest.mark.parametrize(
  "grafo_gerado",
  [
      gerar_grafo(6,10) for n_grafo in range(50)
  ]
)
def test_dsatur_exato_viabilidade(capfd, grafo_gerado):
  """
  Testes da função que implementa o algoritmo Dsatur Exato.
  Trata-se de um algoritmo exato de devolve o número cromático de um grafo.
  Nesse teste avaliamos se para cada resposta de 100 grafos aleatórios se
  a coloração devolvida é viável.
  """
  algoritmos_exatos = Exatos
  coloracao_dsatur_exato = algoritmos_exatos.dsatur_exato(grafo_gerado)
  coloracao_viavel(coloracao_dsatur_exato)

@pytest.mark.parametrize(
  "grafo_gerado",
  [
      gerar_grafo(6,10) for n_grafo in range(50)
  ]
)
def test_exatos_igualdade(capfd, grafo_gerado):
  """
  Testes que vão comparar o resultado obtido pelo algoritmo de Lawler e
  o algoritmo Dsatur Exato, pois como ambos são exatos devem chegar ao mesmo
  valor de número cromático
  """
  algoritmos_exatos = Exatos
  coloracao_dsatur_exato = algoritmos_exatos.dsatur_exato(grafo_gerado)
  num_cromatico = algoritmos_exatos.cromatico_lawler(grafo_gerado)
  assert num_cromatico == len(set(coloracao_dsatur_exato.vs['cor']))

@pytest.mark.parametrize(
  "vertices, arestas, resultado",
  [
      (9, [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(5,6),(5,7),(5,8),(6,7),(6,8),(7,8)], 5),
      (7, [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(3,4)], 3),
      (6, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(1,5),(2,5),(2,4),(3,4)], 4),
      (9, [(0,4),(0,6),(1,2),(1,3),(2,4),(3,4),(3,5),(4,6),(5,6),(5,7),(6,8),(7,8)], 3),
      (7, [(0,1),(0,2),(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,6),(4,5),(4,6)], 4)
  ]
)
def test_grafos_conhecidos(capfd, vertices, arestas, resultado):
  """
  Testes que usam grafos com resultado ótimo já conhecido, como estamos
  testando algoritmos exatos então o número cromático e a quantidade de cores
  usadas em colorações deve ser igual
  """
  algoritmos_exatos = Exatos
  G = igraph.Graph()
  G.add_vertices(vertices)
  G.add_edges(arestas)
  coloracao_dsatur_exato = algoritmos_exatos.dsatur_exato(G)
  num_cromatico = algoritmos_exatos.cromatico_lawler(G)
  assert num_cromatico == resultado
  assert len(set(coloracao_dsatur_exato.vs['cor'])) == resultado

@pytest.mark.parametrize(
  "grafo_gerado",
  [
      gerar_grafo(6,10) for n_grafo in range(50)
  ]
)
def test_compara_algoritmos(capfd, grafo_gerado):
  """
  Testes que comparam resultados de algoritmos gulosos com os resultados de 
  algoritmos exatos, pois os resultados dos exatos devem sempre ser menores ou
  iguais ao dos gulosos
  """
  algoritmos_exatos = Exatos
  algoritmos_gulosos = Gulosos
  coloracao_dsatur_exato = algoritmos_exatos.dsatur_exato(grafo_gerado)
  num_cromatico = algoritmos_exatos.cromatico_lawler(grafo_gerado)

  coloracao_guloso = algoritmos_gulosos.guloso(grafo_gerado)
  assert num_cromatico <= len(set(coloracao_guloso.vs['cor']))
  assert len(set(coloracao_dsatur_exato.vs['cor'])) <= len(set(coloracao_guloso.vs['cor']))

  coloracao_rlf = algoritmos_gulosos.rlf(grafo_gerado)
  assert num_cromatico <= len(set(coloracao_rlf.vs['cor']))
  assert len(set(coloracao_dsatur_exato.vs['cor'])) <= len(set(coloracao_rlf.vs['cor']))

  coloracao_dsatur = algoritmos_gulosos.dsatur(grafo_gerado)
  assert num_cromatico <= len(set(coloracao_dsatur.vs['cor']))
  assert len(set(coloracao_dsatur_exato.vs['cor'])) <= len(set(coloracao_dsatur.vs['cor']))

