# Enunciado:
# 1) Procure quem foi a pessoa que mais gastou?
from functions import convert_data_files, conv_monetary

# chamada da funcao de leitura de arquivo
data_frame = convert_data_files.init_app()

higher_value = -1  # maior valor de compra
position = 0
for indice, person_row in enumerate(data_frame):
    # se valor atual e maior do que o valor da pessoa anterior da lista
    if (higher_value) < person_row['compra']:
        higher_value = person_row['compra']
        position = indice
# ------- END FOR -------

print(f"\n{'=':=^70}")
print(f' \n O {data_frame[position]["nome"]} {data_frame[position]["sobrenome"]} de {data_frame[position]["idade"]} anos \n teve o mais gasto em compras no valor total de R$ {conv_monetary.init_app(data_frame[position]["compra"])} reais, em {data_frame[position]["ano"]}. \n')
print(f"{'=':=^70}\n")

# resposta do print abaixo:
#  O Gabriel Pereira de 67 anos
#  teve o mais gasto em compras no valor total de R$ 9998.0 reais, em 2016.
