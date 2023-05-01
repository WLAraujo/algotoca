import igraph
import pytest
import random

def gerar_grafo(min = 15, max = 50):
    grafo = igraph.Graph()
    n = random.randint(min,max)
    return grafo.Erdos_Renyi(n, p=0.7)

def coloracao_viavel(grafo_colorido):
    lista_adj = grafo_colorido.get_adjlist()
    for vertice in range(grafo_colorido.vcount()):
        for vizinho in lista_adj[vertice]:
            assert grafo_colorido.vs[vertice]["cor"] != grafo_colorido.vs[vizinho]["cor"]