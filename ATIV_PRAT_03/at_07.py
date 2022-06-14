# 7) Escreva um algoritmo que receba 3 números, faça a soma dos dois primeiros
# e verifique se o resultado da soma é maior que o terceiro número lido.

# entrada de dados
(num1,  num2, num3) = float(input('Digite o primeiro numero: \n')),float(input('Digite o segundo numero: \n')),float(input('Digite o terceiro numero: \n'))

# Processamento
if (num1 + num2) > num3:
    # saida de dados
    print(f'SIM, A soma do primeiro numero [{num1}] + o segundo [{num2}] é [{num1 + num2}], ')
else:
    # saida de dados
    print(f'NÃO, a soma do primeiro com segundo numero não é maior do que o terceiro')

# pronto