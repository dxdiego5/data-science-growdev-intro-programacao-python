# 7) Escreva um programa que leia 10 valores e encontre o maior e o menor
# deles. Mostre o resultado.

maior = 0
menor = 0
for i in range(10): # range inicia no numero [ 0 ]
    num = float(input('Digite um valor: \n'))

    if i > 0: # pra poder inicializar a variaveis de maior e menor a primeira nao passa
        if num > maior: # se cair aqui e maior
            maior = num
        elif num < maior:# se cair aqui entao e menor
            menor = num
    else:# so cai aqui a primeira vez
        maior = num

print('')
print('-----')
print(f'O numero MAIOR é: {maior}')
print(f'O numero MENOR é: {menor}')
print('-----')