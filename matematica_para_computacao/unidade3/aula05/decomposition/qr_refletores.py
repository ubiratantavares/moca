"""
A decomposição QR utilizando refletores (ou reflectores) é uma abordagem para decompor 
uma matriz em um produto de matrizes ortogonais Q e R triangular superior. 
Isso pode ser feito usando o método de reflexão de Householder
"""
import numpy as np
from scipy.linalg import qr

class QRWithReflectors:

    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.Q = None
        self.R = None

    def get_Q(self):
        return self.Q

    def get_R(self):
        return self.R

    def decompose(self):
        self.Q, self.R = qr(self.matrix, mode='full')
