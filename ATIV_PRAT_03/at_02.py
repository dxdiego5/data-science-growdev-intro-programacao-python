# 2) Faça um algoritmo que receba um valor negativo e retorne o seu valor
# absoluto (ex: recebe -5 e retorna 5).

# entrada de dados
num = float(input('Digite um valor para ser calculado o absoluto: \n'))

num_absoluto = num # variavel auxiliar para não se perder o valor original

# processamento
if num < 0:
    num_absoluto = num * -1 # inver~sao deixando o positivo e absoluto

# Saida de dados
print(f'O absoluto do n: {num} é ABS:({num_absoluto})')

# pronto