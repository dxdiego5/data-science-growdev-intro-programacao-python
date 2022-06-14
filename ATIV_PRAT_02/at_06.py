# 6) Escreva um programa que receba a posição de dois pontos em um espaço 2D, ou seja,
# cada ponto tem coordenadas x e y,
# e calcule a distância entre esses dois pontos, exibindo-a na tela.

# FORMULA = dAB² = (xB – xA)² + (yB – yA)².

# Entrada de dados, coordenadas do ponto A(x,y)
(xA, yA) = float(input('Digitie a coordenada "X" do PONTO "A": \n')), float(
    input('Digitie a coordenada "Y" do PONTO "A": \n'))
print('----------')

# Entrada de dados, coordenadas do ponto B(x,y)
(xB, yB) = float(input('Digitie a coordenada "X" do PONTO "B": \n')), float(
    input('Digitie a coordenada "Y" do PONTO "B": \n'))
print('----------')

# Processamento dos dados
distancia_A_B = (((xB - (xA))**2) + ((yB - (yA))**2))
distancia_A_B = distancia_A_B ** 0.5

# Saida dos dados
print('')
print('---------- RESULTADO DOS CALCULOS ----------')
print(f'Coordenadas ponta "A": x{xA,yA}y')
print(f'Coordenadas ponta "B": x{xB,yB}y')
print(f'A distancia entre o ponta "A" e "B" é: [{distancia_A_B:.2f}]')
print(f'"A" <---------[{distancia_A_B:.2f}]---------> "B"')
print('')