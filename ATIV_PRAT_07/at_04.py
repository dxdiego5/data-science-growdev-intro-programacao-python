# 4) Construa uma função que desenhe um retângulo usando os caracteres ‘+’ ,
# ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo
# que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
# valores fora da faixa forem informados, eles devem ser modificados para
# valores dentro da faixa.
import os

os.system('clear')


def create_rectangle(line, column):
    c = ''
    #comands = ['_','+','|']
    for i in range(line):
        for j in range(column):
            if j == column or j == 0:
                c += '+'
            else:
                c += ' - '
        c += f'|\n'

    p = 'Retangulo [horizontal]'
    if line > column:
        p = 'Retangulo [VERTICAL]'

    # retorno de dados
    return c + f'\n {p} \n'


valid = False
while valid == False:
    print('\n')
    line = int(input('Digite um numro para linha de [1 ate 20]: \n'))
    column = int(input('Digite um numro para coluna de [1 ate 20]: \n'))

    os.system('clear')

    if (line >= 1 and line <= 20) and (column >= 1 and column <= 20):
        valid = True
        break

print(create_rectangle(line, column))
