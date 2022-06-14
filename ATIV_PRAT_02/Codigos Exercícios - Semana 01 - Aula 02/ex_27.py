# formato 1
print("Informe a temperatura em graus Celsius: ")
celsius = int(input())

fahrenheit = 9 / 5 * celsius + 32

print("Temperatura em Fahrenheit: {}".format(fahrenheit))

# formato 2
print("Informe a temperatura em graus Fahrenheit: ")
celsius = int(input())

celsius = (fahrenheit - 32) * 5 / 9

print("Temperatura em Celsius: {}".format(celsius))

