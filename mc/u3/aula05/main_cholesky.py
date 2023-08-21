from decomposition.cholesky import Cholesky
from util.operation import Operation

matrix = [[9, 3, 6],
          [3, 4, -2],
          [6, -2, 7]]

decomposition = Cholesky(matrix)

if decomposition.is_symmetric():    
    decomposition.decompose()
    matriz_L = decomposition.get_L()
    matriz_U = decomposition.get_U()
    
    print("Matrix")
    for row in matrix:
        print(row)

    print("\nMatriz Triangular L")
    for row in matriz_L:
        print(row)

    print("\nMatriz Triangular L Transposta")
    for row in matriz_U:
        print(row)

    print("\nProduto")
    operation = Operation(matriz_L, matriz_U)
    matriz_produto = operation.produto_matrizes()
    for row in matriz_produto:
        print(row)
else:
    print("Matriz não simetrica")