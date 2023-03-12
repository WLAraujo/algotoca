from graphcol.gulosos import Gulosos
from graphcol import gulosos
from graphcol.metaheuristicas import Metaheuristicas
import igraph as ig
import numpy as np
import pandas as pd
import plotly.express as px
import glob
import time
from datetime import datetime
import traceback

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

instancias = sorted(glob.glob("./instancias/*.col"))

flag_erro = 0

resultados_gulosos = pd.DataFrame({"algoritmo" : pd.Series(dtype='str'),
                           "instancia" : pd.Series(dtype='str'),
                           "vertices" : pd.Series(dtype='int'),
                           "arestas" : pd.Series(dtype='int'),
                           "otimo" : pd.Series(dtype='int'),
                           "resultado" : pd.Series(dtype='int'),
                           "inicio" : pd.Series(dtype='datetime64[ns]'),
                           "fim" : pd.Series(dtype='datetime64[ns]')
                           })

resultados_metaheuristicos = pd.DataFrame({"algoritmo" : pd.Series(dtype='str'),
                                "instancia" : pd.Series(dtype='str'),
                                "vertices" : pd.Series(dtype='int'),
                                "arestas" : pd.Series(dtype='int'),
                                "otimo" : pd.Series(dtype='int'),
                                "resultado" : pd.Series(dtype='int'),
                                "tabu" : pd.Series(dtype='int'),
                                "iteracoes_min" : pd.Series(dtype='int'),
                                "iteracoes_max" : pd.Series(dtype='int'),
                                "iteracoes_s_mud_mel" : pd.Series(dtype='int'),
                                "hc_div" : pd.Series(dtype='float'),
                                "populacao" : pd.Series(dtype='int'),
                                "geracoes" : pd.Series(dtype='int'),
                                "cf_alfa" : pd.Series(dtype='float'),
                                "cf_beta" : pd.Series(dtype='float'),
                                "cf_evaporacao" : pd.Series(dtype='float'),
                                "inicio" : pd.Series(dtype='datetime64[ns]'),
                                "fim" : pd.Series(dtype='datetime64[ns]')
                                })

def pipeline_gulosos(grafo, instancia, vertices, arestas):
    linhas_instancia = []
    inicio_guloso = datetime.now()
    linha_guloso = ["guloso", instancia, vertices, arestas, 0, len(set(Gulosos.guloso(grafo).vs['cor'])), inicio_guloso]
    linha_guloso.append(datetime.now())
    inicio_dsatur = datetime.now()
    linha_dsatur = ["dsatur", instancia, vertices, arestas, 0, len(set(Gulosos.dsatur(grafo).vs['cor'])), inicio_dsatur]
    linha_dsatur.append(datetime.now())
    inicio_rlf = datetime.now()
    linha_rlf = ["rlf", instancia, vertices, arestas, 0, len(set(Gulosos.rlf(grafo).vs['cor'])), inicio_rlf]
    linha_rlf.append(datetime.now())
    linhas_instancia.append(linha_guloso)
    linhas_instancia.append(linha_dsatur)
    linhas_instancia.append(linha_rlf)
    return linhas_instancia

