# 5) Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e
# colunas, com um número em cada posição e no qual a soma das linhas,
# colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
# lado 3, com números de 1 a 9:
# 8 3 4
# 1 5 9
# 6 7 2
# Elabore uma função que identifica e mostra na tela todos os quadrados
# mágicos com as características acima. Dica: produza todas as combinações
# possíveis e verifique a soma quando completar cada quadrado.
import os
import random
os.system('clear')


def verify_sum(board):
    # soma das linhas
    sum_line_1 = sum(board[0])
    sum_line_2 = sum(board[1])
    sum_line_3 = sum(board[2])

    # soma das colunas
    sum_col_1 = (board[0][0] + board[1][0] + board[2][0])
    sum_col_2 = (board[0][1] + board[1][1] + board[2][1])
    sum_col_3 = (board[0][2] + board[1][2] + board[2][2])

    # soma das diagonais
    sum_diagnal_1 = (board[0][0] + board[1][1] + board[2][2])
    sum_diagnol_2 = (board[0][2] + board[1][1] + board[2][0])

    message = [False, 'A soma do quadrado magíco não bate:']
    if (sum_diagnal_1 == sum_diagnol_2):  # verifica diagonais
        if (sum_col_1 == sum_col_2) and (sum_col_2 == sum_col_3):  # verifica colunas
            if (sum_line_1 == sum_line_2) and (sum_line_2 == sum_line_3):  # verifica linhas
                message = [
                    True, f'Encontramos a combinação!!!, a soma do quadrado magíco da certo é: {sum_line_1}']

    return message


def creating_magic_square():
    # number_game = [8,3,4,1,5,9,6,7,2] # se colocar para teste da certo
    number_game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number_game)

    # criacao zerado do quadrado magico
    board = [[0 for i in range(3)] for j in range(3)]

    index = 0
    for line in range(3):
        for col in range(3):
            # adicionando numeros no quadrado magico
            board[line][col] = number_game[index]
            index += 1

    result_sum = verify_sum(board)  # chama a funcao sum para validar somas
    return {'square': board, 'is_valid': result_sum[0], 'message': result_sum[1]}


index = 0
is_valid = False
while is_valid == False:  # chances para tentar encontrar uma combinacao ou encontrar primeiro o codigo ja para
    res_board = creating_magic_square()  # pega a listas

    print(f'Tentativa numero: {index+1}')
    for i, info in enumerate(res_board['square']):
        print(res_board['square'][i])

    print(res_board['message'])
    print('------------------------------')

    if res_board['is_valid'] == True:  # quando encontrar uma combinacao valida parar o looping
        is_valid = True
        break
    index += 1
