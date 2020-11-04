import gurobipy as gp
from gurobipy import GRB

import os

entradas = os.listdir(path='instancias') #list com os nomes dos arquivos de entrada

for i in entradas: #loop para abrir todos os arquivos
    print('Abrindo arquivo {}...'.format(i))
    arq = open(os.path.join(os.getcwd(), 'instancias', i), 'r') #abre o arquivo
    first_line = arq.readline() #le primeira linha para pegar os parametros
    quebra = first_line.split(' ') #split na primeira linha para capturar o parametros
    v = int(quebra[0]) #numero de vertices do grafo
    c = int(quebra[1]) #numero de cores
    print('{} vértices'.format(v))
    print('{} cores'.format(c))

    cor = [0] * v #vetor que armazena a cor de um determinado vertice

    j=0
    for linha in arq: #le o resto do arquivo com as cores de cada vertice
        cor[j] = int(linha) #armazena os valores no vetor cor
        j=j+1

    print(cor) #imprime vetor cor

    print('\n')   
