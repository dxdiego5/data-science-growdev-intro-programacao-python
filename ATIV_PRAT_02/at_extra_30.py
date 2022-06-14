# 30) Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
# CENTENA = x
# DEZENA = x
# UNIDADE = x
# Exemplo: 357 tem 3 centenas, 5 dezenas e 7 unidades.

# Entrada de dados
num = input('Digite um numero inteiro de no maximo até 999: \n')

# Validação do processo
if int(num) <= 999:
    # Processamento e saida de dados
    print(
        f'{num} tem {num[0]} centenas, {num[1]} dezenas e {num[2]} unidades.')

# Validação do processo
elif int(num) >= 100:
    print(
        f'Você digitou {num}, é menos do que o algoritimo pode processar volte e digite novamento um valor correto maior ou igual a 100.')

# Validação do processo
else:
    print(
        f'Você digitou {num}, é maior do que o algoritimo pode processar volte e digite novamento um valor correto menor ou igual a 999.')

# centenas = 840 / 100
# resto = centenas % 1
# centenas = centenas - resto
# print(centenas)
# print(resto)