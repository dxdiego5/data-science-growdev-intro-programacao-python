# 4) Escreva um programa que receba 3 números, faça a soma dos dois primeiros e
# depois divida o resultado pelo 3º número. Após, exiba o resultado na tela.

# Entrada de dados pelo usuario
num1 = float(input('Digite o primeiro numero: \n'))
num2 = float(input('Digite o segundo numero: \n'))
num3 = float(input('Digite o terceiro numero: \n'))

# OBS: Entre parenteses sera prioridade e calculado a soma primeiro e depois a divisão com os dois numeros já somados
# Processamento dos dados
resultado = (num1 + num2) / num3

# Saida dos dados
print(f'O resultado do calculo é: {resultado}')
