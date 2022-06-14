# 16) Faça um programa que receba o cateto oposto e o cateto adjacente de um triângulo e retorne a hipotenusa do mesmo.

# FORMULA c² = a² + b²

# Entrada de dados
print('--- CALCULANDO A HIPOTENUSA DE UM TRIANGULO ---')
(a, b) = float(input('Digite o valor para o [ cateto oposto ]: \n')), float(
    input('Digite o valor para o [ cateto adjacente ]: \n'))

# Processamento 
val = ((a**2) + (b**2))
c = val ** 0.5  # tirando a raiz quadrada

# Saida dos dados
print('')
print(f'--- O VALOR DA HIPOTENUSA É: {c:.3f}')
print('')