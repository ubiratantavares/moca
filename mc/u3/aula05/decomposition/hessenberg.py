import numpy as np
from scipy.linalg import hessenberg

class Hessenberg:

    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.H = None
        self.P = None

    def get_H(self):
        return self.H

    def get_P(self):
        return self.P

    def decompose(self):
        self.H, self.P = hessenberg(self.matrix, calc_q=True)
