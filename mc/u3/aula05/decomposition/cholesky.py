from decomposition.decomposition import Decomposition

class Cholesky(Decomposition):
    
    def __init__(self, matrix):
        super().__init__(matrix)
        self.L = [[0.0] * self.n for _ in range(self.n)]

    def get_L(self):
        return self.L
    
    def get_LT(self):
        return [[self.L[j][i] for j in range(self.n)] for i in range(self.n)]
    
    def get_U(self):
        return self.get_LT()

    def is_symmetric(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True  
    
    def decompose(self):
        if not self.is_symmetric():
            raise ValueError("Matrix is not symmetric")

        for i in range(self.n):
            for j in range(i + 1):
                if i == j:
                    sum_diag = sum(self.L[i][k] ** 2 for k in range(j))
                    self.L[i][j] = (self.matrix[i][j] - sum_diag) ** 0.5
                else:
                    sum_lower = sum(self.L[i][k] * self.L[j][k] for k in range(j))
                    self.L[i][j]= (self.matrix[i][j] - sum_lower) / self.L[j][j]