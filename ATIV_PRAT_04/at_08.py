# 8) Um carpinteiro esculpe placas personalizadas para estabelecimentos
# comerciais e deseja um programa que faça orçamentos das placas que
# produz, considerando as seguintes informações:
# a) O valor mínimo de qualquer placa é de R$ 300,00;
# b) Placas de angelim custam R$ 150,00 adicionais, mas placas de pinus
# não possuem nenhum custo extra;
# c) Frases com até 12 caracteres estão incluídas no valor mínimo; para
# frases maiores, são cobrados R$ 15,00 por caractere;

# d) Para placas com dizeres brancos ou pretos não se cobra adicional,
# mas se ele contiver letras douradas, cobra-se R$ 60,00 a mais.
# Baseado nessas informações, 
# construa um algoritmo que leia o número de um orçamento, 
# o nome do cliente, tipo de madeira (angelim ou pinus),
# número de caracteres da mensagem e a cor dos caracteres (branco, preto ou
# dourado). Ao final, imprima todos os dados de entrada e o preço da placa
# orçada.

import os

# valores de inicialização e peses
valor_min=300
placa_pinus=0
placa_angelim=150
preco_caracter=15
letra_dourada=60

# Valores e peses de inicialização
valor_orcamento = valor_min 

# Entrada de dados
num_orcamento = int(input('Nº de orçamento: \n'))
nome_cliente = input('Nome do cliente: \n')
tipo_madeira = input('Digite a letra [A] para angelim ou Digite a letra [P] para pinus: \n')
cor_referencia = input('Digite a letra [B] para bracno, Digite a letra [P] para preto ou Digite a letra [D] para dourado: \n')
letras = int(input('Quatas letras vai ter a menssagem: \n'))

os.system('clear')

# Processamento
if tipo_madeira.upper() == "A": # Angelim
    valor_orcamento += placa_angelim    

if letras > 12: 
    valor_orcamento += (letras - 12) * preco_caracter

if cor_referencia.upper() == "D": 
    valor_orcamento += 60


# Saida de dados
print('--- DADOS ---')
print(f'Nº Orçamento: {num_orcamento}')
print(f'Cliente: {nome_cliente}')

# tipo madeira selecionada
if tipo_madeira.upper() == "A": 
    print('Tipo de madeira: ANGELIM')
else:
    print('Tipo de madeira: PINUS')

# tipo cor de letra selecionada
if cor_referencia.upper() == "B": 
    print('COR LETRAS: BRANCO')
elif cor_referencia.upper() == "P": 
    print('COR LETRAS: PRETO')
elif cor_referencia.upper() == "D": 
    print('COR LETRAS: DOURADA')

print(f'total de letras: {letras}')

print('')
print('--- ORÇAMENTO ---')
print(f'O valor total orçamento é: R${round(valor_orcamento, 2)}')
print('---------')