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

@pytest.mark.parametrize(
    "vertices, arestas, cores, ordem",
    [
        (6, [(0,3),(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)], 3, [0,1,2,3,4,5]),
        (10, [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,4),(3,4),(3,7),(4,6),
            (4,7),(4,8),(5,7),(6,7),(6,9),(7,8),(8,9)], 4, 
            [4,5,6,0,1,2,9,3,7,8]),
        (20, [(0,1),(0,6),(1,5),(1,6),(1,7),(2,3),(2,6),(2,7),(3,4),(3,7),(3,8),
            (4,8),(5,6),(5,10),(5,15),(6,7),(6,11),(7,8),(7,11),(7,12),(8,9),(8,13),
            (8,14),(9,13),(10,11),(11,12),(11,15),(12,13),(12,16),(12,17),(13,17),
            (13,18),(14,18),(14,19),(15,16),(17,18)], 5, 
            [15,13,2,0,6,7,8,5,4,9,19,18,10,1,16,3,11,14,17,12]),
        (6, [(0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5)], 3, [0,1,2,3,4,5]),
        (6, [(0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5)], 4, [0,1,5,4,3,2]),
        (7, [(0,1),(0,2),(0,3),(0,5),(0,6),(1,2),(1,5),(1,6),(2,3),(2,4),(2,5),(3,4),
            (3,5),(3,6),(4,5),(5,6)], 5, [5,3,4,6,1,0,2]),
        (7, [(0,1),(0,2),(0,3),(0,5),(0,6),(1,2),(1,5),(1,6),(2,3),(2,4),(2,5),(3,4),
            (3,5),(3,6),(4,5),(5,6)], 4, [0,1,2,3,4,5,6])
    ]
)
def test_guloso_ordem(vertices, arestas, cores, ordem):
    """
    Testes da função que implementa o algoritmo heurístico 
    guloso passando uma ordem pré-definida dos vértices a serem coloridos.
    Como a ordem de coloração é conhecida previamente a quantidade de
    cores usadas também é.
    """
    algoritmos_gulosos = Gulosos()
    G = igraph.Graph()
    G.add_vertices(vertices)
    G.add_edges(arestas)
    coloracao_guloso = algoritmos_gulosos.guloso(G, ordem).vs["cor"]
    assert len(set(coloracao_guloso)) == cores