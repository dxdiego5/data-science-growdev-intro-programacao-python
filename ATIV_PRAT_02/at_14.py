# 14) Escreva um programa que leia dois números e faça a adição, subtração, divisão e multiplicação
# dos dois números, e após, exiba os 4 resultados calculados.

# Entrada de dados
(num1, num2) = float(input('Digite o 1º numero: \n')), float(
    input('Digite o 2º numero: \n'))

# Processando dados
adicao = num1 + num2
multi = num1 * num2
divisao = num1 / num2
subtracao = num1 - num2

# Saida de dados
print('----------------------------------------')
resultado = f'--------- Adição --- ({num1} + {num2}) = {adicao} \n'
resultado += f'-------- Divisão --- ({num1} / {num2}) = {divisao} \n'
resultado += f'------ Subtração --- ({num1} - {num2}) = {subtracao} \n'
resultado += f'-- Multiplicação --- ({num1} * {num2}) = {multi}'
print(resultado)
print('----------------------------------------')