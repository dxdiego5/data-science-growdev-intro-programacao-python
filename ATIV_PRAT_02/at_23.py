# 23) - Faça um programa que receba um valor no intervalo entre 0 e 1000, e converta para o valor correspondente ao intervalo -1 e 1.

# Entrada de dodos
num = float(input("Digite um valor entre [0] e [1000] \n"))

# validação simples de numero
if num >= 0 and num <= 1000:
    # processamento de conversão
    num = (num / 500) -1

    # Saida de dados
    print('')
    print('-----------------------')
    print(f'REULTADO DA CONVERSÃO: {num}')
    print('-----------------------')
else:
    # Erro se numero nao for valido
    print(' ERROR: ---- Valor digitado não é válido!!')