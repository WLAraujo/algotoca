import igraph
import sys
import os
import pytest
from grafos_aleatorios import gerar_grafo, coloracao_viavel
sys.path.insert(0,f'{os.getenv("HOME")}/algotoca/algotoca/algotoca/grafos/coloracao')
from gulosos import Gulosos

gus = Gulosos()

grafo = igraph.Graph()

grafo.add_vertices(6)
grafo.add_edges([(0,3),(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)])

grafo = gus.dsatur(grafo, 1)

print(grafo.vs["cor"])