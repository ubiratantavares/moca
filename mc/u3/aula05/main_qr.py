from decomposition.qr import QR

matrix = [[6, 5, 1],
          [0, 3, 5],
          [2, 7, 2]]

decomposition = QR(matrix)
decomposition.decompose()

Q = decomposition.get_Q()
R = decomposition.get_R()

print("Matrix:")
for row in matrix:
    print(row)

print("\nMatrix Q:")
for row in Q:
    print(row)

print("\nMatrix R:")
for row in R:
    print(row)