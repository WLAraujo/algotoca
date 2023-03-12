import igraph
import sys
import os
import pytest
from graphcol.exatos import Exatos
import random

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        igraph.Graph().Erdos_Renyi(random.randint(5,15), p=random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])) for n_grafo in range(100)
    ]
)
def test_lawler(grafo_gerado):
    """
    Testes da função que implementa o algoritmo exato de Lawler
    para 100 grafos aleatórios. .
    """
    pass