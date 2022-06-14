# 14) Faça um algoritmo para ler a temperatura atual e conforme leitura, imprima o
# resultado de acordo com a tabela abaixo.

# Temperatura Resultado
# até 15o Muito frio
# de 16o à 22o Frio
# de 23o à 26o Agradável
# de 27o à 30o Quente
# 31o ou mais Muito quente

# Entrada de dados
temp = int(input('Qual a temperatura atual: \n'))

# Processando e saida de dados
if temp <= 15:
    print(f'{temp}º Muito Frio')
elif temp >= 16 and temp <= 22:
    print(f'{temp}º Frio')
elif temp >= 23 and temp <= 26:
    print(f'{temp}º Agradável')
elif temp >= 27 and temp <= 30:
    print(f'{temp}º Quente')
elif temp >= 31:
    print(f'{temp}º Muito quente')