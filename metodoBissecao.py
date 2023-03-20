import math

def f(x):
    return math.exp(x) - pow(x, 3) - pow(x, 2) - 1
def bissecao():
    k = 0
    #a = float(input("Insira o valor a: "))
    #b = float(input("Insira o valor b: "))
    #eps = float(input("Insira o erro: "))
    a = -1
    b = 0.7
    eps = 0.001

    k = 0
    while (b - a) / 2 > eps:
        k += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        print("Iteracao: %d" % k, " Valor de X = %f" % c, " f(x) = %f" % f(c))

    return (a + b) / 2

result = bissecao()
print("Resultado: %f" % result)
zer0 = f(result)
print("F("+ str(result) +") = " + str(zer0))