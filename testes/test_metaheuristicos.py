import igraph
import sys
import os
import pytest
import random
from grafos_aleatorios import gerar_grafo, coloracao_viavel
from graphcol import gulosos
from graphcol.metaheuristicas import Metaheuristicas

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        gerar_grafo() for n_grafo in range(100)
        
    ]
)
def test_tabucol(capfd, grafo_gerado):
    """
    Testes da função que implementa o algoritmo metaheurístico 
    coloração tabu para 100 grafos aleatórios. O teste verifica duas possibilidades,
    se a coloração devolvida é inviável através da mensagem de erro da função e, 
    caso não seja inviável, verifica se é viável
    """
    algoritmos_metaheuristicos = Metaheuristicas
    cores_max = random.choice(list(range(5,20)))
    coloracao_metaheuristicos = algoritmos_metaheuristicos.tabucol(grafo_gerado, cores_max=cores_max)
    saida_terminal, erro = capfd.readouterr()
    try:
        coloracao_inviavel = saida_terminal == "Não foi possível encontrar solução viável com os parâmetros passados.\n"
        assert coloracao_inviavel
    except:
        coloracao_viavel(coloracao_metaheuristicos)

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        gerar_grafo() for n_grafo in range(100)
    ]
)
def test_hill_climbing(grafo_gerado):
    """
    Testes da função que implementa o algoritmo metaheurístico 
    hill-climbing para 100 grafos aleatórios. O teste verifica se a cor 
    dos vizinhos de cada vértice é diferentes, ou seja, verifica se
    a coloração devolvida é viável.
    """
    algoritmos_metaheuristicos = Metaheuristicas
    coloracao_metaheuristicos = algoritmos_metaheuristicos.hill_climbing(grafo_gerado)
    coloracao_viavel(coloracao_metaheuristicos)

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        gerar_grafo() for n_grafo in range(100)
        
    ]
)
def test_evolucionario(capfd, grafo_gerado):
    """
    Testes da função que implementa o algoritmo metaheurístico 
    evolucionário para 100 grafos aleatórios. O teste verifica se a coloração 
    devolvida é viável
    """
    algoritmos_metaheuristicos = Metaheuristicas
    n_pop = random.choice(list(range(10,30)))
    coloracao_metaheuristicos = algoritmos_metaheuristicos.evolucionario(grafo = grafo_gerado, n_pop = n_pop)
    coloracao_viavel(coloracao_metaheuristicos)

@pytest.mark.parametrize(
    "grafo_gerado",
    [
        gerar_grafo() for n_grafo in range(100)
        
    ]
)
def test_colonia(capfd, grafo_gerado):
    """
    Testes da função que implementa o algoritmo metaheurístico 
    colônia de formigas para 100 grafos aleatórios. O teste verifica se a coloração 
    devolvida é viável
    """
    algoritmos_metaheuristicos = Metaheuristicas
    coloracao_metaheuristicos = algoritmos_metaheuristicos.colonia_formigas(grafo = grafo_gerado)
    coloracao_viavel(coloracao_metaheuristicos)