def pipeline_metaheuristicos(grafo, instancia, vertices, arestas):

    linhas_instancia = []

    def pipeline_tabucol(grafo, instancia, vertices,arestas):
        linhas_tabucol = []
        iteracoes_min = 20
        iteracoes_max = 50
        for tabu in [3,5,7,9]:
            for iteracoes_s_mudanca in [8,10,12,14]:
                inicio_tabucol = datetime.now()
                linha_tabucol = ["tabucol", instancia, vertices, arestas, 0, len(set(Metaheuristicas.tabucol(grafo, 
                                tabu = tabu, iteracoes_s_mudanca=iteracoes_s_mudanca, msg_print = False).vs['cor'])),
                                tabu, iteracoes_min, iteracoes_max, iteracoes_s_mudanca, 0, 0, 0, 0, 0, 0, inicio_tabucol]
                linha_tabucol.append(datetime.now())
                linhas_tabucol.append(linha_tabucol)
                time.sleep(0.5)
        return linhas_tabucol

    def pipeline_hillclimbing(grafo, instancia, vertices, arestas):
        linhas_hillclimbing = []
        iteracoes_s_melhora = 10
        for div in [x/100 for x in range(15, 96, 25)]:
            for iteracoes_max in [40,45,50,55]:
                inicio_hillclimbing = datetime.now()
                linha_hillclimbing = ["hill climbing", instancia, vertices, arestas, 0, len(set(Metaheuristicas.hill_climbing(grafo, 
                                    div, iteracoes_max).vs['cor'])), 0, 0, iteracoes_max, 
                                    iteracoes_s_melhora, div, 0, 0, 0, 0, 0, inicio_hillclimbing]
                linha_hillclimbing.append(datetime.now())
                linhas_hillclimbing.append(linha_hillclimbing)
                time.sleep(0.5)
        return linhas_hillclimbing

    def pipeline_evolucionario(grafo, instancia, vertices, arestas):
        linhas_evolucionario = []
        for populacao in [10,15,20,25]:
            for geracoes in [10,15,20,25]:
                inicio_evolucionario = datetime.now()
                linha_evolucionario = ["evolucionario", instancia, vertices, arestas, 0, len(set(Metaheuristicas.evolucionario(grafo, 
                                    populacao, geracoes).vs['cor'])), 0, 0, 0, 0, 0, populacao, geracoes, 0, 0, 0, inicio_evolucionario]
                linha_evolucionario.append(datetime.now())
                linhas_evolucionario.append(linha_evolucionario)
                time.sleep(0.5)
        return linhas_evolucionario
    
    def pipeline_colonia(grafo, instancia, vertices, arestas):
        linhas_colonia = []
        iteracoes_max = 20
        beta = 1
        alfa = 1
        for formigas in [10,15,20,25]:
            for evaporacao in [x/100 for x in range(15, 96, 25)]:
                inicio_colonia = datetime.now()
                linha_colonia = ["colonia formigas", instancia, vertices, arestas, 0, len(set(Metaheuristicas.colonia_formigas(grafo, 
                formigas, iteracoes_max, alfa, beta, evaporacao).vs['cor'])), 0, 0, iteracoes_max, 0, 0, formigas, 0, alfa, beta, 
                evaporacao, inicio_colonia]
                linha_colonia.append(datetime.now())
                linhas_colonia.append(linha_colonia)
                time.sleep(0.5)
        return linhas_colonia

    linhas_tabucol = pipeline_tabucol(grafo, instancia, vertices,arestas)
    linhas_hillclimbing = pipeline_hillclimbing(grafo, instancia, vertices,arestas)
    linhas_evolucionario = pipeline_evolucionario(grafo, instancia, vertices,arestas)
    linhas_colonia = pipeline_colonia(grafo, instancia, vertices,arestas)
    linhas_instancia = linhas_tabucol + linhas_evolucionario + linhas_hillclimbing + linhas_colonia
    return linhas_instancia

def criar_grafo(arquivo):
    try:
        linhas = []
        with open(f'{arquivo}') as f:
            linhas = f.readlines()
        lista_arestas = []
        for linha in linhas:
            if linha[0] == 'p':
                nos_arestas = tuple(linha[7:-1].split(" "))
                n_vertices = int(nos_arestas[0])
                m_arestas = int(nos_arestas[1])
            if linha[0] == 'e':
                aresta_strings = linha[2:-1].split(" ")
                lista_arestas.append(tuple([(int(v)-1) for v in aresta_strings]))
        grafo = ig.Graph()
        grafo.add_vertices(n_vertices)
        grafo.add_edges(lista_arestas)
        grafo.simplify(multiple=True, loops=True)
        return grafo
    except:
        print(f"Arquivo {arquivo} no formato errado")
        return None

for instancia in instancias:
    try:
        print(f"Instancia {instancia}")
        grafo = criar_grafo(instancia)
        if grafo is not None:
            for i in range(10):
                print("Iteração " + str(i))
                linhas_instancia_gulosos = pipeline_gulosos(grafo, instancia[13:-4], grafo.vcount(), grafo.ecount())
                resultados_gulosos = pd.concat([resultados_gulosos, pd.DataFrame(linhas_instancia_gulosos,
                                                            columns = ['algoritmo', 'instancia', 'vertices', 'arestas', 'otimo', 'resultado',
                                                            'inicio', 'fim'])])               
                linhas_instancia_metaheuristicos = pipeline_metaheuristicos(grafo, instancia[13:-4], grafo.vcount(), grafo.ecount())
                resultados_metaheuristicos = pd.concat([resultados_metaheuristicos, pd.DataFrame(linhas_instancia_metaheuristicos,
                                                            columns = ['algoritmo', 'instancia', 'vertices', 'arestas', 'otimo', 'resultado',
                                                            'tabu', 'iteracoes_min', 'iteracoes_max', 'iteracoes_s_mud_mel', 'hc_div',
                                                            'populacao', 'geracoes', 'cf_alfa', 'cf_beta', 'cf_evaporacao', 'inicio', 'fim'])])
                time.sleep(0.5)
        print(f'Instância {instancia[13:-4]} processada')
        resultados_gulosos.to_csv('resultados_gulosos.csv', encoding='utf-8')
        resultados_metaheuristicos.to_csv('resultados_metaheuristicos.csv', encoding='utf-8')
    except Exception as e:
        traceback.print_exc()


