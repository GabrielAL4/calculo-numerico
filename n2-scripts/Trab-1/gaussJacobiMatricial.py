import numpy as np

n = int(input("Informe o número de incógnitas do sistema: "))

A = np.zeros((n, n))
B = np.zeros((n, 1))
X = np.zeros((n, 1))
Xi = np.zeros((n, 1))
D = np.zeros((n, n))
S = np.zeros((n, n))
I = np.zeros((n, n))
SI = np.zeros((n, n))
J = np.zeros((n, n))
E = np.zeros((n, 1))
JX = np.zeros((n, 1))
AX = np.zeros((n, 1))

erro = float(input("Entre com o valor do erro: "))

para = True
while para:
    cont = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = 1 / A[i][j]
            else:
                D[i][j] = 0
    print("\n\nMatriz inversa da diagonal de A:\n", D)

    for i in range(n):
        for j in range(n):
            if i <= j:
                I[i][j] = 0
            else:
                I[i][j] = A[i][j]
    print("\n\nMatriz inferior:\n", I)

    for i in range(n):
        for j in range(n):
            if i >= j:
                S[i][j] = 0
            else:
                S[i][j] = A[i][j]
    print("\n\nMatriz superior:\n", S)

    SI = S + I
    print("\n\nMatriz superior + inferior:\n", SI)

    for i in range(n):
        for j in range(n):
            J[i][j] = -D[i][j] * SI[i][j]
    print("\n\nMatriz J:\n", J)

    for i in range(n):
        for j in range(1):
            E[i][j] = B[i][j]
            for k in range(n):
                E[i][j] = E[i][j] + J[i][k] * Xi[k][j]
    print("\n\nMatriz E:\n", E)

    for i in range(n):
        for j in range(1):
            X[i][j] = E[i][j] / D[i][i]
    print("\n\nMatriz X:\n", X)

    for i in range(n):
        for j in range(1):
            dif = abs(Xi[i][j] - X[i][j])
            if dif > erro:
                Xi[i][j] = X[i][j]
            else:
                cont = cont + 1
    if cont == n:
        para = False
