from decomposition.qr_refletores import QRWithReflectors

# Example usage
matrix = [[6, 5, 1],
            [0, 3, 5],
            [2, 7, 2]]

decomposition = QRWithReflectors(matrix)
decomposition.decompose()

Q = decomposition.get_Q()
R = decomposition.get_R()

print("Matrix")
for row in matrix:
    print(row)

print("\nMatrix Q:")
print(Q)

print("\nMatrix R:")
print(R)
