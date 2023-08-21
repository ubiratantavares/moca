"""
Método Iterativo para Resolução de Sistemas de Equações Lineares

Método de Jacobi: Divide o sistema em equações lineares isoladas e atualiza
iterativamente as variáveis.
"""
import numpy as np
from scipy.linalg import norm

class JacobiSolver:

    def __init__(self, A, b, tol=1e-8, max_iter=1000):
        self.A = A
        self.b = b
        self.tol = tol
        self.max_iter = max_iter
        self.n = A.shape[0]

    def solve(self):
        x = np.zeros(self.n)
        x_new = np.copy(x)
        iter_count = 0

        while iter_count < self.max_iter:
            for i in range(self.n):
                x_new[i] = (self.b[i] - np.dot(self.A[i, :i], x[:i]) - np.dot(self.A[i, i+1:], x[i+1:])) / self.A[i, i]

            if norm(x_new - x) < self.tol:
                break
        
            x = np.copy(x_new)
            iter_count += 1

        return x, iter_count
