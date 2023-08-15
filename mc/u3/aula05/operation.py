import numpy as np

class OperationMatrix:

    def __init__(self, A, B):
        self.A = np.array(A)
        self.B = np.array(B)

    def soma(self):
        if self.A.shape != self.B.shape:
            raise ValueError("As matrizes devem ter as mesmas dimensões para realizar a soma.")        
        result = self.A + self.B
        return result

    def subtracao(self):
        if self.A.shape != self.B.shape:
            raise ValueError("As matrizes devem ter as mesmas dimensões para realizar a subtração.")        
        result = self.A - self.B
        return result

    def produto_matrizes(self):
        if self.A.shape[1] != self.B.shape[0]:
            raise ValueError("O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")        
        result = np.dot(self.A, self.B)
        return result

    def multiplicacao_matriz_vetor(self, vetor):
        if self.A.shape[1] != len(vetor):
            raise ValueError("O número de colunas da matriz deve ser igual ao tamanho do vetor.")        
        result = np.dot(self.A, vetor)
        return result.tolist()
