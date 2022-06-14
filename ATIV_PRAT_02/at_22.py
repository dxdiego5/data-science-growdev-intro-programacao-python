# 22) Uma receita de biscoitos exige os seguintes ingredientes para produzir 48 unidades:
# a) 1,5 xícaras de açúcar
# b) 1 xícara de manteiga
# c) 2,75 xícaras de farinha
# Crie um algoritmo que pergunte ao usuário quantos biscoitos ele deseja fazer e calcule a quantidade correspondente dos ingredientes.

# Entrada de dados
biscoitos = int(input('Quantos biscoitos deseja fazer? \n'))

# variaveis de inicialização de pesos
unid_xic_acucar = 1.5 / 48    # 0.031 | xícaras de açúcara produzir uma unidade
unid_xic_manteiga = 1 / 48    # 0.020 | xícaras de manteiga produzir uma unidade
unid_xic_farinha = 2.75 / 48  # 0.572 | xícaras de farinha produzir uma unidade

# processamento
acucar = unid_xic_acucar * biscoitos
manteiga = unid_xic_manteiga * biscoitos
farinha = unid_xic_farinha * biscoitos

# Saida de dados
print(f'---------- INGREDIENTES NECESSARIOS PARA FAZER {biscoitos} BISCOITOS -------')
print(f'{acucar:.2f} Xícaras de açúcar')
print(f'{manteiga:.2f} Xícaras de manteiga')
print(f'{farinha:.2f} Xícaras de farinha')
print('----------')