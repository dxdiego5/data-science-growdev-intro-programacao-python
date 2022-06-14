# 8) Crie um algoritmo para uma empresa de transportes que, a partir do peso de
# uma encomenda fornecida pelo usuário, calcule o preço da remessa
# conforme a seguinte tabela:

# PESO DA ENCOMENDA  |  VALOR
# ------------------------------------
# 500g ou menos      |  R$ 1,10
# 500g >and< 2 Kg    |  R$ 2,20
# 2Kg >and< 10 Kg    |  R$ 3,70
# 10Kg ou mais       |  R$ 5,00, mais R$3,80/Kg pelo peso

# Entrada de dados
print('---------------------------')
peso_g = float(
    input('OBS: BALANÇA ESTA EM Gramas(g): Digite o peso para calcular o valor de transporte do produto:  \n'))

peso_convertido_kg = peso_g / 1000

# processamento e saida dos dados
if peso_convertido_kg <= 0.5: # 500g ou menos|R$ 1,10
    print(f'O valor do produto pra transporte é: R$ 1,10 reais, do peso de {round(peso_convertido_kg,2)}Kg')

elif peso_convertido_kg > 0.5 and peso_convertido_kg <= 2: # 500g >and< 2000 Kg|R$ 2,20
    print(f'O valor do produto pra transporte é: R$ 2,20 reais, do peso de {round(peso_convertido_kg,2)}Kg')

elif peso_convertido_kg > 2 and peso_convertido_kg < 10: # 2Kg >and< 10 Kg|R$ 3,70
    print(f'O valor do produto pra transporte é: R$ 3,70 reais, do peso de {round(peso_convertido_kg,2)}Kg')

elif peso_convertido_kg >= 10: # 10Kg ou mais R$ 5,00, mais R$3,80/Kg pelo peso
    peso_maior = int(peso_convertido_kg - 10) 
    valor_peso = (peso_maior * 3.80) + 5
    print(f'O valor do produto pra transporte é: R$ {round(valor_peso,2)} reais, do peso de {round(peso_convertido_kg,2)}Kg')

# pronto