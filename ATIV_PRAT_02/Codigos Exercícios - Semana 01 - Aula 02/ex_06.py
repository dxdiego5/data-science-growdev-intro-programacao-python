from math import sqrt
#from math import sqrt, pow

print("Informe a coordenada X do ponto 1: ")
ponto_1_x = int(input())

print("Informe a coordenada Y do ponto 1: ")
ponto_1_y = int(input())

print("Informe a coordenada X do ponto 2: ")
ponto_2_x = int(input())

print("Informe a coordenada Y do ponto 2: ")
ponto_2_y = int(input())

distancia = sqrt((ponto_1_x - ponto_2_x) * (ponto_1_x - ponto_2_x) + (ponto_1_y - ponto_2_y) * (ponto_1_y - ponto_2_y))
distancia = sqrt(pow(ponto_1_x - ponto_2_x, 2) + pow(ponto_1_y - ponto_2_y, 2))

print("Distância: {}".format(distancia))