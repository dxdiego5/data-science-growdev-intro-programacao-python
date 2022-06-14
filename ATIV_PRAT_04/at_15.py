# 15) Construa um algoritmo que, a partir de duas cores primárias fornecidas pelo
# usuário, determine qual cor seria obtida pela mistura delas. As cores
# vermelho, azul e amarelo são chamadas de cores primárias porque não
# podem ser obtidas a partir de outras cores e, quando misturadas, resultam
# numa cor secundária, de acordo com as seguintes regras:
# a) vermelho + azul = roxo;
# b) vermelho + amarelo = laranja;
# c) azul + amarelo = verde.
# Se o usuário inserir algo diferente de “vermelho”, “azul” ou “amarelo”, o
# programa deverá exibir uma mensagem de erro. Caso contrário, o programa
# deve exibir o nome da cor secundária resultante.

lista_cor_primaria = ['vermelho','azul','amarelo']

# Entrada de dados
cor_1 = input('Digite [V] - Para vermelho | Digite [A] - Para azul ou Digite [M] - Para amarelo: \n')
cor_2 = input('Digite [V] - Para vermelho | Digite [A] - Para azul ou Digite [M] - Para amarelo: \n')

# Saida e processamento de dados
print('')
print('------')
if cor_1.upper() == "V" and cor_2.upper() == "A":
    print('VERMEHLO + AZUL = ROXO')
elif cor_1.upper() == "V" and cor_2.upper() == "M":
    print('VERMEHLO + AMARELO = LARANJA')
elif cor_1.upper() == "A" and cor_2.upper() == "M":
    print('AZUL + AMARELO = VERDE')
else:
    print('Vocé digitou errado ou não selecionou um cor correta!')
    
print('------')