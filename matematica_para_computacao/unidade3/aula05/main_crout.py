from decomposition.crout import Crout
from util.operation import Operation

matriz = [[2.0, -1.0, 3.0],
          [4.0, 2.0, 1.0],
          [1.0, 3.0, 2.0]]

decomposition  = Crout(matriz)
decomposition.decompose()

matriz_L = decomposition.get_L()
matriz_U = decomposition.get_U()

print("Matrix")
for row in matriz:
    print(row)

print("\nMatriz Triangular L (Lower)")
for row in matriz_L:
    print(row)

print("\nMatriz Triangular U (Upper)")
for row in matriz_U:
    print(row)

print("\nProduto")
operation = Operation(matriz_L, matriz_U)
matriz_produto = operation.produto_matrizes()
for row in matriz_produto:
    print(row)
