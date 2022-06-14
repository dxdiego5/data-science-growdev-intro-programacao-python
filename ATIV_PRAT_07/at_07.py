# 7) Faça uma função que recebe por parâmetro o tempo de duração da produção
# de uma peça em uma fábrica expressa em segundos e exibe esse tempo em
# horas, minutos e segundos.
import os

os.system('clear')

def production_time(time):
    os.system('clear')
    # conversao em segundos
    min_1 = 60 # segundos de 1 minuto
    hour_1 = 3600 # segundos de uma hora
    day_1 = 86400 # segundos de um dia
    
    days = int(time / day_1) # convertendo segundos em dias
    new_time = time - (days * day_1) # removendo os segundos do dias encontrado

    hours = int(new_time / hour_1) # convertendo segundos em horas
    new_time = new_time - (hours * hour_1) # removendo os segundos das horas encontrado

    minutes = int(new_time / min_1) # convertendo segundos em minutos
    new_time = new_time - (minutes * min_1) # removendo os segundos dos minutos encontrado

    seconds = new_time # o tempo que sobrou foi somento os segundos
    return f'Conversão por extenso do tempo de produção da peça: \n {days} Dias, {hours} Horas, {minutes} Minutes, {seconds} Segundos'

time = int(input('Digite um numero em segundos para calcular o tempo de produção: \n'))
time_p = production_time(time)
print('\n')
print(time_p)
print('\n')
