print("Informe a nota 1 do aluno")
nota_1 = float(input())

print("Informe a nota 2 do aluno")
nota_2 = float(input())

print("Informe a nota 3 do aluno")
nota_3 = float(input())

nota_final = nota_1 * 20 / 100 + nota_2 * 30 / 100 + nota_3 * 50 / 100

print("Nota final: {}".format(nota_final))