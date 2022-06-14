# 3) Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular, utilizando a fórmula.

### FORMULA DO CALCULO ###
# VOLUME = COMPRIMENTO * LARGURA * ALTURA

VOLUME = 0  # valor de inicialização e pesos

print('--- VAMOS CALCULAR O VOLUME DE UMA CAIXA RETANGULAR ---')

# Entrada de dados pelo usuario
COMPRIMENTO = float(input('Digite um valor de COMPRIMENTO: \n'))
LARGURA = float(input('Digite um valor para LARGURA: \n'))
ALTURA = float(input('Digite um valor para ALTURA: \n'))

# Processamento dos dados
VOLUME = COMPRIMENTO * LARGURA * ALTURA

# Saida de dados
print(f'O volume da caixa retangular é: {VOLUME}')
