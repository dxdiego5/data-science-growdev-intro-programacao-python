# 1) Escreva um algoritmo que receba dois números, exiba as opções:
# a) 1 - adição
# b) 2 - subtração
# Então peça ao usuário para escolher uma das opções. Caso escolha a opção
# 1 o algoritmo deve realizar a soma dos dois números lidos e exibir. Caso
# escolha a opção 2 o algoritmo deve realizar a subtração dos dois números
# lidos e exibir.

num1, num2 = float(input('Digite o primeiro numero: \n')), float(input('Digite o segundo numero: \n'))

op = int(input("Escolha uma opção: \n [1] - Adição \n [2] - Subtração \n"))

if op == 1:
    soma = num1 + num2
    print(f'Você selecionou a opção [1] - resultado da adição: %s' % soma)
elif op == 2:
    subtracao = num1 - num2
    print(f'Você selecionou a opção [2] - o resultado da subtração: %s' % subtracao)
else:
    print('Opção digitada está incorreta! ...')