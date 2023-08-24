"""
Eigen Decomposition

Seja P uma matriz de autovetores de uma determinada matriz quadrada A e seja D uma matriz diagonal com os autovalores 
correspondentes na diagonal. 

Então, desde que P seja uma matriz quadrada, A pode ser escrita como uma decomposição própria como: 

A = PDP*

Onde P* é a matriz transposta do conjugado da matriz P.

"""
import numpy as np

from scipy.linalg import eig

class Eigen:

    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.eigenvalues = None
        self.eigenvectors = None

    def get_eigenvalues(self):
        return self.eigenvalues
    
    def get_eigenvectors(self):
        return self.eigenvectors

    def decompose(self):
        self.eigenvalues, self.eigenvectors = eig(self.matrix)
