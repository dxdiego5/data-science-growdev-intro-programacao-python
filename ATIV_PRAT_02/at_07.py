# 7) Escreva um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.
# Considere ano = 365 dias, mês = 31 dias.

# Entrada de dados pelo usuario
(idade, meses, dias) = int(input('Quantos anos você tem? \n')), int(
    input('Quantos meses de vida? \n')), int(input('E quantos dias? \n'))

# Processamento de dados
total_dias = ((idade * 365) + (meses * 31)) + dias

# saida de dados
print(f'Você ja viveu {total_dias} dias, uauuu !!!')