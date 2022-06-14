# 15) Escreva um programa que imprima na tela para escrever a tabuada de um
# número fornecido pelo usuário, de 1 a 10.
numero = int(input('Digite um valor: \n'))

for i in range(1,11):
    print(f'{i} X {numero} = {i * numero}')