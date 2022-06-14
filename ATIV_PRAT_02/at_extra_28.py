# 28) Escreva um programa que receba 3 valores e some as partes decimais de todos eles. Ex: 5.6, 2.3, 8.0, resultado deve ser 0.9.

# Entrada de dados
(v1, v2, v3) = float(input('Digite o primeiro valor: \n ')), float(input(
    'Digite o segundo valor: \n ')), float(input('Digite o terceiro valor: \n '))

soma_decimal = 0 # Variavel de inicialização

# Processamento
for a in (v1, v2, v3):
    decimal_str = f'{a}'.split('.')[1] # Transformando o numero em string e quebrando no ponto e separando somento o decima na posição [1]
    soma_decimal += float(f'0.{decimal_str}') # Convertendo em inteiro novamente para efetuar a soma

# Saida de dados
print(f'O valor dos decimais somados são: {soma_decimal:.2f}')