from gurobipy import *
from itertools import product
import numpy as np
#import numpy as np

import os


def le_entrada(instancia):
    print('Abrindo arquivo {}...'.format(instancia))
    arq = open(os.path.join(os.getcwd(), 'instancias',
                            instancia), 'r')  # abre o arquivo
    first_line = arq.readline()  # le primeira linha para pegar os parametros
    # split na primeira linha para capturar o parametros
    quebra = first_line.split(' ')
    v = int(quebra[0])  # numero de vertices do grafo
    c = int(quebra[1])  # numero de cores
    print('{} vértices'.format(v))
    print('{} cores'.format(c))

    grafo = [0] * v  # vetor que armazena a cor de um determinado vertice

    j = 0
    for linha in arq:  # le o resto do arquivo com as cores de cada vertice
        grafo[j] = int(linha)  # armazena os valores no vetor cor
        j += 1

    print(grafo)  # imprime vetor cor

    print('\n')

    return v, c, grafo


def executa_modelo(v, c, grafo):
    # criando um modelo vazio no gurobi
    try:

        modelo = Model()
        modelo.params.TimeLimit
        x = modelo.addVars(v, c, vtype=GRB.BINARY)
        
        # Funcao objetivo
        modelo.setObjective(quicksum(x[vertice, cor] for vertice in range(v)
                                     for cor in range(c)
                                     if grafo[vertice]-1 != cor), GRB.MINIMIZE)
        # Restricao 1  
        modelo.addConstrs(quicksum(x[vertice, cor]
                                    for cor in range(c)) == 1 
        							for vertice in range(v))
        
        vertices = range(2, v)
        # Restricao 2
        modelo.addConstrs((x[p, cor] - x[q, cor] + x[r, cor]) <= 1
			                for p in range(v)
			                for q in range(v)
			                for r in range(v)
			                for cor in range(c)
			                if p < q < r)

        modelo.optimize()
        c= modelo.getVars()
        print(c)

    except GurobiError as e:
        print('Error code ' + str(e.errno) + ': ' + str(e))

    except AttributeError:
        print('Encountered an attribute error')


#entradas = os.listdir(path='instancias') #list com os nomes dos arquivos de entrada
entradas = ['rand_50_10.txt']
for instancia in entradas:  # loop para abrir todos os arquivos
    v, c, grafo = le_entrada(instancia)
    executa_modelo(v, c, grafo)
