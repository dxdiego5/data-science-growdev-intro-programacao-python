from math import sqrt

print("Resolução de Equação do 2° grau")

print("Informe o coeficiente a")
a = int(input())

print("Informe o coeficiente b")
b = int(input())

print("Informe o coeficiente c")
c = int(input())

x1 = (-b + sqrt(b * b - 4 * a * c)) / 2 * a
x2 = (-b - sqrt(b * b - 4 * a * c)) / 2 * a

print("Raíz 1: {}".format(x1))
print("Raíz 2: {}".format(x2))