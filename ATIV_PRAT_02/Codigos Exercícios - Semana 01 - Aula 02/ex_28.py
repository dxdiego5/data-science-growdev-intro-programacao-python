print("Informe o primeiro número: ")
n1 = float(input())

print("Informe o segundo número: ")
n2 = float(input())

print("Informe o terceiro número: ")
n3 = float(input())

frac_1 = n1 % 1
frac_2 = n2 % 1
frac_3 = n3 % 1

soma = frac_1 + frac_2 + frac_3

print("Soma: {}".format(soma))