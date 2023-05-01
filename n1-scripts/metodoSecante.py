import math

def funcao(x):
    return (pow(3,x) -3*x + math.exp(x) - 10 )/(3 - 20)

#x0 = float(input("Informe um valor para 'a' no intervalo [a,b]: "))
#x1 = float(input("\nInforme um valor para 'b' no intervalo [a,b]: "))
#erro = float(input("\nInforme o valor do erro: "))
#Ni = int(input("\nInforme o numero maximo de interacoes: "))
x0 = -5
x1 = -2
erro = 0.001
Ni = 100
c = x1 - x0
cont = 0
x2 = x1

while (abs(funcao(x2)) > erro):
    x2 = x1 - funcao(x1) * ((x1 - x0) / (funcao(x1) - funcao(x0)))
    print(f"{cont+1} \t| {x0} \t| F({x0:.2f}) = {funcao(x0):.4f} \t| {x1} \t| F({x1:.2f}) = {funcao(x1):.4f} \t| {x2} \t| F({x2:.2f})= {funcao(x2):.4f}")
    c = x1 - x0
    x0 = x1
    x1 = x2
    cont += 1
    if cont >= Ni:
        break

print(f"Numero de Iteracoes: " + str(cont))
print(f"Raiz: {x2}.4")
print(f"F({x2}) = {funcao(x2)}.4")