# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos
# Enunciado:

# 11) Qual opção de pagamento é mais utilizada em cada faixa etária?
from functions import conv_data_files

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

young = {'age_category': 'Jovens', 'form_payment': {
    'credito': 0, 'debito': 0, 'dinheiro': 0}}
adults = {'age_category': 'Adultos', 'form_payment': {
    'credito': 0, 'debito': 0, 'dinheiro': 0}}
seniors = {'age_category': 'Idosos', 'form_payment': {
    'credito': 0, 'debito': 0, 'dinheiro': 0}}


def calc_option_payment_must_used_age_group(age_group, payment):
    age_group['form_payment'][payment] += 1


for i, data in enumerate(data_frame):
    if data['idade'] >= 18 and data['idade'] <= 25:
        calc_option_payment_must_used_age_group(young, data['pagamento'])
    if data['idade'] >= 26 and data['idade'] <= 59:
        calc_option_payment_must_used_age_group(adults, data['pagamento'])
    if data['idade'] >= 60:
        calc_option_payment_must_used_age_group(seniors, data['pagamento'])


# for de print das respostas
print(f"{'=':=^70}")
for j in young, adults, seniors:
    category = j['age_category']
    form_payment = j['form_payment']
    
    if form_payment['credito'] > form_payment['debito'] and form_payment['credito'] > form_payment['dinheiro']:
        print(f'Os {category} utilizam mais CREDITO com um total de {form_payment["credito"]} vezes.')

    if form_payment['debito'] > form_payment['credito'] and form_payment['debito'] > form_payment['dinheiro']:
        print(f'Os {category} utilizam mais DEBITO com um total de {form_payment["debito"]} vezes.')
    
    if form_payment['dinheiro'] > form_payment['credito'] and form_payment['dinheiro'] > form_payment['debito']:
        print(f'Os {category} utilizam mais DINHEIRO com um total de {form_payment["dinheiro"]} vezes.')
print(f"{'=':=^70}\n")

# resposta do print abaixo:
# ======================================================================
# Os Jovens utilizam mais DINHEIRO com um total de 254 vezes.
# Os Adultos utilizam mais DEBITO com um total de 1101 vezes.
# Os Idosos utilizam mais DEBITO com um total de 341 vezes.
# ======================================================================
