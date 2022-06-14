# 13)Faça um programa que leia um valor N e mostre os N termos da Série a
# seguir:
# a) S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m
numero = int(input('Digite um valor: \n'))
n = 1
m = 1
menssagem = 'S= '
soma = 0
for i in range(1,(numero + 1)):
    if i <= 1:
        menssagem += f'{i}/{i} '
    else:
        m = m + 2
        menssagem += f'+ {i}/{m} '

    soma =  soma + i/m

print(menssagem)
print(soma)