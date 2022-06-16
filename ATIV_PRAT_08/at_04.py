# Enunciado:
# Qual foi o gasto por ano?
from functions import convert_data_files, conv_monetary

# chamada da funcao de leitura de arquivo
data_frame = convert_data_files.init_app()

sale_per_year = []  # valores sale per year
years_of_list = []  # lista de anos unicos  da base de dados


def sale_per_year_sum(year, price):  # pega valor do ano que esta para adicionar
    for i in sale_per_year:
        if i["year"] == year:
            i["total_sale"] += price
    return i


for index, data in enumerate(data_frame):

    is_exist = data['ano'] in years_of_list

    if is_exist == True:
        sale_per_year_sum(data['ano'], data['compra'])
    else:  # entrar aqui quando o ano unca exisitiu na contagem
        d = {
            'year': data['ano'],
            'total_sale': data['compra']
        }
        sale_per_year.append(d)
        years_of_list.append(data['ano'])

for data in sale_per_year:
    val = conv_monetary.init_app(data["total_sale"])
    print(
        f'No ano de ({data["year"]}) o faturamento de vendas foi de R$ {val}')

# resposta do print abaixo:
# No ano de (2006) o faturamento de vendas foi de R$ 1.671.499,00
# No ano de (2005) o faturamento de vendas foi de R$ 1.542.645,00
# No ano de (2010) o faturamento de vendas foi de R$ 1.611.940,00
# No ano de (2007) o faturamento de vendas foi de R$ 1.711.268,00
# No ano de (2018) o faturamento de vendas foi de R$ 1.778.911,00
# No ano de (2019) o faturamento de vendas foi de R$ 1.717.606,00
# No ano de (2008) o faturamento de vendas foi de R$ 1.475.291,00
# No ano de (2009) o faturamento de vendas foi de R$ 1.518.779,00
# No ano de (2015) o faturamento de vendas foi de R$ 1.514.146,00
# No ano de (2011) o faturamento de vendas foi de R$ 1.668.563,00
# No ano de (2012) o faturamento de vendas foi de R$ 1.642.695,00
# No ano de (2017) o faturamento de vendas foi de R$ 1.645.386,00
# No ano de (2016) o faturamento de vendas foi de R$ 1.812.226,00
# No ano de (2014) o faturamento de vendas foi de R$ 1.671.750,00
# No ano de (2020) o faturamento de vendas foi de R$ 1.515.322,00
# No ano de (2013) o faturamento de vendas foi de R$ 1.647.590,00
