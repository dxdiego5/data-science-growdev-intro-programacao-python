# 10)Implemente um programa onde o usuário deve adivinhar as letras de uma
# palavra por meio de palpites. A palavra deve ser mostrada inicialmente com
# as letras substituídas por underlines, conforme exemplo abaixo.
# dados => _ _ _ _ _
# O usuário deve então palpitar sobre as letras que ele julga estarem na frase.
# A cada letra que errar, ele perde 1 ponto. A cada letra que ele acertar a
# mesma deve ser exibida na tela, exemplo:
# Palpite: d
# Saída: d _ d _ _
# Se completar a frase o usuário ganha o jogo, se sua pontuação zerar ele
# perde o jogo. Ao iniciar o jogo, a pontuação é de 4 pontos.
import os
import random
import json

# se nao tiver a lib, instale a com cmd dentro do projeto:[ pip install pathlib ]
import pathlib # para ler arquivos

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve() # pega exatamente a ultima pasta ate no projeto raiz
DATA_PATH = BASE_PATH.joinpath("frases.json").resolve() # adiciona ao camniho o arquivo que queira abrir

with open(DATA_PATH,'r') as file:
    # palpites do jogo, tipo do arquivo em json
    game_guesses = json.load(file) 

# escolha aleatoria da palavra a ser jogada
phrase_game = random.choice(game_guesses)

attempts = 1
hits = 0

# montando o tamanho do frase vazia de acordo com o tamanho da mesma
phrase_digit = ['_' for i in range(len(phrase_game['phrase']))]
size_phrase = len(phrase_game['phrase']) - phrase_game['phrase'].count(' ') 

# deixando somente as letras unicas, para validacao de repeticao de palavras
unique_digits = list(set(phrase_game['phrase']))
while ' ' in unique_digits:
    unique_digits.remove(' ')

print(unique_digits)
# looping enquanto existe as tentativas e acertos totais nao tiverem chegado ao fim
while (attempts <= phrase_game['chances']) and (hits <= size_phrase):
    os.system('clear')
    print('----------------------------------')
    # prints de inicializacao na tela
    print(f'Tentativa numero: {attempts} de {phrase_game["chances"]} chances! \n')
    print(f'{phrase_game["reference"]} \n')
    print(f'Frase:  {phrase_digit} \n')

    # entrada de dados do usuario
    t = input('Digite uma letra para o palpite: \n')

    hit_valid = False
    # looping da palavra e verificacao se existe a letra e faz a colocacao da mesma nos indices corretos
    for i, info in enumerate(phrase_game['phrase']):
        # verifica se a letra ja foi digitada e acertada entao se nao tiver na lista NAO acertou
        if t in unique_digits:
            if info.lower() == t.lower():
                # compara a letra digitada com a posicao da frase e faz a troca do '_' pela letra certa
                phrase_digit[i] = info.upper()
                hit_valid = True
                hits += 1
    # se usuario errou a palavra,soma tentativa +1, se ele acertou continua com as chances
    if hit_valid == False:
        attempts += 1
    else:
        # apos a insercao das palavras certa digitada, aqui remove a letra acertada, para validacao de dados repetidos
        while t in unique_digits:
            unique_digits.remove(t)  # enquanto a letra [t] existir remova

    # Print de dados na tela apos o palpite
    print(f'Tentativa numero: {attempts} de {phrase_game["chances"]} chances! \n')
    print(f'{phrase_game["reference"]} \n')
    print(f'Frase:  {phrase_digit} \n')

    # se usuario acertou tudo antes de acabar as chances fim de game [WIN]
    if hits == size_phrase:
        print(f'Você ganhou antes de acabar as tentativas!!!')
        print('----------------------------------  \n')
        break

    # se acabou as chances antes de acertar tudo fim de game [LOSS]
    if attempts == phrase_game['chances']:
        print(f'Você perdeu acabou suas tentativas!!!')
        print('-- GAME HOVER --')
        print('----------------------------------  \n')
        break
