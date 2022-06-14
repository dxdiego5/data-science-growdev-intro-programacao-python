# Desafio
# Crie um algoritmo que funcione como um jogo de loteria, conforme as seguintes regras:
# a) O algoritmo deve gerar três números aleatórios entre 0 e 9;
# b) O usuário deve fornecer um palpite com três números, também entre 0 e 9;
# c) Cada um dos palpites do usuário deve ser comparado com os números
# aleatórios, de acordo com a tabela abaixo:

# Números Correspondentes Número de pontos
# Nenhum número coincidente 0
# Acertar um número 10
# Acertar dois números 100
# Acertar os três números, mas não na mesma ordem em que foram gerados 1000
# Acertar três números na mesma ordem que os números aleatórios 1.000.000
import random

# Gerando o jogos
jogo_gerad = random.sample(range(0,9), 3)
jogo_ap = []
acertos = []
indice = 1
pontos = 0

# Entrada de dados e jogo gerado por
while indice < 4:
    jogo_ap.append(int(input(f'Digite o {indice}º de 3 para o sorteio: regras ->[digite de 0 ate 9] \n')))
    indice +=1

# Processamento e saida de dados
print('')
print('------------')
if (jogo_gerad[0] == jogo_ap[0]) and (jogo_gerad[1] == jogo_ap[1]) and (jogo_gerad[2] == jogo_ap[2]):
    pontos = 1000000
    ponto_max= True
    acertos = jogo_gerad
    print(f'Acertou os 3 numeros na sequencia:')

else: # Não acertou 3 numero corretos na sequencia, então ponto maximo recebe [False]
    ponto_max=False 
    
if ponto_max == False:
    for i in jogo_gerad:
        if (i == jogo_ap[0]) or (i == jogo_ap[1]) or (i == jogo_ap[2]):
            acertos.append(i)
    # -----------
    # Verificação de acertos de 1 até 3 sem ter sido em sequencia
    if len(acertos) == 1:
        pontos = 10
    elif len(acertos) == 2:
        pontos = 100
    elif len(acertos) == 3:
        pontos = 1000

# Saida de dados
print(f'Total de Pontos: {pontos}')
print(f'Numeros Apostado: {jogo_ap}')
print(f'Numeros Sorteado: {jogo_gerad}')
print(f'Numeros de Acertos: {len(acertos)} de 3')
print('------------')