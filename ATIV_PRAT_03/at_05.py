# 5) Escreva um algoritmo que leia três números fornecidos pelo usuário e mostre
# se a soma de dois deles resulta no terceiro.

# entrada de dados
(num1,  num2, num3) = float(input('Digite o primeiro numero: \n')),float(input('Digite o segundo numero: \n')),float(input('Digite o terceiro numero: \n'))

# Processamento
if (num1 + num2) == num3:
    # saida de dados
    print(f'SIM, A soma do primeiro numero [{num1}] + o segundo [{num2}] é igual [{num1 + num2}], ')
else:
    # saida de dados
    print(f'NÃO, a soma do primeiro com segundo numero não é igual ao terceiro')

# pronto