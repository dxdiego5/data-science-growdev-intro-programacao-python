# 10) Construa um algoritmo que leia uma data qualquer (dia, mês e ano) e calcule
# a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro
# tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.

dia, mes, ano = int(input('Digite um dia valido [de 1 ate 31]: \n')), int(input('Digite um mes valido [de 1 ate 12]: \n')),int(input('Digite um ano valido: \n'))

# Processamento e saida de dados
data_valida = True
anoIs_bissexto = False
novo_dia = dia
novo_mes = mes
novo_ano = ano

# Processamento de dados referente ao dia
if (ano % 4) == 0: # Ano bissexto
    anoIs_bissexto = True
    if mes == 2 and dia >= 29:
        novo_dia = 1
    elif mes == 2 and dia < 29:
        novo_dia += 1
else:
    if mes == 2 and dia >= 28:
        novo_dia = 1
    elif mes == 2 and dia < 28:
        novo_dia += 1
    # ---
    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 10): # Processamento de dia quando vai ate 30
        if dia >= 31:
            novo_dia = 1
        elif dia > 1 and dia < 31:
            novo_dia += 1
    elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 10) or (mes == 12): # Processamento de dia quando vai ate 31
        if dia >= 31:
            novo_dia = 1
        elif dia > 1 and dia < 31:
            novo_dia += 1 
# ------
# Processamento de dados referente ao mes
if novo_dia == 1 and mes < 12:
    novo_mes += 1
elif novo_dia > 1 and novo_dia <= 31 and mes < 12:
    novo_mes = mes
elif novo_dia == 1 and mes == 12:
    novo_mes = 1 # ano novo

# ------
# Processamento de dados referente ao ano
if novo_mes == 1:
    novo_ano += 1
else: 
    novo_ano = ano

# Saida de dados
print('------')
print(f'DATA ANTIGA: {dia}-{mes}-{ano}')
print(f'DATA NOVA: {novo_dia}-{novo_mes}-{novo_ano}')
print('------')