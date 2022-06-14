# 6) Numa determinada escola, os critérios de aprovação são os seguintes:
# a) O aluno deve ter, no máximo, 25% de faltas;
# b) A nota final deve ser igual ou superior a 7,00.

# Construa um algoritmo para ler as notas que um aluno tirou nos 4 bimestres,
# o número total de aulas e o número de faltas, mostrando ao final a situação
# do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por
# média”, considerando que a reprovação por faltas se sobrepõe a reprovação
# por nota.

# Entrada de dados
notas = []
print('-----------NOTAS-----------')
notas = float(input('Digite a nota do 1ºBimestre: \n')),float(input('Digite a nota do 2ºBimestre: \n')),float(input('Digite a nota do 3ºBimestre: \n')),float(input('Digite a nota do 4ºBimestre: \n'))

# Entrada de dados
print('-----------AULAS E FALTAS-----------------')
aulas, faltas = int(input('Quantas aulas teve este ano: \n')),int(input('Quantas faltas teve este ano: \n')) 

# Processamento de dados
media = round(sum(notas) / len(notas), 2)
percentual_faltas = round((faltas * 100) / aulas, 2)

# Saida de dados
print('')
print('------')
if percentual_faltas >= float(25): # validando aprovanção por presença 
    print(f'Aluno REPROVADO por [faltas] com um total de {percentual_faltas}% mínimo de 25% \n' 
          f'de presença aluno faltou {faltas} de um total de {aulas} aulas')
    
else: 
    if media >= float(7):
        print(f'Aluno APROVADO por nota média de: {media} e APROVADO por presença')
    else:
        print(f'Aluno REPROVADO por nota média de: {media}')
print('------')