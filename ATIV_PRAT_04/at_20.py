# 20) Faça um programa que leia as duas notas parciais obtidas por um aluno
# numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
# de conceitos obedece à tabela abaixo:
# Média de Aproveitamento
# Entre 9.0 e 10.0 ||| A
# Entre 7.5 e 8.9  ||| B
# Entre 6.0 e 7.4  ||| C
# Entre 4.0 e 5.9  ||| D
# Entre 0 e 3.9    ||| E  
 
# O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem:
# a) APROVADO se o conceito for A, B ou C.
# b) REPROVADO se o conceito for D ou E.
import os

# Entrada de dados
notas = []
notas = float(input('Digite a nota do 1º Semestre: \n')),float(input('Digite a nota do 2º Semestre: \n'))

os.system('clear')

# Processamento da media
media = sum(notas) / len(notas)

print('---------')
# verificação e saida de dados
if media >= 0 and media <= 3.9:
    print(f'Média: {round(media, 2)}')
    print(f'Conceito aplicado: (E)')
    print(f'Status do aluno: REPROVADO')
elif media >= 4.0 and media <= 5.9:
    print(f'Média: {round(media, 2)}')
    print(f'Conceito aplicado: (D)')
    print(f'Status do aluno: REPROVADO')
elif media >= 6.0 and media <= 7.4:
    print(f'Média: {round(media, 2)}')
    print(f'Conceito aplicado: (C)')
    print(f'Status do aluno: APROVADO')
elif media >= 7.5 and media <= 8.9:
    print(f'Média: {round(media, 2)}')
    print(f'Conceito aplicado: (B)')
    print(f'Status do aluno: APROVADO')
elif media >= 9.0 and media <= 10.0:
    print(f'Média: {round(media, 2)}')
    print(f'Conceito aplicado: (A)')
    print(f'Status do aluno: APROVADO')

print('---------')