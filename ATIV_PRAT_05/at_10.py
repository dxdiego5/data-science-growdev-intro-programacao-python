# 10)Escreva um programa que recebe 10 valores e imprima o somatório dos
# elementos.
import os
soma = 0
for i in range(1,11):
    info = float(input('Digite uma valor: \n'))
    soma += info
    os.system('clear')

print(f' A soma dos elementos e: {soma}')