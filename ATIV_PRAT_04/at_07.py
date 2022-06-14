# 7) Após construir o algoritmo anterior, crie mais duas versões dele para prever
# as seguintes situações:

# a) Um aluno pode ficar em recuperação se possuir frequência suficiente
# (superior a 75%) e média superior a 5 mas inferior a 7;

# b) Caso um aluno reprove por média e faltas, sua situação deve ser

# “Reprovado por Média e Faltas” (ao invés de simplesmente
# “Reprovado por Faltas” como antes).

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
percentual_presenca = ((aulas - faltas) / aulas) * 100

print(media)
print(percentual_faltas)
print(percentual_presenca)

# Saida de dados
print('')
print('------')
if media >= 7 and percentual_presenca >= float(75): # se meida (true) e presenca (true) = aprovado
    print(f'Aluno APROVADO por nota média de: {media} e APROVADO por presença')
    
elif  media >= 7 and percentual_faltas > float(25): # se meida (true) e presenca (false) = reprovado falta
    print(f'Aluno com média: {media}, mas REPROVADO po faltas de {percentual_faltas}% mínimo de 25% de presença')

elif percentual_faltas > 25 and media < 7: # se faltas (true) e meida (true) = reprovado em ambas
    print(f'Aluno REPROVADO por por média: {media} e REPROVADO por faltas de {percentual_faltas}% mínimo de 25% de presença')

# Se faltas minimo 75% presenca(true) e meida minima 5 e maxima 6.9 (true) = recuperação
elif percentual_presenca > float(75) and media > 5 and media < 7: 
    print(f'O aluno ficou de RECUPERAÇÃO média: {media} e presença de: {percentual_presenca}%')

elif percentual_faltas <= 25 and media < 7: # se faltas (true) e meida (true) = reprovado em ambas
    print(f'Aluno REPROVADO por por média: {media}')
else:
    print('Algo deu errado')
print('------')