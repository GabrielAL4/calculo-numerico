import math

def gaussJacobi():
    n = int(input("Informe o numero de incognitas do sistema: "))

    A = [[0]*n for i in range(n)]
    B = [0]*n
    X = [0]*n
    Xi = [0]*n
    Soma = [0]*n

    print("Entre com os elementos da matriz A: ")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))

    print("\nMatriz A:")
    for i in range(n):
        for j in range(n):
            print("{:.2f}".format(A[i][j]), end="\t")
        print()

    print("\nEntre com os valores da matriz B (termos independentes): ")
    for i in range(n):
        B[i] = float(input(f"B[{i+1}]: "))

    print("\nMatriz B:")
    for i in range(n):
        print("{:.2f}".format(B[i]))

    erro = float(input("\nInforme o valor do Erro: "))
    k = int(input("\nEntre com o número de iterações: "))

    print("\nEntre com os valores para um chute inicial: ")
    for i in range(n):
        Xi[i] = float(input(f"Xi[{i+1}]: "))

    cont = 0
    para = True

    while para and cont <= k:
        for i in range(n):
            Soma[i] = B[i]
            for j in range(n):
                if i != j:
                    Soma[i] -= A[i][j]*Xi[j]
            X[i] = Soma[i]/A[i][i]
            print("X({}) = {:.4f}".format(i+1, X[i]))
            dif = math.fabs(X[i]) - math.fabs(Xi[i])
            Xi[i] = X[i]
            if math.fabs(dif) > erro:
                para = True
            else:
                para = False
        cont += 1
        print()

    print("\nResultado: ")
    for i in range(n):
        print("X({}) = {:.4f}".format(i+1, X[i]))

    print("\nNúmero de iterações: {}".format(cont))

gaussJacobi()