# 17) Receba 3 notas de um aluno e peça o peso (em porcentagem) respectivamente de cada nota, ao final exiba a nota final do mesmo.

# Entrada de dados
(n1, n2, n3) = float(input('Digite a NOTA 1 \n')), float(
    input('Digite a NOTA 2 \n')),  float(input('Digite a NOTA 3 \n'))

(p1, p2, p3) = float(input('Digite o PESO DA NOTA 1 \n')), float(
    input('Digite o PESO DA NOTA 2 \n')),  float(input('Digite o PESO DA NOTA 3 \n'))

# Variaveis de inicializações e CONVERSÕES DE PESOS EM PORCENTAGEM %
p1 = p1 / 100
p2 = p2 / 100
p3 = p3 / 100

# Processamento
MP = ((p1 * n1) + (p2 * n2) + (p3 * n3)) / (p1 + p2 + p3)

# Saida de dados
print('')
print('--------- MEDIA PONDERADA ----------')
print('')

# condicional de passou ou não de ano 
if MP >= 7:
    print(f'A MÉDIA É: {MP} -> APROVADO')
else:
    print(f'A MÉDIA É: {MP} -> REPROVADO')

print('----------------------------------')
