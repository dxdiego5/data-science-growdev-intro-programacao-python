# 18)As Organizações XTC resolveram dar um aumento de salário aos seus
# colaboradores e lhe contrataram para desenvolver o programa que calcula os
# reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:

# a) salários até R$ 280,00 (incluindo): aumento de 20%
# b) salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# c) salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# d) salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado informe na tela:

# a) o salário antes do reajuste;
# b) o percentual de aumento aplicado;
# c) o valor do aumento;
# d) o novo salário, após o aumento.

salario = float(input('Digite o valor do salário, para calcular o reajuste! \n'))

salario_atualizado = 0
percentual_aumento = 0
percent_reajuste = 0

# Processando de dados
if salario <= 280: 
    percent_reajuste = 0.20
    percentual_aumento = salario * percent_reajuste
    salario_atualizado += (salario + percentual_aumento)

elif salario > 280 and salario <= 700:
    percent_reajuste = 0.15
    percentual_aumento = salario * percent_reajuste
    salario_atualizado += (salario + percentual_aumento)

elif salario > 700 and salario <= 1500:
    percent_reajuste = 0.10
    percentual_aumento = salario * percent_reajuste
    salario_atualizado += (salario + percentual_aumento)
    
elif salario > 1500:
    percent_reajuste = 0.05
    percentual_aumento = salario * percent_reajuste
    salario_atualizado += (salario + percentual_aumento)
else:
    print('Error, deve ter digitado algo invalido!')

# Saida de dados
print('')
# a) o salário antes do reajuste;
print(f'----- O salário antes do reajuste: R$ {salario:.2f}')
print(f'----- O percentual de aumento aplicado: {percent_reajuste:.2%}')
print(f'----- O valor de aumento: R${percentual_aumento:.2f}')
print(f'----- O novo salário, após o aumento: R$ {salario_atualizado:.2f}')
print('-------')