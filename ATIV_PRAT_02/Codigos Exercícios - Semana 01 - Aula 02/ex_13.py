print("Informe o primeiro valor: ")
n1 = int(input())

print("Informe o segundo valor: ")
n2 = int(input())

aux = n1
n1 = n2
n2 = aux

print("Novos valores\nn1: {}\nn2: {}".format(n1, n2))