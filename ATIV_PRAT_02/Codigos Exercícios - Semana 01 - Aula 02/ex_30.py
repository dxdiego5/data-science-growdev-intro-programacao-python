print("Informe um número")
num = int(input())

centenas = num / 100
centenas = centenas - centenas % 1

num = num - centenas * 100

dezenas = num / 10
dezenas = dezenas - dezenas % 1

unidades = num - dezenas * 10

print("Centenas: {}\nDezenas: {}\nUnidades: {}".format(centenas, dezenas, unidades))