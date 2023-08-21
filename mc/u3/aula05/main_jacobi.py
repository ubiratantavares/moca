import numpy as np
from ssle.jacobi import JacobiSolver

A = np.array([[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]])

b = np.array([4, 7, 3])

solver = JacobiSolver(A, b)
solution, iterations = solver.solve()
print("Solution:", solution)
print("Iterations:", iterations)