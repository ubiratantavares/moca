import numpy as np

class GaussMatrixFactorization:

    def __init__(self, matrix):
        self.matrix  = matrix
    
    def gaussian_elimination(self):
        n = len(self.matrix)
        for i in range(n):
            # pivoteamento - troque linhas se necessário
            max_row = i
            for j in range(i + 1, n):
                if abs(self.matrix[j][i]) > abs(self.matrix[max_row][i]):
                    max_row = j
            self.matrix[i], self.matrix[max_row] = self.matrix[max_row], self.matrix[i]
        
            # fazer o elemento diagonal ser 1
            pivot = self.matrix[i][i]

            for j in range(i, n + 1):
                self.matrix[i][j] /= pivot

            # Elimine entradas diferentes de zero abaixo do pivot
            for j in range(i + 1, n):
                factor = self.matrix[j][i]
                for k in range(i, n + 1):
                    self.matrix[j][k] -= factor * self.matrix[i][k]

    def back_substitution(self):
        n = len(self.matrix)
        solution = [0] * n
        for i in range(n - 1, -1, -1):
            solution[i] = self.matrix[i][n]
            for j in range (i + 1 , n ):
                solution[i] -= self.matrix[i][j] * solution[j]
        return solution
    
    def factorize(self):
        self.gaussian_elimination()
        solution = self.back_substitution()
        return solution
    
    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str
