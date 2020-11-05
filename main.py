import gurobipy as gp
from gurobipy import GRB
import numpy as np

import os

def le_entrada(instancia):
    print('Abrindo arquivo {}...'.format(instancia))
    arq = open(os.path.join(os.getcwd(), 'instancias', instancia), 'r') #abre o arquivo
    first_line = arq.readline() #le primeira linha para pegar os parametros
    quebra = first_line.split(' ') #split na primeira linha para capturar o parametros
    v = int(quebra[0]) #numero de vertices do grafo
    c = int(quebra[1]) #numero de cores
    print('{} vértices'.format(v))
    print('{} cores'.format(c))

    grafo = [0] * v #vetor que armazena a cor de um determinado vertice

    j = 0
    for linha in arq: #le o resto do arquivo com as cores de cada vertice
        grafo[j] = int(linha) #armazena os valores no vetor cor
        j += 1

    print(grafo) #imprime vetor cor

    print('\n')

    return v, c, grafo


def executa_modelo(v, c, grafo):
    #criando um modelo vazio no gurobi
    modelo = Model()

    tam_xvk = v*c
    modelo.params.LogToConsole = True
    modelo.params.TimeLimit
    x = modelo.addVars(tam_xvk, vtype = GRB.BINARY)

    #Funcao objetivo
    #ESTA ERRADO
    modelo.setObjective(quicksum(x[i*c + k] for i in range(0, v) for k in range(0, c)), GRB.MINIMIZE)

    #Restricao 1
    #ESTA ERRADO
    modelo.addConstr(quicksum(x[i*c + (k-1)] for k in grafo) = 1)
    #Restricao 2
    #Restricao 3
    
    modelo.optimize()
#    for i in range(v):
#        if x[i].X > 0.5:
#            print("item:", i, "foi selecionado")


#entradas = os.listdir(path='instancias') #list com os nomes dos arquivos de entrada
entradas = ['rand_10_2.txt']
for instancia in entradas: #loop para abrir todos os arquivos
    le_entrada(instancia)
