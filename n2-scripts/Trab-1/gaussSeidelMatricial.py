import numpy as np
import math

n = int(input("Informe o numero de incognitas do sistema: "))
erro = float(input("Entre com o valor do erro: "))

A = np.zeros((n, n))
B = np.zeros((n, 1))
X = np.zeros((n, 1))

for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"Entre com o elemento A[{i+1}][{j+1}] : "))

    B[i][0] = float(input(f"Entre com o elemento B[{i+1}]: "))
    X[i][0] = float(input(f"Entre com o elemento Xi[{i+1}]: "))

# Calculando a Diagonal
D = np.diag(np.diag(A))

# Montando a Matriz Inferior
I = np.tril(A, k=-1)

# Montando a Matriz Superior
S = np.triu(A, k=1)

# Matriz identidade
ident = np.eye(n)

pivo = 0
p = 0
m = 0
soma = 0
aux = 0
dif = 0
para = 1

while para == 1:
    GX = np.dot(G, X)  # Multiplica a matriz G pela matriz X
    AX = np.dot(A, X)  # Multiplica a matriz A pela matriz X

    for i in range(n):
        R[i][0] = B[i][0] - AX[i][0]  # Calcula o vetor residual

        for j in range(n):
            if i == j:
                DI[i][j] = 1/D[i][j]  # Inversa da matriz diagonal
            else:
                DI[i][j] = 0

    G = np.dot(-DI, (I + S))  # Matriz G
    F = np.dot(DI, B)  # Vetor F
    X = np.dot(G, X) + F  # Nova solução

    for i in range(n):
        soma = soma + pow(R[i][0], 2)

    p = math.sqrt(soma)

    if aux != 0:
        dif = abs(p - pivo)

    if p != 0:
        erro_p = abs(dif/p)
    else:
        erro_p = abs(dif)

    if erro_p < erro:
        para = 0
    else:
        pivo = p
        soma = 0
        aux = aux + 1

print("\n\nResultado:")
for i in range(n):
    print("X{} = {:.4f}".format(i+1, X[i][0]))
