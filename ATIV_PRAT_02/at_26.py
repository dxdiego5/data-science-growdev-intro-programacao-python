# 26) Escreva um programa que aceite uma quantidade de minutos e o converta em horas e dias.
# Por exemplo, 6.000 minutos equivalem a 100 horas e é igual a 4.167 dias.

# Entrada de dados
num = int(input('Digite um numero em minutos para conversão em (Horas e Dias) \n'))

# processamento de conversão
hora = num / 60
dia = hora / 24

# Saida de dadps 
print('')
print('------ CONVERSOR DE MINUTOS PARA HORA E DIA --------')
print(f'{hora:.2f} Hr(s)')
print(f'{dia:.1f} Dia(s)')
print(f'{num} Minuto(s)')
print('----------------------')