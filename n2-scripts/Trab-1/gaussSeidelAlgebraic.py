def gaussSeidel():

    n = 3
    A = [[0] * (n+1) for i in range(n)]
    for i in range(n):
        eq = input(f"Insira os coeficientes da equacao {i+1} separados por espaco ")
        eq = eq.split()
        for j in range(n):
            A[i][j] = float(eq[j])
        A[i][n] = float(eq[n])

    # definir as condicoes iniciais
    x = [0] * n
    delta = 1e-8
    diff = delta + 1

    # iterar ate que a precisao desejada seja alcancada
    while diff > delta:
        x_old = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (A[i][n] - s) / A[i][i]
        diff = sum(abs(x[i] - x_old[i]) for i in range(n))

    print("A solucao do sistema e:")
    for i in range(n):
        print(f"x_{i+1} = {x[i]:.4f}")

gaussSeidel()