# 21) Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para calcular seu rendimento, e
# la deverá fornecer o valor constante da aplicação mensal, a taxa e o número de meses.
# abendo-se que a fórmula usada para este cálculo é:
#  onde:
# ● i = taxa
# ● P = aplicação mensal
# ● n= número de meses
# Crie um programa que receba os coeficientes necessários e realize o cálculo.

# Entrada dos dados ..
(n, p, i) = int(input('Quantos meses de aplicação? \n')), float(
    input('Qual o valor da aplicação mensal? \n')), float(input('Qual o TAXA? \n'))


#  𝑃*(1+𝑖)n −1 / 𝑖  [[ FORMULA PASSADA PELO TUTOR ]]
# Processamento de dados
taxa = i / 100  # taxa convertida em porcentagem (%)
VF = ((p * ((1 + taxa)**n)) - 1) / taxa

# Saida de dados
print('')
print('------- EXTRATO DE RENDIMENTO --------')
print('')
print(
    f'Em uma aplicação de R$ {p} reais por {n} meses. Você tera em sua conta o total de R$ {VF:.2f}')
print('--------------------------------------')