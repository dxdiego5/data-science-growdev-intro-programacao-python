# 9) Escreva um programa que peça ao usuário para fornecer um dia, mês e o
# ano arbitrários e determine se esses dados correspondem a uma data válida.
# Não deixe de considerar que existem meses com 30 e 31 dias, e que
# fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto.
# Considere que um ano é bissexto quando for divisível por 4.

# Input de dad]
dia, mes, ano = int(input('Digite um dia valido [de 1 ate 31]: \n')), int(input('Digite um mes valido [de 1 ate 12]: \n')),int(input('Digite um ano valido: \n'))

print('')
print('-------')

    # Processamento e saida de dados
if (dia > 0 and  dia <= 31) and (mes > 0 and mes <= 12):
    data_valida = True
    anoIs_bissexto = False
    if (ano % 4) == 0: # Ano bissexto
        anoIs_bissexto = True
        if mes == 2 and dia > 29:
            print('ERROR: Data iválida, do ano bissexto')
            data_valida = False
            
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 10) and (data_valida == True):
        if dia > 30:
            print(f'ERROR: Mês {mes} tem no maximo 30 dias, data inválida')
            data_valida = False
    else:
        if mes == 2 and dia >= 29 and (anoIs_bissexto == False):
            print('ERROR: Data iválida')
            data_valida = False
            
    if data_valida == True:
        print('Data é valida!')

else:
    print('ERROR: Data é invalida!')
###
print('-------')