# 17) Faça um programa que pergunte ao usuário se ele quer passar uma
# temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e
# que, a partir da resposta do usuário, faça a devida conversão.

print('')
tipo_conversao = input("Digite [C] para converter de fahrenheit para Celsius;\nou Digite [F] para converter de celsius fahrenheit: \n")
temperatura = int(input('Digite o valor para temperatura:'))

if tipo_conversao.upper() == "C":
    temp_convertida =( (temperatura - 32) * (5/9))
    print(f'A teperatura em fahrenheit para celsius é: °C {temp_convertida:.2f}')
    
elif tipo_conversao.upper() == "F":
    temp_convertida = (temperatura * (9/5)) + 32
    print(f'A teperatura em celsius para fahrenheit é: °F {temp_convertida:.2f}')