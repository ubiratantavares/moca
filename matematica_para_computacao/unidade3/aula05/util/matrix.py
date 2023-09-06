import numpy as np

class Matrix:

    def __init__(self, data):
        self.data = np.array(data)
        self.shape = self.data.shape
   
    def inverse(self):
        if self.shape[0] != self.shape[1]:
            raise ValueError("A matriz não é quadrada, a inversa não existe.")        
        try:
            inv = np.linalg.inv(self.data)
            return Matrix(inv)
        except np.linalg.LinAlgError:
            raise ValueError("Matrix é singular, inversa não existe.")
    
    def determinant(self):
        if self.shape[0] != self.shape[1]:
            raise ValueError("A matriz não é quadrada, o determinante não existe")        
        return np.linalg.det(self.data)
    
    def transpose(self):
        transposed = np.transpose(self.data)
        return Matrix(transposed)
    
    def scalar_multiply(self, alpha):
        scaled = self.data * alpha
        return Matrix(scaled)
    
    def add_constant(self, c):
        added = self.data + c
        return Matrix(added)
    
    def __str__(self):
        return str(self.data.tolist())  

