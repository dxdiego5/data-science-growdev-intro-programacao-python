print("Você deverá informar sua idade expressa em anos, meses e dias")

print("Anos: ")
anos = int(input())

print("Mêses: ")
meses = int(input())

print("Dias: ")
dias = int(input())

total_dias = anos * 365 + meses * 31 + dias

print("Sua idade em dias: {}".format(total_dias))