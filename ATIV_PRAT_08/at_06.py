# Enunciado:
# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos
# 6) Utilizando as faixas etárias, diga quantas pessoas há em cada faixa?
from functions import conv_data_files, conv_monetary

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

young = 0
adults = 0
seniors = 0
for data in data_frame:
    if data['idade'] >= 18 and data['idade'] <= 25:  # jovens
        young += 1
    elif data['idade'] >= 26 and data['idade'] <= 59:  # adultos
        adults += 1
    elif data['idade'] >= 60:  # Idosos
        seniors += 1
# ---- END FOR ----

total_people = (young + adults + seniors)

percent_young = (young * 100) / total_people
percent_adults = (adults * 100) / total_people
percent_seniors = (seniors * 100) / total_people

msg_young = f'Existem um total de {young} de {total_people}, pessoas jovens, que representa {percent_young}%.'
msg_adults = f'Existem um total de {adults} de {total_people}, pessoas adultas, que representa {percent_adults}%.'
msg_seniors = f'Existem um total de {seniors} de {total_people}, pessoas idosas, que representa {percent_seniors}%.'
print(f"\n{'=':=^70}\n")
print(msg_young)
print(msg_adults)
print(msg_seniors)
print(f"\n{'=':=^70}\n")

# resposta do print abaixo:
# ======================================================================
# Existem um total de 728 de 5000, pessoas jovens, que representa 14.56%.
# Existem um total de 3280 de 5000, pessoas adultas, que representa 65.6%.
# Existem um total de 992 de 5000, pessoas idosas, que representa 19.84%.
# ======================================================================