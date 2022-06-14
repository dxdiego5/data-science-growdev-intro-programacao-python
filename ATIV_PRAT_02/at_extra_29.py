# 29) Crie um algoritmo que calcule e exiba a conversão de uma determinada quantidade
# em reais em moedas de R$1.00, R$0.5, R$0.25, R$0.1, R$0.05 e R$0.01.
# Por exemplo, R$3.78 resulta em três moedas de um real,
# uma de cinquenta centavos, duas de dez centavos, uma de 5 centavos e três de um centavo.

# Entrada de dados
moeda = float(input('Digite o valor de uma moeda. \n'))

# Inicialização dos pesos zerados em arraays para furuas soma
moeda_modificada = moeda
moeda_1_real = []
moeda_50_centavos = []
moeda_25_centavos = []
moeda_10_centavos = []
moeda_5_centavos = []
moeda_1_centavos = []

# Inicio do processamento
while moeda_modificada > float(0):
    verificado = False  # essa é uma condição para verificar se ja entrou em algum if para depois não entra novamento e fazer o calculo errado

    # Verifica se valor entra no stagio de contagem para 1 real
    if moeda_modificada >= float(1):
        moeda_1_real.append(float(1))
        moeda_modificada -= float(1)
        verificado = True

    if verificado == False:
        # verifica se valor entra no stagio de contagem para 0.5 centavos
        if moeda_modificada >= float(0.5) and moeda_modificada < float(1):
            moeda_50_centavos.append(float(0.5))
            moeda_modificada -= float(0.5)
            verificado = True

    if verificado == False:
        # verifica se valor entra no stagio de contagem para 0.25 centavos
        if moeda_modificada >= float(0.25) and moeda_modificada < float(0.5):
            moeda_25_centavos.append(float(0.25))
            moeda_modificada -= float(0.25)
            verificado = True

    if verificado == False:
        # verifica se valor entra no stagio de contagem para 0.1 centavos
        if moeda_modificada >= float(0.10) and moeda_modificada < float(0.25):
            moeda_10_centavos.append(float(0.10))
            moeda_modificada -= float(0.10)
            verificado = True

    if verificado == False:
        # verifica se valor entra no stagio de contagem para 0.05 centavos
        if moeda_modificada >= float(0.05) and moeda_modificada < float(0.10):
            moeda_5_centavos.append(float(0.05))
            moeda_modificada -= float(0.05)
            verificado = True

    if verificado == False:
        # verifica se valores entra no stagio de contagem para 0.01 centavos
        if moeda_modificada < float(0.05):
            moeda_1_centavos.append(float(0.01))
            moeda_modificada -= float(0.01)
            verificado = True

    # Essa linha codigo abaixo transforma o resultado do processo em um valor com 2 casas decimais
    # se tirar essa linha o codigo continua a funcionar porem com uma margem de erro de 0.01 centavos, em alguns casos
    moeda_modificada = float(f'{moeda_modificada:.2f}')

# Fim do while aqui

# Saida de dados
print('')
print(f'---- CONVERTENDO R$ {moeda} ----')
print(f'----> [ {len(moeda_1_real)} ] X 1 REAL, TOTAL R$ {sum(moeda_1_real)}')
print(
    f'----> [ {len(moeda_50_centavos)} ] X 0.50 CENTAVOS TOTAL R$ {sum(moeda_50_centavos)}')
print(
    f'----> [ {len(moeda_25_centavos)} ] X 0.25 CENTAVOS TOTAL R$ {sum(moeda_25_centavos)}')
print(
    f'----> [ {len(moeda_10_centavos)} ] X 0.10 CENTAVOS TOTAL R$ {sum(moeda_10_centavos)}')
print(
    f'----> [ {len(moeda_5_centavos)} ] X 0.05 CENTAVOS TOTAL R$ {sum(moeda_5_centavos)}')
print(
    f'----> [ {len(moeda_1_centavos)} ] X 0.01 CENTAVOS TOTAL R$ {sum(moeda_1_centavos)}')