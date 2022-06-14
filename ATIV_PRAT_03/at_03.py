# 3) Um brechó revende produtos usados, e fixa o preço de venda de cada
# produto conforme o valor de sua aquisição. Se o preço de aquisição de um
# produto é menor do de R$ 50.00, ele deve ser vendido por um preço 45%
# maior; caso contrário, o lucro será de 30%. Sabendo disso, construa um
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de
# venda.

# Entrada de dados
val_aquis_prod = float(input('Qual o valor de aquisição do produto: \n'))

val_venda = 0 # variavel de inicialização 

# processamento
## Condição de venda se valor menor do que 50 reais(vender por 45% a mais)
if val_aquis_prod < 50:
    val_venda = (val_aquis_prod * 0.45)
    val_venda += val_aquis_prod
    print(f'O valor da venda é R${round(val_venda,2)} eo valor da aquisição foi de R${round(val_aquis_prod,2)}')

else: # se for maior do que 50 reais (vender por 30% a mais)
    val_venda = (val_aquis_prod * 0.30)
    val_venda += val_aquis_prod
    print(f'O valor da venda é R${round(val_venda,2)} eo valor da aquisição foi de R${round(val_aquis_prod,2)}')

# pronto