# 19) Faça um Programa que leia um número inteiro menor que 1000 e imprima a
# quantidade de centenas, dezenas e unidades do mesmo. Exemplos:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades

# entrada de dados
numero = int(input('Digite um numero de 1 ate 999: \n'))
centenas = 0
dezenas = 0
unidades = 0

# validação, processamento e saida de dados
if numero >= 1 and numero <= 999:
    if numero >=100:
        centenas = numero / 100
        centenas = int(centenas - centenas % 1)
        numero = numero - centenas * 100 # para fazer o calculo restantes
        print(f"Centenas: {centenas}")
        
    if numero >= 10:
        dezenas = numero / 10
        dezenas = int(dezenas - dezenas % 1)
        print(f"Dezenas: {dezenas}")
        
    unidades = int(numero - dezenas * 10)
    print(f"Unidades: {unidades}")
    
else: # erro se numero for invalido
    print('ERROR ....')
    print('Numero digitado invalido')