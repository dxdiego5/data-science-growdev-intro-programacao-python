# Enunciado:
# 10)Qual foi o ano em que os homens mais usaram o crédito?
from functions import conv_data_files

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

year_most_used_credit = []


def counter_must_used_credit(data):  # adiciona, ja existe somando
    for info in year_most_used_credit:
        if info[1] == data['ano'] and (data['sexo'].upper() == 'M' and data['pagamento'].lower() == 'credito'):
            info[0] += 1
            return True
    return None  # return none se nao achar nehum


for data in data_frame:
    d = counter_must_used_credit(data)
    if d == False or d == None:  # se nao ano existente entao adicionar o novo a lista
        if data['sexo'].upper() == 'M' and data['pagamento'].lower() == 'credito':
            year_most_used_credit.append([1, data['ano']])


# ano que foi mais usado a funcao de credito por homens
most_used_credit = max(year_most_used_credit)
# ano que foi menos usado a funcao de credito por homens
less_used_credit = min(year_most_used_credit)

print(f"\n{'=':=^70}")
print(f"O ano que os HOMENS MAIS usarao o CREDITO foi em {most_used_credit[1]} com um total de {most_used_credit[0]} vezes.")
print(f"O ano que os HOMENS MENOS usarao o CREDITO foi em {less_used_credit[1]} com um total de {less_used_credit[0]} vezes.")
print(f"{'=':=^70}\n")

# resposta do print abaixo:
# ======================================================================
# O ano que os HOMENS MAIS usarao o CREDITO foi em 2018 com um total de 71 vezes.
# O ano que os HOMENS MENOS usarao o CREDITO foi em 2013 com um total de 47 vezes.
# ======================================================================