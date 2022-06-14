# 5) Construa um programa que permita a um usuário informar uma série de
# números, até que um número negativo seja fornecido. Ao final, imprima o
# somatório desses números, a média, o valor máximo e o mínimo.
# Desconsidere o último número (negativo) informado pelo usuário.
import os

continuar = True
lista_numeros = []
while continuar == True:
    num = float(input("Digite um valor numerico: \n"))
    
    if num < 0:
        continuar = False
        break
    
    lista_numeros.append(num)
    soma = sum(lista_numeros)
    media = sum(lista_numeros) / len(lista_numeros)
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)
    os.system("clear")

print('\n')
print(f'A soma: {round(soma,2)}')
print(f'A media: {round(media,2)}')
print(f'A minima: {round(minimo,2)}')
print(f'A maxima: {round(maximo,2)}')
print('\n')
