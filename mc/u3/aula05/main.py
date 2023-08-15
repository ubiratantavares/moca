import numpy as np

from matrix import Matrix
from lu import LUDecomposition
from operation import OperationMatrix

matrix_A = [[2, -1, 3],
            [4, 2, 1],
            [1, 3, 2]]

lu_decomposition = LUDecomposition(matrix_A)
lu_decomposition.decompose()

L = lu_decomposition.get_L()
U = lu_decomposition.get_U()

print("Matrix A:")
for row in matrix_A:
    print(row)

print("\nLower Triangular Matrix L:")
for row in L:
    print(row)

print("\nUpper Triangular Matrix U:")
for row in U:
    print(row)

print("\nProduto L*U")
om = OperationMatrix(L, U)
P = om.produto_matrizes()
for row in P:
    print(row)

