# Enunciado:
# 2) Busque qual são os anos da base de dados?
from functions import convert_data_files

# chamada da funcao de leitura de arquivo
data_frame = convert_data_files.init_app()

years_of_list = []
for data in data_frame:
    years_of_list.append(data['ano'])

# lista unica de anos em ordem crescente
years_uniques = sorted(list(set(years_of_list)))

print(f"\n{'=':=^70}")
print(
    f'Os anos registrado na base de dados vão de {years_uniques[0]} ate o ano de {years_uniques[-1]} \n\nA lista completa: {years_uniques}')
print(f"{'=':=^70}\n")

# resposta do print abaixo:
# Os anos registrado na base de dados vão de 2005 ate o ano de 2020
# A lista completa: [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
