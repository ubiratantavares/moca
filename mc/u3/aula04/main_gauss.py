from gauss import GaussMatrixFactorization

matrix = [[2, 3, 1, 5],
          [1, 1, -1, 1],
          [3, 2, 3, 10]]

gauss_fatorization = GaussMatrixFactorization(matrix)
print("Matriz Original:")
print(gauss_fatorization)

gauss_fatorization.gaussian_elimination()
print("Matriz após a fatoração pelo método de eliminação de gauss:")
print(gauss_fatorization)

print("Solução do sistema de equação:")
solution = gauss_fatorization.factorize()
print(solution)