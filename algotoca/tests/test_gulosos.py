import igraph
import sys
import os
sys.path.insert(0,f'{os.getenv("HOME")}/algotoca/algotoca/algotoca/grafos/coloracao')
from gulosos import Gulosos

def teste_triangulo():
    """Testando se os algoritmos devolvem uma coloração de tamanho 3 para um triângulo."""
    G = igraph.Graph()
    G.add_vertices(3)
    G.add_edges([(0,1),(1,2),(2,0)])
    algoritmos_gulosos = Gulosos()
    coloracao_guloso = algoritmos_gulosos.guloso(G).vs["cor"]
    coloracao_dsatur = algoritmos_gulosos.dsatur(G).vs["cor"]
    coloracao_rlf = algoritmos_gulosos.rlf(G).vs["cor"]
    assert len(set(coloracao_guloso)) == 3
    assert len(set(coloracao_dsatur)) == 3
    assert len(set(coloracao_rlf)) == 3

def teste_estrela():
    """Testando se os algoritmos devolvem uma coloração de tamanho 2 para uma estrela de 5 pontas."""
    G = igraph.Graph()
    G.add_vertices(6)
    G.add_edges([(0,1),(0,2),(0,3),(0,4),(0,5)])
    algoritmos_gulosos = Gulosos()
    coloracao_guloso = algoritmos_gulosos.guloso(G).vs["cor"]
    coloracao_dsatur = algoritmos_gulosos.dsatur(G).vs["cor"]
    coloracao_rlf = algoritmos_gulosos.rlf(G).vs["cor"]
    assert len(set(coloracao_guloso)) == 2
    assert len(set(coloracao_dsatur)) == 2
    assert len(set(coloracao_rlf)) == 2

def teste_completo_5():
    """Testando se os algoritmos devolvem uma coloração de tamanho 5 para um grafo completo de 5 vértices."""
    G = igraph.Graph()
    G.add_vertices(5) 
    arestas = []
    for vertice_1 in range(5):
        for vertice_2 in range(vertice_1+1, 5):
            arestas.append((vertice_1, vertice_2))
    G.add_edges(arestas)
    algoritmos_gulosos = Gulosos()
    coloracao_guloso = algoritmos_gulosos.guloso(G).vs["cor"]
    coloracao_dsatur = algoritmos_gulosos.dsatur(G).vs["cor"]
    coloracao_rlf = algoritmos_gulosos.rlf(G).vs["cor"]
    assert len(set(coloracao_guloso)) == 5
    assert len(set(coloracao_dsatur)) == 5
    assert len(set(coloracao_rlf)) == 5

def teste_bipartido():
    """Testando se os algoritmos devolvem uma coloração de tamanho 2 para um grafo bipartido 3x3."""
    G = igraph.Graph()
    G.add_vertices(6) 
    arestas = [(0,3), (0,4), (1,4), (1,5), (2,5)]
    G.add_edges(arestas)
    algoritmos_gulosos = Gulosos()
    coloracao_dsatur = algoritmos_gulosos.dsatur(G).vs["cor"]
    #coloracao_rlf = algoritmos_gulosos.rlf(G).vs["cor"]
    assert len(set(coloracao_dsatur)) == 2
    #assert len(set(coloracao_rlf)) == 2

def teste_ciclo_impar():
    "Testando se os algoritmos devolvem uma coloração de tamanho 3 para um ciclo ímpar"
    G = igraph.Graph()
    G.add_vertices(5) 
    arestas = [(0,1), (1,2), (2,3), (3,4), (4,0)]
    G.add_edges(arestas)
    algoritmos_gulosos = Gulosos()
    coloracao_guloso = algoritmos_gulosos.guloso(G).vs["cor"]
    coloracao_dsatur = algoritmos_gulosos.dsatur(G).vs["cor"]
    coloracao_rlf = algoritmos_gulosos.rlf(G).vs["cor"]
    assert len(set(coloracao_guloso)) == 3
    assert len(set(coloracao_dsatur)) == 3
    assert len(set(coloracao_rlf)) == 3

def testes_gulosos():
    teste_triangulo()
    teste_estrela()
    teste_completo_5()
    teste_bipartido()
    teste_ciclo_impar()

