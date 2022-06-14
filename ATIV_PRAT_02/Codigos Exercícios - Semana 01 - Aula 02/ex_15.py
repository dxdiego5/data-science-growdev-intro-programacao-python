print("Informe o valor do produto 1: ")
p1 = int(input())

print("Informe o valor do produto 2: ")
p2 = int(input())

print("Informe o valor do produto 3: ")
p3 = int(input())

print("Informe o valor do produto 4: ")
p4 = int(input())

print("Informe o valor do produto 5: ")
p5 = int(input())

subtotal = p1 + p2 + p3 + p4 + p5

imposto = 0.06 * subtotal

total = subtotal + imposto

print("Subtotal: {}\nImposto: {}\nTotal: {}".format(subtotal, imposto, total))