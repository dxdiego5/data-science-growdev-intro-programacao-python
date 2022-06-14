# 1) Faça um Programa que leia um vetor de 10 números reais e mostre-os na
# ordem inversa.
import os
num = []

for i in range(1, 11):
    n = int(input(f'Digite o {i} numero: \n')) 
    num.append(n)
    os.system('clear')

num.reverse()
print(f' \n {num} \n ')