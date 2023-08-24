"""
Em álgebra linear, a decomposição em valores singulares ou singular value decomposition (SVD) 
é a fatoração de uma matriz real ou complexa, com diversas aplicações importantes em processamento de sinais e estatística.

Formalmente, a decomposição em valores singulares de uma matriz m × n real ou complexa M é uma fatoração ou fatorização 
na forma: USV*

onde U é uma matriz unitária m × m real ou complexa, S é uma matriz retangular diagonal m × n com números reais 
não-negativos na diagonal, e V* (a conjugada transposta de V) é uma matriz unitária n × n real ou complexa.

"""

from scipy.linalg import svd

class SVD:

    def __init__(self, matrix):
        self.matrix = matrix
        self.U = None
        self.S = None
        self.Vt = None

    def get_U(self):
        return self.U
    
    def get_S(self):
        return self.S
    
    def get_Vt(self):
        return self.Vt

    def decompose(self):
        self.U, self.S, self.Vt = svd(self.matrix)

