# 13) Escreva um programa que receba dois valores para as variáveis A e B e 
# efetue a troca dos valores de forma que a variável A passe a possuir o 
# valor da variável B e a variável B passe a possuir o valor da variável A. 
# Apresentar os valores após a efetivação do processamento da troca.

# Entrada de dados
(a, b) = float(input('Digite um valor para A: \n')),float(input('Digite um valor para B: \n'))

print(f'--- VALOR ORIGINAL A {a} X B {b}')

# processamento de dados
(b,a) = (a,b)

# Saida de dados
print(f'--- VALOR ALTERADO A {a} X B {b}')