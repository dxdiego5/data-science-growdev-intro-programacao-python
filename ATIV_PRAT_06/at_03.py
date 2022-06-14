# 3) Modifique o programa anterior para que utilize apenas uma lista e em cada
# posição da lista armazene um dicionário com o nome e a média.

import os
alunos = []

for i in range(3):
    nome = input('Digite seu nome: \n')
    n1 = float(input('Digite a nota 1: \n'))
    n2 = float(input('Digite a nota 2: \n'))
    n3 = float(input('Digite a nota 3: \n'))
    n4 = float(input('Digite a nota 4: \n'))
    media = (n1 + n2) / 2

    aluno = {'nome':nome, 'media':media}
    alunos.append(aluno)
    os.system('clear')

for i in range(3):
    aluno = alunos[i]
    if aluno['media'] >= 7:
        print(f'Nome: {aluno["nome"]}, com media: {aluno["media"]}')
 