from decomposition.ldu import LDU
from util.operation import Operation


matrix = [[2.0, -1.0, 3.0],
          [4.0, 2.0, 1.0],
          [1.0, 3.0, 2.0]]

decomposition = LDU(matrix)

print("Matrix")
for row in matrix:
    print(row)

decomposition.decompose()

matriz_L = decomposition.get_L()
matriz_D = decomposition.get_D()
matriz_U = decomposition.get_U()

print("\nMatriz Triangular L")
for row in matriz_L:
    print(row)

print("\nMatriz D")
for row in matriz_D:
    print(row)

print("\nMatriz Triangular U")
for row in matriz_U:
    print(row)

# calcular o produto LDU para verificar se devolve a matriz A
print("\nProduto")
operation = Operation(matriz_L, matriz_D)
matriz_produto1 = operation.produto_matrizes()

operation = Operation(matriz_produto1, matriz_U)
matriz_produto2 = operation.produto_matrizes()
for row in matriz_produto2:
    print(row)
