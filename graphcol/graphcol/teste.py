from metaheuristicas import Metaheuristicas
import igraph

G = igraph.Graph()
G.add_vertices(6)
G.add_edges([(0,1),(0,2),(0,3),(0,4),(0,5)])

G = Metaheuristicas.evolucionario(G)

print(G.vs["cor"])



