# 2)Faça um programa,com uma função que necessite de um argumento.
# A função retorna o valor de caractere‘P’,se seu argumento for positivo,e‘N’,se seu argumento for zero ou negativo
import os

def validator(variant):
    return f'O valor {variant} é [P] - Positivo' if variant > 0 else f'O valor {variant} é [N] - Negativo ou ZERO'

print('\n')
val = float(input('Digite um valor numierico positivo ou negativo: \n'))
r = validator(val)
os.system('clear')
print(r)