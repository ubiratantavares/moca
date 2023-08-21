from abc import ABC, abstractmethod

class Decomposition(ABC):

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    @abstractmethod
    def get_L(self):
        pass

    @abstractmethod
    def get_U(self):
        pass

    @abstractmethod
    def decompose(self):
        pass

