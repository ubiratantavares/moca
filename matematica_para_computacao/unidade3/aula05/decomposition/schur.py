"""
A decomposição de Schur de uma matriz quadrada complexa é uma decomposição de matriz da forma A

Q*AQ = T = D + N

onde Q é uma matriz unitária, Q* é sua transposta conjugada e T é uma matriz triangular superior que é a 
soma da diagonal D = diag(lambda_1,lambda_2,...,lambda_n), ou seja, uma matriz diagonal que consiste em autovalores 
lambda_i de A e uma matriz triangular estritamente superior N.
"""

import numpy as np
from scipy.linalg import schur

class Schur:

    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.T = None
        self.P = None

    def get_T(self):
        return self.T

    def get_P(self):
        return self.P

    def decompose(self):
        self.T, self.P = schur(self.matrix)

    