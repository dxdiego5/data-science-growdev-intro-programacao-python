# Enunciado:
# 5) Qual foi o ano com maior gasto?
from functions import conv_data_files, conv_monetary

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

spent_per_year = []  # valores gasto por ano
years_of_list = []  # lista de anos unicos  da base de dados

def spent_per_year_sum(year, price):  # pega valor do ano que esta para adicionar
    for i in spent_per_year:
        if i["year"] == year:
            i["total_spent"] += price
    return i

for index, data in enumerate(data_frame):
    is_exist = data['ano'] in years_of_list

    if is_exist == True:
        spent_per_year_sum(data['ano'], data['compra'])
    else:  # entrar aqui quando o ano nunca exisitiu na contagem
        d = {
            'year': data['ano'],
            'total_spent': data['compra']
        }
        spent_per_year.append(d)
        years_of_list.append(data['ano'])

 # lista anos agrupados com valores
list_year_spent = [[info['total_spent'], info['year']]for i, info in enumerate(spent_per_year)]
                   
year_spent_total_max = max(list_year_spent)  # pega o ano de maior gasto
year_spent_total_min = min(list_year_spent)  # pega o ano de menor gasto
message_max = f'O ano com MAIOR gasto foi de {year_spent_total_max[1]}, com um total de R$ {conv_monetary.init_app(year_spent_total_max[0])} reais.'
message_min = f'O ano com MENOR gasto foi de {year_spent_total_min[1]}, com um total de R$ {conv_monetary.init_app(year_spent_total_min[0])} reais.'

print(f"\n{'=':=^75}")
print(message_max)
print(f"{'-':=^75}")
print(message_min)
print(f"{'=':=^75}\n")

# resposta do print abaixo:
# O ano com MAIOR gasto foi de 2016, com um total de R$ 1.812.226,00 reais.
# =====================================-=====================================
# O ano com MENOR gasto foi de 2008, com um total de R$ 1.475.291,00 reais.