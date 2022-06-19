# 5) Faça um programa completo utilizando funções e classes que:
# a) Possui uma classe chamada Ponto, com os atributos x e y.
# b) Possui uma classe chamada Retângulo, com os atributos
# largura e altura.
# c) Possui uma função para imprimir os valores da classe Ponto.
# d) Possui uma função para encontrar o centro de um retângulo.
# e) Você deve criar alguns objetos da classe Retangulo.
# f) Cada objeto deve ter um vértice de partida, por exemplo, o
# vértice inferior esquerdo do retângulo, que deve ser um objeto
# da classe Ponto.
# g) A função para encontrar o centro do retângulo deve retornar o
# valor para um objeto do tipo ponto que indique os valores de x
# e y para o centro do objeto.
# h) O valor do centro do objeto deve ser mostrado na tela

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_point(self):
        print(f'x={self.x}, y={self.y}')


class Rectangle:
    def __init__(self):
        self.point_1 = None
        self.point_2 = None

    def center(self):
        point_center = Point()
        point_center.x = (self.point_1.x + self.point_2.x) / 2
        point_center.y = (self.point_1.y + self.point_2.y) / 2
        return point_center

ret = Rectangle()

ret.point_1 = Point(4,3)
ret.point_2 = Point(10,7)

center_point = ret.center()

center_point.get_point()