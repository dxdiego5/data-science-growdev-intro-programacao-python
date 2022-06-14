# 3) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a
# porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
# escrever um algoritmo para ler o custo de fábrica de um carro, calcular e
# escrever o custo final ao consumidor.

# percentual do distribuidor seja de 28%
# impostos de 45%
# custo de fábrica de um carro
# o  Custo do carro novo é: Soma custo de fabrica + Porcentagem do distribuidor e dos impos(aplicados ao custo de fábrica).

# Entrada de dados
custo_fabrica = float(input('Digite o valor de fabrica do carro. \n'))

# Processando
porcent_distribuidor = round(custo_fabrica * 0.28, 2)
imposto = round(custo_fabrica * 0.45, 2)
custo_venda = round(custo_fabrica + (porcent_distribuidor + imposto), 2)

# Saida de dados
print('')
print(f'Impostos de 45%: R${imposto}')
print(f'Percentual do distribuidor seja de 28%: R${porcent_distribuidor}')
print(' --- ')
print(f'Custo de fabrica é: R${custo_fabrica}')
print(f'O custo de venda é: R${custo_venda}')