from decomposition.decomposition import Decomposition

class Crout(Decomposition):

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
            self.U[i][i] = 1.0

            for j in range(i, self.n):
                sum_l = 0.0
                for k in range(i):
                    sum_l += self.L[j][k] * self.U[k][i]
                self.L[j][i] = self.matrix[j][i] - sum_l

            for j in range(i + 1, self.n):
                sum_u = 0.0
                for k in range(i):
                    sum_u += self.L[i][k] * self.U[k][j]
                self.U[i][j] = (self.matrix[i][j] - sum_u) / self.L[i][i]

