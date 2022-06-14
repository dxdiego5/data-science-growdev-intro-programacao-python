# 3) Escrever um programa que lê um valor N inteiro e positivo e que calcula e
# escreve o valor de E.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / N!

numero = int(input('Digite um valor: \n'))
somatorio = 1

for i in range(1, (numero+1)):
    fatorial = 1
    for valor in range (i,1 -1):
        fatorial = fatorial * valor

    somatorio = somatorio + 1 / fatorial

print(f'E: {somatorio}')