# 2) Faça um programa que peça o nome e as duas notas de 5 alunos, calcule a
# média das notas e armazene nome e média cada uma em uma lista, ao final
# imprima o nome e o número de alunos com média maior ou igual a 7.0.

import os
lista_nomes = []
lista_medias = []

for i in range(3):
    nome = input('Digite seu nome: \n')
    n1 = float(input('Digite a nota 1: \n'))
    n2 = float(input('Digite a nota 2: \n'))
    n3 = float(input('Digite a nota 3: \n'))
    n4 = float(input('Digite a nota 4: \n'))
    media = (n1 + n2) / 2

    lista_nomes.append(nome)
    lista_medias.append(media)

    os.system('clear')

for i in range(3):
    if lista_medias[i] >= 7:
        print(f'Nome: {lista_nomes[i]}, com media: {lista_medias[i]}')
 