# 4) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
# elementos intercalados dos dois outros vetores.
import os 

vetor_1 = []
vetor_2 = []
for i in range(0, 5):
    vetor_1.append(input('Digite um valor para o vetor [1]: \n'))
    vetor_2.append(input('Digite um valor para o vetor [2]: \n'))
    os.system('clear')

vetor_3 = []
for v1, v2 in zip(vetor_1, vetor_2):
    vetor_3.append(v1)
    vetor_3.append(v2)

print('\n')
print(f'VETOR 1: {vetor_1} \n')
print(f'VETOR 2: {vetor_2} \n')
print(f'VETOR 3: (vetor1 + vetor2) intercalado: {vetor_3} \n')
print('\n')
