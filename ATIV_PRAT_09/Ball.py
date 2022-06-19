# 1) Crie uma classe que modele uma bola:
# a) Atributos
# i) Cor
# ii) Circunferência
# iii) Material
# b) Métodos
# i) troca_cor
# ii) mostra_cor

class Ball:
    def __init__(self, color='branco', material='couro', circuferencia=10):
        self.color = color
        self.material = material
        self.circuferencia = circuferencia

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


b = Ball()  # criacao da instancia para o objeto
b.set_color('amarelo')  # altera o valor do atributo
print(b.get_color())
b.set_color('verde')  # altera o valor do atributo
print(b.get_color())

# resultado do print
# amarelo
# verde
