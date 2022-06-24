from metaheuristicas import Metaheuristicas
import igraph
import numpy as np
import random

def coloracao_viavel(grafo_colorido):
    lista_adj = grafo_colorido.get_adjlist()
    for vertice in range(grafo_colorido.vcount()):
        for vizinho in lista_adj[vertice]:
            assert grafo_colorido.vs[vertice]["cor"] != grafo_colorido.vs[vizinho]["cor"]

def gerar_grafo():
    grafo = igraph.Graph()
    n = random.randint(20,100)
    return grafo.Barabasi(n)

for i in range(200):
    grafo = gerar_grafo()
    col_tabu = Metaheuristicas.tabucol(grafo, cores_max=3)
    #print(coloracao_viavel(col_tabu))
    #print(col_tabu.vs["cor"])

