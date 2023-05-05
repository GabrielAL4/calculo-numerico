def gaussSeidel():

    n = 3
    A = [[0] * (n+1) for i in range(n)]
    for i in range(n):
        eq = input(f"Insira os coeficientes da equacao {i+1} separados por espaço ")
        eq = eq.split()
        for j in range(n):
            A[i][j] = float(eq[j])
        A[i][n] = float(eq[n])

    x0 = [0] * n
    count = 1
    eps = 0.01

    #print('\nCount\tx\ty\tz\n')

    flag = True

    while flag:
        x1 = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x1[j]
            x1[i] = (A[i][n] - s) / A[i][i]

        print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1[0], x1[1], x1[2]))

        e = [abs(x0[i] - x1[i]) for i in range(n)]
        count += 1
        x0 = x1

        flag = all([e[i] > eps for i in range(n)])

    print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n' % (x1[0], x1[1], x1[2]))

gaussSeidel()