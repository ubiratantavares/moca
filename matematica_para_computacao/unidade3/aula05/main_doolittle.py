from decomposition.doolittle import Doolittle
from util.operation import Operation

matrix = [[2.0, -1.0, 3.0],
          [4.0, 2.0, 1.0],
          [1.0, 3.0, 2.0]]

decomposition  = Doolittle(matrix)
decomposition.decompose()

matriz_L = decomposition.get_L()
matriz_U = decomposition.get_U()

print("Matrix")
for row in matrix:
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
