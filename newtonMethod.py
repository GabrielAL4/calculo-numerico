import math

#x0 = float(input("Insira o chute inicial 'X(0)': "))
#eps = float(input("Insira o erro: "))
#eps2 = float(input("Insira o segundo erro: "))
#it = int(input("Insira o numero de iterações: "))
x0 = -1
eps = 0.01
eps2 = 0.01
it = 100

def f(x):
    return pow(4, x) * math.log(4) + x

def derivada(x):
    return pow(math.log(2), 2) * pow(2, 2*x + 2) +1

if (math.fabs(f(x0))) < eps:
    xFinal = x0
else:
    k = 1
    flag = True

    while flag:
        x1 = x0 - (f(x0) / derivada(x0))
        print("Iteracao: %d" % k, " Valor de X = %f" % x1, " f(x) = %f" % f(x1))
        if (math.fabs(f(x1))) < eps or math.fabs(x1 - x0) < eps2:
            xFinal = x1
            flag = False
        elif(k>=100):
            xFinal = x1
            flag = False
        x0 = x1
        k += 1

print("Resultado: %f" % xFinal)
zer0 = f(xFinal)
print("F("+ str(xFinal) +") = " + str(zer0))
