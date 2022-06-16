# Enunciado:
# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos
# 7) Qual é a faixa etária que mais gasta?
from functions import conv_data_files, conv_monetary

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

young = [0,'Jovens']
adults = [0,'Adultos']
seniors = [0,'Idosos']
for data in data_frame:
    if data['idade'] >= 18 and data['idade'] <= 25:  # jovens
        young[0] += data['compra']
    elif data['idade'] >= 26 and data['idade'] <= 59:  # adultos
        adults[0] += data['compra']
    elif data['idade'] >= 60:  # Idosos
        seniors[0] += data['compra']
# ---- END FOR ----
all_age_group = [young, adults, seniors]

less_spent = min(all_age_group) # menos gasto
more_spent = max(all_age_group) # maior gasto

msg_less_spent = f'O grupo de idade com MENOR gasto foi os {less_spent[1]}, com um valor total de {conv_monetary.init_app(less_spent[0])}'
msg_more_spent = f'O grupo de idade com MAIOR gasto foi os {more_spent[1]}, com um valor total de {conv_monetary.init_app(more_spent[0])}'

print(f"\n{'=':=^80}")
print(msg_less_spent)
print(msg_more_spent)
print(f"{'=':=^80}\n")

# resposta do print abaixo:
# ================================================================================
# O grupo de idade com MENOR gasto foi os Jovens, com um valor total de 3.717.756,00
# O grupo de idade com MAIOR gasto foi os Adultos, com um valor total de 17.132.497,00
# ================================================================================