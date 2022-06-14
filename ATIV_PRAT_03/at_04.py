# 4) O programa de fidelidade de uma determinada livraria premia seus clientes
# de acordo com o número de livros comprados a cada mês. Os pontos são
# atribuídos da seguinte forma:
# a) Se um cliente comprar 0 livros, ele ganhará 0 pontos.
# b) Se um cliente comprar um livro, ele ganhará 5 pontos.
# c) Se um cliente comprar dois livros, ele ganhará 15 pontos.
# d) Se um cliente comprar 3 livros, ele ganhará 30 pontos.
# e) Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.

# Crie um algoritmo que leia o número de livros comprados por um cliente e
# exiba o número de pontos correspondentes.

# Entrada de dados
quant_livro_comprado = int(input('Quantos livros você comprou este mês: \n'))

pontos = 0 # Variavel de inicialização

# Processamento
if quant_livro_comprado <= 0:
    pontos = 0

elif quant_livro_comprado == 1:
    pontos = 5

elif quant_livro_comprado == 2:
    pontos = 15

elif quant_livro_comprado == 3:
    pontos = 30

elif quant_livro_comprado >= 4:
    pontos = 60

print(f'Você comprou {quant_livro_comprado} livros este mês, seu total de pontos é: [{pontos}] pontos')

# pronto