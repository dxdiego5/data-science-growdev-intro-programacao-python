from math import pow

print("Informe o valor da aplicação mensal: ")
p = float(input())

print("Informe a taxa: ")
i = float(input())

print("Informe o número de meses: ")
n = float(input())

rendimento = (p * pow(1 + i, n) - 1) / i

print("Rendimento: {}".format(rendimento))