# Enunciado:
# 9) Qual o sobrenome que mais aparece na base de dados?
from functions import conv_data_files

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

last_name_counter = []


def counter_last_name(last_name):  # adiciona o nome ja existe somando
    for info in last_name_counter:
        if info[1] == last_name:
            info[0] += 1
            return True
    return None  # return none se nao achar nehum


for data in data_frame:
    d = counter_last_name(data['sobrenome'])
    if d == False or d == None:  # se nao tiver nome existente entao adicionar o novo a lista
        last_name_counter.append([1, data['sobrenome']])

last_name = max(last_name_counter)
print(f"{'=':=^70}")
print(
    f'O sobrenome que mais aparece é: [{last_name[1]}] com um total de {last_name[0]} vezes que apareceu.')
print(f"{'=':=^70}\n")

# resposta do print abaixo:
# ======================================================================
# O sobrenome que mais aparece é: [Alves] com um total de 768 vezes que apareceu.
# ======================================================================
