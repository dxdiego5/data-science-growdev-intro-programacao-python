# 9) Escreva um programa que receba o nome de 10 pessoas e para cada
# pessoa, o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades:
# a) Rio de Janeiro
# b) Bahia
# c) Minas Gerais
# Após, informar qual foi o destino mais visitado e qual o menos visitado.
import os

index = 0
rj = 0
bh = 0
mg = 0
nenhum = 0
maximo = ''
minimo = ''
menssagem = ''
for i in range(1,5):
    print(f'Pesquisa numero: {i}')
    print('Qual lugar você ja viajou: \n - Digite [R] para Rio de Janeiro' +
        '\n - Digite [B] para Bahia \n - Digite [M] para Minas Gerais \n - Digite [N] para nehuma \n -------------')
    cidade = input()

    os.system('clear')

    rj += 1 if cidade.upper() == 'R' else 0
    bh += 1 if cidade.upper() == 'B' else 0
    mg += 1 if cidade.upper() == 'M' else 0
    nenhum += 1 if cidade.upper() == 'N' else 0
    index += 1

if rj > bh and rj > mg:
    maximo = f'RJ e o maior visitando com {rj} votos'
elif bh > rj and bh > mg:
    maximo = f'BH e o maior visitando com {bh} votos'
elif mg > rj and mg > bh:
    maximo = f'MG e o maior visitando com {mg} votos'

if rj < bh and rj < mg:
    minimo = f'RJ e o menos visitando com {rj} votos'
elif bh < rj and bh < mg:
    minimo = f'BH e o menos visitando com {bh} votos'
elif mg < rj and mg < bh:
    minimo = f'MG e o menos visitando com {mg} votos'

print(maximo)
print(minimo)