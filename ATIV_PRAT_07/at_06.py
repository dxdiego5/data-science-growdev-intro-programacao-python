# 6) Escreva um programa para solicitar ao usuário o raio r de uma esfera, e
# calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize
# a seguinte fórmula para determinar o volume:
# v = (4.0 / 3.0) * π * r3
import math

def calc_volume(radius):
    
    V = (4/3) * math.pi * (radius**3)
    return V

radius = float(input('Digite um valor para podermos medir o raio de uma esfera: \n'))
volume = calc_volume(radius)
print(f'O volume da esfera de raio: {radius} é: {round(volume,2)}')