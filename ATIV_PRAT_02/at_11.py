# 11) Sabendo que o lucro anual de uma empresa é, tipicamente, 23% do total de vendas, 
# crie um programa que solicite ao usuário que entre com o valor projetado do total de 
# vendas e, em seguida, calcule e exiba o lucro que deve ser obtido com esse valor.

# Entrada de dados
fatur_bruto_ano = float(input("Qual foi o faturamento BRUTO da empresa este ANO? \n"))

# Processamento ... tirando os 23% de lucro do faturamento total
lucro_ano = fatur_bruto_ano * 0.23

print('')
print(f'--------------------- FATURAMENTO BRUTO TOTAL DO ANO --- R$ {fatur_bruto_ano:.2f} reais')
print(f'--------------------------------- LUCRO TOTAL DO ANO --- R$ {lucro_ano:.2f} reais')
print(f'---------------- PROVISIONAMENTO DE LUCRO MENSAL FOI --- R$ {round((lucro_ano / 12),2)} reais')
print(f'---- PROVISIONAMENTO DE FATURAMENTO BRUTO MENSAL FOI --- R$ {round((fatur_bruto_ano / 12),2)} reais')