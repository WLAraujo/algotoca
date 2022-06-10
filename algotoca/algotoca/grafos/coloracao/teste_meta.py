from metaheuristicas import Metaheuristicas
import igraph
import numpy as np

grafo = igraph.Graph(6)
grafo.add_edges([(0,1),(0,2),(0,3),(0,4),(0,5),(1,5),(2,3)])

col_tabu = Metaheuristicas.tabucol(grafo, cores_max=3)

print(col_tabu.vs["cor"])

print(grafo.get_adjlist())

