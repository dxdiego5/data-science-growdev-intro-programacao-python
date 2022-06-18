# Enunciado:
# 12)Qual o valor gasto em compras por jovens do ano de 2010 até 2015?
from functions import conv_data_files, conv_monetary

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()


sum_year_spent = 0

for data in data_frame:
    if data['idade'] >= 18 and data['idade'] <= 25:
        if data['ano'] >= 2010 and data['ano'] <= 2015:
            sum_year_spent += data['compra']

print(f"{'=':=^70}")
print(
    f"A som dos gastos do ano de 2010 ate 2015 foi de R$ {conv_monetary.init_app(sum_year_spent)}")
print(f"{'=':=^70}\n")

# resposta do print abaixo:
# ======================================================================
# A som dos gastos do ano de 2010 ate 2015 foi de R$ 1.265.539,00
# ======================================================================
