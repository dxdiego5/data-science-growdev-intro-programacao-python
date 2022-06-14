# 6) Crie um programa que leia continuamente a altura e o sexo de uma lista de
# pessoas salvando todas as informações em listas, até que uma altura
# negativa seja fornecida. Ao final, sabendo que a média de altura para as
# mulheres brasileiras é de 1.60m e a dos homens brasileiros é de 1.73m,
# escreva as seguintes informações:
#
# a) quantas mulheres da lista estão acima da média nacional de altura
# para mulheres, e quantas estão abaixo;mulheres brasileiras é de 1.60m

# b) quantos homens da lista estão acima da média nacional de altura para
# homens, e quantos estão abaixo.homens brasileiros é de 1.73m,
import os

low_women = 0
low_men = 0
taller_women = 0
taller_men = 0
list_of_people = []

next_p = True
while next_p == True:
    print('\n')
    gender = input(
        'Qual o seu genero: \n  Digite [F] para feminino e Digite [M] para masculino: \n')
    print('\n')
    height = int(input('Qual a sua altura em CM inteiro (EX:180): \n'))
    os.system('clear')

    if height < 0:
        next_p = False
        break

    if gender.upper() == 'F':
        if height <= 160:
            low_women += 1
        else:
            taller_women += 1

    if gender.upper() == 'M':
        if height <= 173:
            low_men += 1
        else:
            taller_men += 1

    list_of_people.append({'gender': gender, 'height': height})

print('\n')
print(f' Tem {taller_women} mulheres acima da media de 1.60m \n')
print(f' Tem {low_women} mulheres abaixo da media de 1.60m \n')
print('\n')
print('-----------')
print('\n')
print(f' Tem {taller_men} homens acima da media de 1.73m \n')
print(f' Tem {low_men} homens abaixo da media de 1.73m \n')
print('\n')
print('\n')
print(f'Segue a lista abaixo: \n {list_of_people}')
print('\n')