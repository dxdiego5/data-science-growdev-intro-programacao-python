# 8) Crie uma estrutura bidimensional utilizando listas com sublistas para para
# representar um tabuleiro (1 lista com 20 elementos e cada elemento é uma
# lista de 20 elementos, tabuleiro 20x20). Cada posição irá armazenar 1 valor
# numérico que significa:
# 0 - Água
# 1 - Navio
# Para cada posição escolha esses valores aleatoriamente, respeitando a regra
# de que não podem existir mais de 20 navios no tabuleiro. Após os valores
# serem distribuídos, o programa deve pedir ao usuário uma posição do
# tabuleiro e informar se ele acertou um navio ou água e repetir o procedimento
# até que o usuário derrote todos os navios ou chegue ao limite de 35
# tentativas.
import os
from random import randint

board = [[0 for i in range(20)] for i in range(20)]

coord_ships = [] 
def create_coord_ships(): # criando coordenadas dos navios = 1
    while len(coord_ships) <= 20: # Enquanto nao tiver os 20 navios faca criacao das coord   
        line = randint(0,19)
        column = randint(0,19)
        operation = [line, column] in coord_ships
        
        if operation == True:
            create_coord_ships() # funcao recursiva
        else:
            coord_ships.append([line,column])
            board[line][column] = 1
    return

# chamando funcao de criaca ode coordenadas e agregacao aleatoria de navios
create_coord_ships() 

hits = 0
attempt = 0
hits_in_water = 0
hits_in_sequenced = 0
sequenced = 1

# printa as coordenadas para testar os acertos
print(coord_ships) 

while hits < 20 and attempt <= 35:
    print('\n')
    print(f'TENTATIVA: {attempt + 1}')
    x_line = int(input('Digite um coordenada X para linha: de [0 ate 19]: \n'))
    y_column = int(input('Digite um coordenada Y para coluna: de [0 ate 19]: \n'))

    operation = [x_line, y_column] in coord_ships
    if operation == True:
        print('Acertou o navio!!!')
        hits +=1
        if sequenced > 0:
            if  hits_in_sequenced <= sequenced:
                hits_in_sequenced = sequenced
        sequenced += 1

    else:
        print('Foi na agua!!!')
        hits_in_water += 1
        sequenced = 0

    porcentage_water = (hits_in_water * 100) / (hits_in_water + hits)
    porcentage_hits = (hits * 100) / (hits_in_water + hits)

    attempt +=1

    print('-------')
    print(f'Maior acertos em sequencia: {hits_in_sequenced}')
    print(f'Acertos: {hits}')
    print(f'Acertos na agua: {hits_in_water}')
    print(f'Tentativas: {attempt}')
    print(f'(%) Na agua: {round(porcentage_water,2)}%')
    print(f'(%) Acertou no navio: {round(porcentage_hits,2)}%')
    print('\n')

os.system('clear')
print('\n')
print('--- GAME FINISH ---')
print(f'Maior acertos em sequencia: {hits_in_sequenced}')
print(f'Acertos: {hits}')
print(f'Acertos na agua: {hits_in_water}')
print(f'Tentativas: {attempt}')
print(f'(%) Na agua: {round(porcentage_water,2)}%')
print(f'(%) Acertou no navio: {round(porcentage_hits,2)}%')
print('\n')
