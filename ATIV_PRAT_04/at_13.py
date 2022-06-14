# 13) Sabendo que há 60 segundos em um minuto, 3.600 segundos em uma hora
# e 86.400 segundo em um dia, crie um algoritmo que a partir de uma
# determinada quantidade de segundos fornecida pelo usuário, converte-a da
# seguinte maneira:
# a) Se a quantidade de segundos for maior ou igual a 60, o programa
# deverá exibir o número de minutos equivalente;
# b) Se a quantidade de segundos for maior ou igual a 3.600, o programa
# deverá exibir o número de horas equivalente;
# c) Se a quantidade de segundos for maior ou igual a 86.400, o programa
# deverá exibir o número de dias equivalente.

# Entrada de dados
segundos = int(input('Digite um numero em segundos: \n'))

# Processando e saida de dados
if segundos >= 60:
    minutos = segundos / 60
    print(f' --- Segundos {round(minutos,2)}')
    
if segundos >= 3600:
    horas = minutos / 60
    print(f' --- Hrs {round(horas,2)}')

if segundos >= 86400:
    dias = horas / 24
    print(f' --- Dias {round(dias, 2)}')