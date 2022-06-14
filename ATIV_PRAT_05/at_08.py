# 8) Escreva um programa que leia a idade e salário de 10 pessoas. Informe em
# seguida:
# a) Qual é a média de idade entre as pessoas?
# b) Quantas pessoas há por faixa etária, considerando:
# i) jovens < 18
# ii) 18 <= adultos < 60
# iii) idosos >= 60
# c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.
import os

salarios = []
idades = []
jovens = 0
salario_jovens = 0
adultos = 0
salario_adultos = 0
idosos = 0
salario_idosos = 0
faixa_eta_maior_salario = 0

for i in range(1, 11):
    print('')
    print(f'Pesquisa numero: {i}')
    salarios.append(float(input('Qual é o seu salário atual: \n')))
    idades.append(int(input('Qual é a sua idade: \n')))

# b) Quantas pessoas há por faixa etária, considerando:
    if idades[i-1] < 18:
        jovens += 1
        salario_jovens += salarios[i-1]
    elif idades[i-1] >= 18 and idades[i-1] < 60:
        adultos += 1
        salario_adultos += salarios[i-1]
    elif idades[i-1] >= 60:
        idosos += 1
        salario_idosos += salarios[i-1]

    os.system('clear')

# a) Qual é a média de idade entre as pessoas?
media_idade = sum(idades) / len(idades)

# c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.
messagem = ''
if salario_jovens > salario_adultos and salario_jovens > salario_idosos:
    messagem = f'JOVENS, com valor acumulado de R$ {salario_jovens}'
elif salario_adultos > salario_jovens and salario_adultos > salario_idosos:
    messagem = f'ADULTOS, com valor acumulado de R$ {salario_adultos}'
else:
    messagem = f'IDOSOS, com valor acumulado de R$ {salario_idosos}'

print('')
print('------')
print(f'a média de idade entre as pessoas é: {media_idade} \n')
print(
    f'Quantas pessoas há por faixa etária é: \n  b. Jovens [{jovens}] \n  b. Adultos [{adultos}] \n  b. Idosos [{idosos}] \n')
print(f'Faixa etária com maior acumulo de salario é: {messagem}')
print('------')
