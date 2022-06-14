# 5) Escreva um programa que receba como entrada a quantidade de torcedores do 
# time X, do time Y e do time Z, 
# calcula e exibe qual a porcentagem de torcedores de cada time.

# valores de inicialização e pesos
time_X = 0
time_Y = 0
time_Z = 0

# Entrada de dados pelo usuario
time_X = int(input('Digite a quantidade de torcedores do time " X ": \n'))
time_Y = int(input('Digite a quantidade de torcedores do time " Y ": \n'))
time_Z = int(input('Digite a quantidade de torcedores do time " Z ": \n'))

# Processamento dos dados
total_torcedores = time_X + time_Y + time_Z # Soma de todos os pesos para notação do calculo de 100%
porcent_time_X = (time_X * 100) / total_torcedores
porcent_time_Y = (time_Y * 100) / total_torcedores
porcent_time_Z = (time_Z * 100) / total_torcedores

# Saida dos dados
print('-------- DADOS ABAIXO --------')
total_porcent = f'Os 100% representam {total_torcedores} torcedores \n'
total_porcent += f'TIME "X" tem {porcent_time_X:.2f}%, de {time_X} torcedores \n'.format(
    porcent_time_X, time_X)
total_porcent += f'TIME "Y" tem {porcent_time_Y:.2f}%, de {time_Y} torcedores \n'.format(
    porcent_time_Y, time_Y)
total_porcent += f'TIME "Z" tem {porcent_time_Z:.2f}%, de {time_Z} torcedores'.format(
    porcent_time_Z, time_Z)
print(total_porcent)
print('-------- FIM ------------------')