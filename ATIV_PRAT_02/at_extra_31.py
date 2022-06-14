# 31) Uma empresa vende um produto a R$5,40 a unidade. Sabendo-se
# que existe um desconto acumulado de 0,5% do valor total da compra
# a cada centena comprada deste produto. Escreva um algoritmo que
# receba a quantidade comprada desse produto e informe.
# a) O valor total da compra (sem o desconto)
# b) A quantidade de centenas compradas desse produto
# c) O desconto em R$.
# d) O valor total da compra (com desconto)

# valores de inicialização e pesos
preco_unit_produto = 5.40
desconto = 0.05  # levando em consideração que o desconto é de meio% (0.05)

# Entrada de dados ...
quantidade_produto = int(input('Digite a quantidade de produtos comprados \n'))

# Processamento dos dados e formatação
valor_bruto_total = quantidade_produto * preco_unit_produto
quant_centenas = int(quantidade_produto / 100)

# Valores de inicialização [padrão]
centenas = 'O numero não possui a casa das centenas.'
descont_message = 'Não houve desconto quantidade minima não atende aos requisitos.'

if quantidade_produto > 99:  # Verificação de numero ter casa das centenas

    centenas = (f'{quantidade_produto}')[-3]# Sempre vai pegar o antepenultimo numero que é a centena
    centenas = f'O numero da centena é: [ {centenas} ] do total de {quant_centenas} centenas dentro do numero {quantidade_produto}'

    # Conversões e porcentagens de descontos
    total_porc_desconto = (quant_centenas * desconto)
    total_porc_desconto = float(f'{total_porc_desconto:.2f}')

    descont_message = f'DESCONTO TOTAL DE R$ {(valor_bruto_total * total_porc_desconto):.2f} \n'
    descont_message += f'------ Porcentagem(%) total de desconto é de {total_porc_desconto}%'

print(f'--------------------------------------------------')
print(f'------ Quant X [{quantidade_produto}] unidades compradas')
print(f'------ {centenas}')
print(f'------ {descont_message}')
print('')
print(f'------ VALOR TOTAL (SEM DESCONTO) R$ {valor_bruto_total:.2f}')
print(f'------ VALOR TOTAL (COM DESCONTO) R$ {valor_bruto_total - (valor_bruto_total * total_porc_desconto):.2f}')
print(f'--------------------------------------------------')