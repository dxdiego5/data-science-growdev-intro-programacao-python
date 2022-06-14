produto_valor = 5.4

print("Informe a quantidade comprada: ")
produto_quantidade = int(input())

total_sem_desconto = produto_quantidade * produto_valor

centenas_compradas = produto_quantidade / 100
centenas_compradas -= centenas_compradas % 1

valor_centena = produto_valor * 100

desconto_centena = valor_centena * 0.5 / 100

desconto_total = centenas_compradas * desconto_centena

total_com_desconto = total_sem_desconto - desconto_total

print("Total sem desconto: {}".format(total_sem_desconto))

print("Centenas compradas: {}".format(centenas_compradas))

print("Desconto: {}".format(desconto_total))

print("Total com desconto: {}".format(total_com_desconto))
