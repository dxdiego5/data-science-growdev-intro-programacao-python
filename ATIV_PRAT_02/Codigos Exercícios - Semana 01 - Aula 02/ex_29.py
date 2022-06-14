print("Informe a quantidade em reais: ")
reais = float(input())

# R$1.00, R$0.50, R$0.25, R$0.10, R$0.05 e R$0.01

moedas_1 = reais - reais % 1

reais -= moedas_1

moedas_50 = reais / 0.5
moedas_50 -= moedas_50 % 1
reais -= moedas_50 * 0.5

moedas_25 = reais / 0.25
moedas_25 -= moedas_25 % 1
reais -= moedas_25 * 0.25

moedas_10 = reais / 0.1
moedas_10 -= moedas_10 % 1
reais -= moedas_10 * 0.1

moedas_05 = reais / 0.05
moedas_05 -= moedas_05 % 1
reais -= moedas_05 * 0.05

print(reais)

moedas_01 = reais / 0.01
moedas_01 -= moedas_01 % 1
reais -= moedas_01 * 0.01

print("Moedas 1: {}".format(moedas_1))
print("Moedas 50: {}".format(moedas_50))
print("Moedas 25: {}".format(moedas_25))
print("Moedas 10: {}".format(moedas_10))
print("Moedas 5: {}".format(moedas_05))
print("Moedas 1: {}".format(moedas_01))