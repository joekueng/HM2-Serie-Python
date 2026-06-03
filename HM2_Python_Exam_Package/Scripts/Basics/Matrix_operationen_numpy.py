import numpy as np


def main():
    a_matrix = np.array([[2.0, -1.0], [1.0, 3.0]])
    b_vector = np.array([1.0, 7.0])

    solution = np.linalg.solve(a_matrix, b_vector)
    inverse_matrix = np.linalg.inv(a_matrix)
    determinant = np.linalg.det(a_matrix)
    eigenvalues, eigenvectors = np.linalg.eig(a_matrix)

    print("A =")
    print(a_matrix)
    print("b =", b_vector)
    print("Loesung von A x = b:", solution)
    print("A inverse =")
    print(inverse_matrix)
    print("det(A) =", determinant)
    print("Eigenwerte =", eigenvalues)
    print("Eigenvektoren =")
    print(eigenvectors)


if __name__ == "__main__":
    main()
