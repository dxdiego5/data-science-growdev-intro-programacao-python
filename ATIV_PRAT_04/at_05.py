# 5) Faça um algoritmo para ler a quantidade adquirida e o preço unitário de um
# produto.
# a) Calcular e escrever o total
    # total = quantidade adquirida * preço unitário
# b) Leia o desconto sobre a compra e calcule.
    # total a pagar = total - desconto
# i) Sabendo-se que:
# (1) Se quantidade <= 5 o desconto será de 2%.
# (2) Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
# (3) Se quantidade > 10 o desconto será de 5%.

quantidade, preco_unit = int(input('Digite a quantidade adquirida: \n')), int(input('Digite o valor unitário: \n'))

total = quantidade * preco_unit

if quantidade <= 5:
    total_pagar = total - (total * 0.02)
    print(f'Total a pagar com quantidade {quantidade}, com 2% de desconto é: {total_pagar}')    
elif quantidade > 5 and quantidade <= 10:
    total_pagar = total - (total * 0.03)
    print(f'Total a pagar com quantidade {quantidade}, com 3% de desconto é: {total_pagar}')
elif quantidade > 10 :
    total_pagar = total - (total * 0.05)
    print(f'Total a pagar com quantidade {quantidade}, com 5% de desconto é: {total_pagar}')
else:
    print('Valor ou algo digitado esta errado!!')

print('')
print(f'O total bruto é R$: {total:.2f}')