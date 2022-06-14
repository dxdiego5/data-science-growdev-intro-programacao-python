# 3) Construa uma função que receba uma data no formato DD/MM/AAAA e
# devolva uma string em um formato por extenso. Opcionalmente, valide a data
# e retorne NULL caso a data seja inválida.
import datetime
import os


def convert_date(date):
    valid_date = None
    if date.count('/') == 2:  # valida se tem 2 barras na data digitada
        try:
            date = date.split('/')
            datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
            valid_date = True
        except ValueError:
            return f'[{valid_date}] Data não é valida!'
    else:
        return f'[{valid_date}] Data não é valida!'

    if valid_date == True:
        if int(date[1]) == 1:
            date[1] = 'Janeiro'
        elif int(date[1]) == 2:
            date[1] = 'Fevereiro'
        elif int(date[1]) == 3:
            date[1] = 'Março'
        elif int(date[1]) == 4:
            date[1] = 'Abril'
        elif int(date[1]) == 5:
            date[1] = 'Maio'
        elif int(date[1]) == 6:
            date[1] = 'Junho'
        elif int(date[1]) == 7:
            date[1] = 'Julho'
        elif int(date[1]) == 8:
            date[1] = 'Agosto'
        elif int(date[1]) == 9:
            date[1] = 'Setembro'
        elif int(date[1]) == 10:
            date[1] = 'Outubro'
        elif int(date[1]) == 11:
            date[1] = 'Novembro'
        elif int(date[1]) == 12:
            date[1] = 'Dezembro'
        return f'dia {date[0]} de {date[1]} de {date[2]}'


date = input('Digite uma data EX:DD/MM/AAAA: \n')
os.system('clear')

print('\n')
print(convert_date(date))
print('\n')
