# 15) Um cliente de uma loja está comprando cinco produtos. Crie um programa que solicite o
# preço de cada um desses produtos e, em seguida,
# exiba o subtotal da venda, o valor do
# imposto e o valor total (subtotal da venda mais o valor do imposto).
# Suponha que a alíquota do imposto seja de 6% sobre o subtotal da venda.

import os
# dados de inicialização e pesos
produtos = ['Arroz', 'Feijao', 'Macarrao', 'Tomate', 'Bife']
sub_total = 0
valor_total = 0
valor_imposto = 0

# Entrada de dados
for i in (produtos):
    informacao = float(input(f'Digite o valor do - [ {i} ]: \n'))
    sub_total += informacao
    os.system('clear')  # no windows cls

# Processamento
valor_total = sub_total + (sub_total * 0.06)
valor_imposto = (sub_total * 0.06)

# Saida de dados
print(f'---------------------- SUB_TOTAL -- R$ {sub_total:.2f}')
print(f'----------------- IMPOSTO de 6% --- R$ {valor_imposto:.2f}')
print(f'--- (IMPOSTO + SUB_TOTAL), TOTAL -- R$ {valor_total:.2f}')
