from decomposition.decomposition import Decomposition

class LDU(Decomposition):

    def __init__(self, matrix):
        super().__init__(matrix)
        self.L = [[0.0] * self.n for _ in range(self.n)]
        self.D = [[0.0] * self.n for _ in range(self.n)]
        self.U = [[0.0] * self.n for _ in range(self.n)]

    def get_L(self):
        for i in range(self.n):
            self.L[i][i] = 1.0
        return self.L
    
    def get_D(self):
        return self.D

    def get_U(self):
        return self.U
    
    def decompose(self):
        for i in range(self.n):
            # Diagonal Matrix D
            self.D[i][i] = self.matrix[i][i]

            # Lower Traiangular Matrix L
            for j in range(i + 1, self.n):
                self.L[j][i] = self.matrix[j][i] / self.D[i][i]

            # Upper Triangular Matrix U
            for j in range(i, self.n):
                self.U[i][j] = self.matrix[i][j] / self.D[i][i]

                for k in range(i + 1, self.n):
                    self.matrix[k][j] -= self.L[k][i] * self.U[i][j] * self.D[i][i]

                