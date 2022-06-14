print("Quantos biscoitos você deseja fazer: ")
numero_biscoitos = int(input())

porcao = numero_biscoitos / 48

print("Xicaras de açucar: {}".format(porcao * 1.5))
print("Xicaras de manteiga: {}".format(porcao * 1))
print("Xicaras de farinha: {}".format(porcao * 2.75))