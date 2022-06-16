# Enunciado:

# 8) A opção de débito é mais utilizada entre homens ou mulheres?
from functions import conv_data_files, conv_monetary

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

payment_men = 0
payment_women = 0
total = 0
for data in data_frame:
    if data['sexo'].upper() == 'M':  # se for homen
        if data['pagamento'].lower() == 'debito':
            total += 1
            payment_men += 1

    else:  # se for mulher
        if data['pagamento'].lower() == 'debito':
            total += 1
            payment_women += 1
# -------- END FOR --------

percent_men = (payment_men * 100) / total
percent_women = (payment_women * 100) / total

if payment_men > payment_women:
    passed_debit = f'Os HOMENS utilizarão mais a função de debíto com um total de {payment_men} de {total}, em porcentagem foi {round(percent_men, 2)}%'
else:
    passed_debit = f'As MULHERES utilizarão mais a função de debíto com um total de {payment_women} de {total}, em porcentagem foi {round(percent_women, 2)}%'

print(f"\n{'=':=^80}")
print(passed_debit)
print(f"{'=':=^80}\n")

# resposta do print abaixo:
# ================================================================================
# Os HOMENS utilizarão mais a função de debíto com um total de 954 de 1685, em porcentagem foi 56.62%
# ================================================================================