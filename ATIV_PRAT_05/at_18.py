# 18) Desenvolver um programa que leia um número não determinado de valores
# e calcule e escreva a média aritmética dos valores lidos, a quantidade de
# valores positivos, a quantidade de valores negativos e o percentual de
# valores negativos e positivos.
from statistics import mean
import os

media = 0
num = []
negativos = 0
positivos = 0
perc_positivos = 0
perc_positivos = 0
continua = False

while continua == False:
    valor = float(input('Digite um valor: \n'))
    num.append(valor)
    media = mean(num)

    if valor < 0:
        negativos += 1
    else:
        positivos += 1

    total = (negativos + positivos)
    perc_positivos = (positivos * 100) / total
    perc_negativos = (negativos * 100) / total

    info = int(
        input('Digite um [1] para continuar, ou digitute [0] para terminar: \n'))
    os.system('clear')

    if int(info) == 1:
        pass
    else:
        continua = True


print(5 * '--')
print(f'A media e: {media}')
print(f'Total de positivos: {positivos}')
print(f'Total de negativos: {negativos}')
print(f'Percentual negativos: {perc_negativos}')
print(f'Percentual positivos: {perc_positivos}')