# Extras
# 27) Conversão de graus Celsius para Fahrenheit –
# Crie um algoritmo que converta graus Celsius em Fahrenheit. A fórmula é a seguinte:
#  𝐹 = 9/5 𝐶 + 32
# O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e,
# em seguida, exiba a temperatura convertida em Fahrenheit.
# Após construir esse algoritmo, modifique-o para que converta graus Fahrenheit em graus Celsius.

# Entrada de dados
celsius = float(
    input('Digite a temperatura em Gráu Celsius para converter para Fahrenheits\n'))

# Processamento
fahrenheit = (celsius * (9/5)) + 32

# saida de dados
print('')
print(f'--- CONVERSOR DE C({celsius}) CELSIUS PARA FAHRENHEIT ----')
print(f'----->>> Fahrenheit F {fahrenheit:.2f}')
print('---------------------------------------------')
print('')

# Entrada de dados
fahrenheit = float(
    input('Digite a temperatura em Fahrenheits para converter em Grau Celsius\n'))

# Processamento
celsius = ((fahrenheit - 32) * (5/9))

# saida de dados
print('')
print(f'--- CONVERSOR DE F({fahrenheit}) FAHRENHEIT PARA CELSIUS ----')
print(f'----->>> Celsius C {celsius:.2f}')
print('---------------------------------------------')