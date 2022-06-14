# 6) Escreva um algoritmo que receba a idade do usuário e exiba a mensagem
# “Maior de idade” caso a idade seja maior ou igual de 18 anos e a mensagem
# “Menor de idade” caso a idade seja menor de 18 anos.

# entrada de dados
idade = int(input('Digite qual a sua idade: \n'))

# Processamento e saida de dados
if idade >= 18:
    print(f' ---> Maior de idade, ja pode fazer a CNH!') 
else:
    print(f' ---> Menor de idade, não pode dirigir!') 

# pronto