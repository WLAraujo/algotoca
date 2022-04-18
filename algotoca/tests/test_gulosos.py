import igraph
import sys
import os
import pytest
from grafos_aleatorios import gerar_grafo, coloracao_viavel
sys.path.insert(0,f'{os.getenv("HOME")}/algotoca/algotoca/algotoca/grafos/coloracao')
from gulosos import Gulosos

@pytest.mark.parametrize(
    "vertices, arestas, cores",
    [
        (3, [(0,1),(1,2),(2,0)], 3), # Triângulo
        (6, [(0,1),(0,2),(0,3),(0,4),(0,5)], 2), # Estrela
        (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], 4), # K4
        (5, [(0,1), (1,2), (2,3), (3,4), (4,0)], 3) # Ciclo ímpar
    ]
)
def test_guloso_teo(vertices, arestas, cores):
    """
    Testes da função que implementa o algoritmo heurístico 
    guloso com base em teoremas da literatura. A quantidade de cores 
    é exata.
    """
    algoritmos_gulosos = Gulosos()
    G = igraph.Graph()
    G.add_vertices(vertices)
    G.add_edges(arestas)
    coloracao_guloso = algoritmos_gulosos.guloso(G).vs["cor"]
    assert len(set(coloracao_guloso)) == cores

@pytest.mark.parametrize(
    "vertices, arestas, cores",
    [
        (3, [(0,1),(1,2),(2,0)], 3), # Triângulo
        (6, [(0,1),(0,2),(0,3),(0,4),(0,5)], 2), # Estrela
        (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], 4), # K4
        (6, [(0,3), (0,4), (1,4), (1,5), (2,5)], 2), # Bipartido
        (5, [(0,1), (1,2), (2,3), (3,4), (4,0)], 3) # Ciclo ímpar
    ]
)
def test_dsatur_teo(vertices, arestas, cores):
    """
    Testes da função que implementa o algoritmo heurístico 
    dsatur com base em teoremas da literatura. A quantidade de cores 
    é exata.
    """
    algoritmos_gulosos = Gulosos()
    G = igraph.Graph()
    G.add_vertices(vertices)
    G.add_edges(arestas)
    coloracao_guloso = algoritmos_gulosos.dsatur(G).vs["cor"]
    assert len(set(coloracao_guloso)) == cores

@pytest.mark.parametrize(
    "vertices, arestas, cores",
    [
        (3, [(0,1),(1,2),(2,0)], 3), # Triângulo
        (6, [(0,1),(0,2),(0,3),(0,4),(0,5)], 2), # Estrela
        (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], 4), # K4
        (5, [(0,1), (1,2), (2,3), (3,4), (4,0)], 3) # Ciclo ímpar
    ]
)
def test_rlf_teo(vertices, arestas, cores):
    """
    Testes da função que implementa o algoritmo heurístico 
    rlf com base em teoremas da literatura. A quantidade de cores 
    é exata.
    """
    algoritmos_gulosos = Gulosos()
    G = igraph.Graph()
    G.add_vertices(vertices)
    G.add_edges(arestas)
    coloracao_guloso = algoritmos_gulosos.rlf(G).vs["cor"]
    assert len(set(coloracao_guloso)) == cores

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        gerar_grafo() for n_grafo in range(100)
    ]
)
def test_guloso_rand(grafo_gerado):
    """
    Testes da função que implementa o algoritmo heurístico 
    guloso para 100 grafos aleatórios. O teste verifica se a cor 
    dos vizinhos de cada vértice é diferentes, ou seja, verifica se
    a coloração devolvida é viável.
    """
    algoritmos_gulosos = Gulosos()
    coloracao_guloso = algoritmos_gulosos.guloso(grafo_gerado)
    coloracao_viavel(coloracao_guloso)

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        gerar_grafo() for n_grafo in range(100)
    ]
)
def test_dsatur_rand(grafo_gerado):
    """
    Testes da função que implementa o algoritmo heurístico 
    dsatur para 100 grafos aleatórios. O teste verifica se a cor 
    dos vizinhos de cada vértice é diferentes, ou seja, verifica se
    a coloração devolvida é viável.
    """
    algoritmos_gulosos = Gulosos()
    coloracao_guloso = algoritmos_gulosos.dsatur(grafo_gerado)
    coloracao_viavel(coloracao_guloso)

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        gerar_grafo() for n_grafo in range(100)
    ]
)
def test_rlf_rand(grafo_gerado):
    """
    Testes da função que implementa o algoritmo heurístico 
    rlf para 100 grafos aleatórios. O teste verifica se a cor 
    dos vizinhos de cada vértice é diferentes, ou seja, verifica se
    a coloração devolvida é viável.
    """
    algoritmos_gulosos = Gulosos()
    coloracao_guloso = algoritmos_gulosos.rlf(grafo_gerado)
    coloracao_viavel(coloracao_guloso)