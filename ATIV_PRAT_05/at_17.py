# 17) Crie um programa para que retorne o somatório de todos os números entre 1
# e um valor fornecido pelo usuário. Por exemplo, se o usuário fornecer o
# número 4, o computador deverá calcular o somatório 1+ 2 + 3 + 4 = 10.
numero = int(input('Digite um valor: \n'))
soma = []

for i in range(1, (numero+1)):
    soma.append(i)

print(f'A soma do numeros da lista {soma} \n --- É: {sum(soma)}')