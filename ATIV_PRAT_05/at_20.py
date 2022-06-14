# 20) Escreva um programa que leia um valor inicial A e uma razão R e imprima
# uma sequência em P.G. contendo 10 valores.
import os
a = int(input('Digite um valor: \n'))
razao = int(input('Digite um valor para razao: \n'))
pg = [] 
for i in range(1,11): 
    pg.append(a)
    a = a * razao

print(pg)