# 2) Escrever um programa que lê um valor N inteiro e positivo e que calcula seu
# valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1

numero = int(input('Digite um valor: \n'))
fatorial = 1

for n in range(numero, 1, -1):
    fatorial = fatorial * n

print("{}! = {}".format(numero, fatorial))