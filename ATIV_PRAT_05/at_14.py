# 14) Desenvolver um programa que efetue a soma de todos os números ímpares
# que se encontram no conjunto dos números de 1 até 500.
soma_impar = []
for i in range(1,500, 2):
    soma_impar.append(i)

# Resultado 62500
print(f'A soma dos impares é: {sum(soma_impar)}')