# 1)Faça um programa,com um afunção que necessite de três argumentos ,
# eque forneça a soma desses três argumentos.
import os

def sum_num(n1, n2, n3):
    return n1 + n2 + n3

num1 = float(input('Digite o 1 numero: \n'))
num2 = float(input('Digite o 2 numero: \n'))
num3 = float(input('Digite o 3 numero: \n'))

r = sum_num(num1, num2, num3)

os.system('clear')
print(f'A soma de: {num1} + {num2} + {num3} = {r}')