# Enunciado:
# 3) Qual a porcentagem de homens e mulheres na base de dados?
from functions import convert_data_files

# chamada da funcao de leitura de arquivo
data_frame = convert_data_files.init_app()

men = 0
women = 0
for data in data_frame:
    if data['sexo'].upper() == 'M':  # se for homen
        men += 1
    else:  # se for mulher
        women += 1
# ---- END FOR ----

total_people = (men + women)

percent_men = (men * 100) / total_people
percent_women = (women * 100) / total_people

if percent_men > percent_women:  # qual genero fez mais compras
    gender_buys_more = 'homens'
else:
    gender_buys_more = 'mulheres'

print(f"\n{'=':=^70}\n")
print(f'A porcentagem de homens é de {percent_men}%')
print(f'A porcentagem de mulheres é de {percent_women}%')
print(f'Conclusão os(as) {gender_buys_more} vão mais ao mercado, fazer compras.')
print(f"\n{'=':=^70}\n")
# resposta do print abaixo:
# A porcentagem de homens é de 57.16%
# A porcentagem de mulheres é de 42.84%
# Conclusão os(as) homens vão mais ao mercado, fazer compras.