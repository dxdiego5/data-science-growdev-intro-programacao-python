# 5) Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
# metro e cresce 3 centímetros por ano. Construa um programa que calcule e
# imprima quantos anos serão necessários para que Zé seja maior que Chico

chico = 1.50
ze = 1.10
ze_E_maior = False
contador_ano = 0

while ze_E_maior == False:
    chico += 0.02
    ze += 0.03
    if (ze > chico):
        ze_E_maior = True
    
    contador_ano += 1

print('')
print(f'Zé precisa de {contador_ano} anos para ficar maior do que o Chico \n')
print(f'Altura de Zé: {round(ze,2)}')
print(f'Altura de Chico: {round(chico,2)}')
print('')