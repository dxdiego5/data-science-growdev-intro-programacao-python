# 19)Faça um programa que receba os coeficientes a, b e c da equação a seguir, e encontre as raízes por meio da fórmula de bhaskara.
# 𝑎𝑥2 + 𝑏𝑥 + 𝑐

# seguindo a formula de {"bhaskara"}

# Entrada de dados
(a, b, c) = float(input('Digite o valor de A: \n')), float(
    input('Digite o valor de B: \n')), float(input('Digite o valor de C: \n'))

# Processamento
delta = (b**2 - 4*a*c)
val_1 = (-b + delta**(1/2)) / (2*a)
val_2 = (-b - delta**(1/2)) / (2*a)

# Saida de dados
print('')

print('---- As duas raízes da equação do segundo 2ªgrau ----')
print('')
print(f'Valor da raíz 1: {val_1}')
print(f'Valor da raíz 2: {val_2}')
print('-----------------------------------------------------')
