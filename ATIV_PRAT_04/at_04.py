# 4) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
# calcular e escrever o valor correspondente em graus Celsius (baseado na
# fórmula abaixo):
# c / 5 = (F - 32) / 9

# Entrada de dados
fahrenheit = float(
    input('Digite a temperatura em Fahrenheits para converter em Grau Celsius\n'))

# Processamento
celsius = ((fahrenheit - 32) * (5/9))

# saida de dados
print('')
print(f'--- CONVERSOR DE F({fahrenheit}) FAHRENHEIT PARA CELSIUS ----')
print(f'->>> Celsius C{celsius:.2f}')