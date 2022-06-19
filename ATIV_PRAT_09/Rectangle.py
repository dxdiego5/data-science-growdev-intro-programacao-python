# 2) Crie uma classe que modele um retângulo:
# a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e
# Altura, a escolher)

# b) Métodos:
# i) Mudar valor dos lados
# ii) Retornar valor dos lados
# iii) Calcular Área
# iv) Calcular Perímetro;

# c) Crie um programa que utilize esta classe. Ele deve pedir
# ao usuário que informe as medidas de um local. Depois,
# deve-se criar um objeto com as medidas e calcular a
# quantidade (em m2) de pisos (1 x 1 m2) e de rodapés
# necessários para o local.
import os


class Rectangle:
    def __init__(self):
        self.sideA = 0
        self.sideB = 0

    def set_sides(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def get_sides(self):
        return self.sideA, self.sideB

    # fórmula A=b⋅h.
    def calc_area(self):
        return self.sideA * self.sideB

    # Perímetro = 2 x (lado A + lado B)
    def calc_perimeter(self):
        return 2 * (self.sideA + self.sideB)

os.system('clear')

sideA, sideB = float(input('Digite quantos mestros tem de comprimento: \n')), float(
    input('Digite quantos mestros tem de largura: \n'))

os.system('clear')

rect = Rectangle()

rect.set_sides(sideA, sideB) # setando valores
floors_m2 = rect.calc_area()# calculando area
footer_m2 = rect.calc_perimeter()# calculando o perimentro

print(f"{'=':=^40}")
print(f'A quantidade de rodapés necessários é {footer_m2} M2.')
print(f'A quantidade de pisos necessários é {floors_m2} M2.')
print(f"{'=':=^40}\n")