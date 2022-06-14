# Etrada de dados
sms_mes = int(input('Qual o total de sms enviados no mês: \n'))

# Variaveis de inicialização e pesos
valor_fatura = 5 # 60 sms pacote de basico
valor_fatura_imposto = 0
X_sms = 61

# Processamento de dados
while X_sms <= sms_mes:
    if X_sms > 60 and X_sms <= 180: # quando passar de 60 sms
        valor_fatura += 0.05
    elif X_sms > 180:# quando passar de 180 sms
        valor_fatura += 0.10
    X_sms+=1 # 

# Calculo de impostos
valor_imposto = valor_fatura * 0.12
valor_fatura_imposto = valor_fatura + valor_imposto

# Saida de dados
print(f' --- FECHAMENTO DE FATURA DO MÊS --- ')
print(f' --- Fatura do mês(sem imposto): R$ {valor_fatura:.2f}')
print(f' --- Fatura do mês(com imposto): R$ {valor_fatura_imposto:.2f}')
print(f' --- Total de imposto: R$ {valor_imposto:.2f}')
print(f' --- SMS enviados no mês:{sms_mes}')
print(f' --- FECHAMENTO DE FATURA DO MÊS --- ')