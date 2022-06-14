# 4) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos. A prefeitura deseja
# saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$2000,00.
# Escreva um programa que receba as informações necessárias de 5 pessoas
# conforme a descrição e responda às questões a, b, c e d anteriores.
import os

filhos = []
salario = []
percent_pessoa = 0
for i in range(1, 6):
    print('')
    print(f'Pesquisa numero: {i}')
    salario.append(float(input('Qual é o seu salário atual: \n')))
    filhos.append(int(input('Quantos filhos você tem: \n')))

    if salario[(i-1)] <= 2000:
        percent_pessoa +=1

    os.system('clear')

# a) média do salário da população;
media_salario = sum(salario) / 5

# b) média do número de filhos;
media_filhos = sum(filhos) / 5

# c) maior salário;
maior_salario = max(salario)

# d) percentual de pessoas com salário até R$2000,00.
percent = (percent_pessoa * 100) / 5

print('')
print('------------------')
print(f'A media do salários de a cordo com a pesquisa é de: {round(media_salario, 2)}')
print(f'A media de filhos de a cordo com a pesquisa é de: {round(media_filhos, 2)}')
print(f'O maior salário da pesquisa é de: R$ {round(maior_salario, 2)}')
print(f'O percentual de pessoas com salário até R$2000,00. é de: {round(percent, 2)}%')
print('')