# 1) Escrever um programa que lê 5 valores para a, um de cada vez, e conta
# quantos destes valores são negativos, escrevendo esta informação.

negativos = 0

for var in range(5):
    dado = (float(input('Digite valores numericos negativos ou positivos: \n')))
    if dado < 0:
        negativos += 1

print(f'quantia de numeros negativos digitados: {negativos}')