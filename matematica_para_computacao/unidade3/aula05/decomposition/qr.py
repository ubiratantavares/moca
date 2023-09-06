"""
Em álgebra linear, uma decomposição QR (também chamada de fatoração QR) de uma matriz é uma decomposição de uma matriz A 
em um produto A = QR de uma matriz ortogonal Q e uma matriz triangular superior R. 
A decomposição QR é usado frequentemente para resolver o problema de mínimos quadrados linear e é a base para um determinado 
algoritmo de autovalores, o algoritmo QR.

Existem vários métodos para calcular a decomposição QR, tais como o uso do processo de Gram–Schmidt, 
transformações Householder, ou rotações de Givens.

Esta classe implementa a decomposição de QR usando o método de Gram-Schmidt para fatoração de uma matriz.

A classe armazena as matrizes Q (com vetores ortogonais normalizados) e 
R (triangular superior) separadamente, que são os resultados da decomposição.

"""

class QR:

    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.Q = [[0.0] * self.n for _ in range(self.m)]
        self.R = [[0.0] * self.n for _ in range(self.n)]

    def get_Q(self):
        return self.Q
    
    def get_R(self):
        return self.R

    def dot_product(self, vec1, vec2):
        return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    
    def normalize(self, vector):
        magnitude = (sum(v ** 2 for v in vector)) ** 0.5
        return [v / magnitude for v in vector]
    
    def decompose(self):
        for j in range(self.n):
            v = [self.matrix[i][j] for i in range(self.m)]
            for i in range(j):
                r = self.dot_product(self.Q[i], v)
                for k in range(self.m):
                    v[k] -= r * self.Q[i][k]
            self.Q[j] = self.normalize(v)
            for i in range(j, self.n):
                self.R[j][i] = self.dot_product(self.Q[j], [self.matrix[k][i] for k in range(self.m)])
            