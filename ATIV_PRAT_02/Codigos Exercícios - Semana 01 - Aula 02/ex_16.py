from math import sqrt, pow

print("Informe o cateto oposto: ")
cateto_oposto = float(input())

print("Informe o cateto adjacente: ")
cateto_adjacente = float(input())

hipotenusa = sqrt(pow(cateto_oposto * 2) + pow(cateto_oposto * 2))

print("Hipotenusa: {}".format(hipotenusa))