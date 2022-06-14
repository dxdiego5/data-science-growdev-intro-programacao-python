# 24) Escreva um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.
# Considerar que a média é ponderada e que o peso das notas é: 20%, 30% e 50%, respectivamente.

# Entrada de dados
(n1, n2, n3) = float(input('Digite a NOTA 1 \n')), float(
    input('Digite a NOTA 2 \n')),  float(input('Digite a NOTA 3 \n'))

# Variaveis de inicializações e CONVERSÕES DE PESOS EM PORCENTAGEM %
p1 = 20 / 100
p2 = 30 / 100
p3 = 50 / 100

# Processamento 
MP = ((p1 * n1) + (p2 * n2) + (p3 * n3)) / (p1 + p2 + p3)

# Saida de dados
# condicional de passou ou não de ano 
if MP >= 7:
    print(f'A MÉDIA É: {MP} -> APROVADO')
else:
    print(f'A MÉDIA É: {MP} -> REPROVADO')
print('----------------------------------')