VALOR_PAO_FRANCES = 0.75
VALOR_PAO_DOCE = 0.85
VALOR_QUINDIM = 1.5

print("Informe a quantidade de produtos vendidos:")

print("Pão Frances: ")
pao_frances = int(input())

print("Pão Doce: ")
pao_doce = int(input())

print("Quindim: ")
quindim = int(input())

total_vendido = pao_frances * VALOR_PAO_FRANCES + pao_doce * VALOR_PAO_DOCE + quindim * VALOR_QUINDIM

print("Total fatura: {}".format(total_vendido))