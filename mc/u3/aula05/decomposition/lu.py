from decomposition.decomposition import Decomposition

class LU(Decomposition):
    def __init__(self, matrix):
        super().__init__(matrix)
        self.L = [[0.0] * self.n for _ in range(self.n)]
        self.U = [[0.0] * self.n for _ in range(self.n)]

    def get_L(self):
        return self.L

    def get_U(self):
        return self.U
    
    def decompose(self):
        for i in range(self.n):
            # Upper Triangular
            for k in range(i, self.n):
                sum = 0.0
                for j in range(i):
                    sum += self.L[i][j] * self.U[j][k]
                self.U[i][k] = self.matrix[i][k] - sum

            # Lower Triangular
            for k in range(i, self.n):
                if i == k:
                    self.L[i][i] = 1.0
                else:
                    sum = 0.0
                    for j in range(i):
                        sum += self.L[k][j] * self.U[j][i]
                    self.L[k][i] = (self.matrix[k][i] - sum) / self.U[i][i]
