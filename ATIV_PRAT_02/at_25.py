# 25) Escreva um programa que receba um número dentro do intervalo de 1 até 9, e exiba a tabuada desse número.

# Entrada de dados
num = int(input('Digite um numero de 1 até 9 para vermos a tabuada, PODE SER MAIOR QUE 9 TBM VAI FUNCIONAR \n'))

print(f'----- TABUADAD DO {num} -----')

# processamento de looping de um range definido de 1 ate 10
for i in range(1,11):
    # Saida de dados, junto com a multiplicação do indice do range * o numero digitado
    print(f'{num} X {i} = {i * num}')

print('-----')