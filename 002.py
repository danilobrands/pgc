# Biblioteca de álgebra linear
import numpy as np

# Pacote de funções para plot
import matplotlib.pyplot as plt

# Função de Mínimos Quadrados ('Least Squares')
from scipy.linalg import lstsq

from scipy.signal import hamming as ham

##testes de tipo de dados

#colocar entre o print para imprimir
#pint(type(3))

#inteiro
type(3)

#float
type(3.23123)

#String
type('teste')

#List
type([1, 2, 3])

#Array
type(np.array([1, 2, 3]))

pi = 3.14
print(isinstance(pi, float))

##Operações básicas

5 + 9
3 - 7
2 * 4
9 / 3

print((1 + (2 - (3 / 4))))

##Listas
#Lista simples
L1 = [1, 3, 7, 29]

#Lista de listas de mesmo tamanho
L2 = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

#Lista de listas de diferentes tamanhos
L3 = [[1], [2, 3], [4, 5, 6]]

#Lista vazia
L4 = []

#adicionar itens ao fim de uma lista
L_teste = []

L_teste.append(5)
L_teste.append([1, 3])

L_teste.append([[7,2], [9,0]])
print(L_teste)

#L_teste.append(L_teste)
#print(L_teste)


##Adicionando o conteúdo de uma lista ao fim de outra
L_teste_1 = []
L_teste_2 = [3,4,5]
L_teste_3 = [9,1,2,3,4,1]

L_teste_1.extend(L_teste_2)
print(L_teste_1)

L_teste_1.extend(L_teste_3)
print(L_teste_1)

##Encontrando a posição do primeiro item com determinado valor na lista
L_teste = [7, 1, 2, 5, 2, 8, 9, 0, 3]
print(L_teste.index(5))

##Ordenando os itens da lista
L_teste = [3,1,4,6,7,9]
L_teste.sort()
print(L_teste)

L_teste.sort(reverse=True)
print(L_teste)

###Exercício
L1 = [1,3,7,29,40,2]
L2 = [1,2,3,4,5,6,7,8,9]

L1.extend(L2)
print('Exercício')
print(L1)
print(L1.index(29))
L1.sort()
print(L1)
print(L1.index(29))

##craindo matrizes 3x3
A = np.array([[3,4,5], [6,7,8], [9,0,1]])
B = np.array([[0,1,2], [3,4,5], [6,7,8]])

#Imprimindo
print(A)
print(A[:, :2])
print(B[1:,1])

#soma
print(A+B)





