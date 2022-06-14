# 8) A padaria do Paulo vende pão francês a R$0.75, pão doce a R$0.85 e quindim a R$1.50.
# Crie um algoritmo que pergunte quantas unidades de cada produto foram vendidas pelo Paulo num dia e calcule o total faturado.

# Modificação 1 – Modifique o algoritmo para que, ao invés de considerar o preço dos produtos como fixos, o usuário possa informar o preço deles.

# Modificação 2 – Paulo tem o hábito de guardar 10% de tudo que fatura numa caderneta de poupança, para eventuais necessidades no futuro.
# Sabendo disso, modifique o algoritmo que você criou para que ele informe quanto do total faturado deve ser poupado.

# Modificação 3 – Modifique o algoritmo para que, antes de calcular quanto deve ser guardado na poupança, ele desconte o valor do imposto devido, que é de 5%.

################################################################
import os

os.system('clear')  # no windows cls

# dados de inicialização e pesos
produtos = [{'produto': 'Pão Francês', 'preco': 0.75}, {
    'produto': 'Pão Doce', 'preco': 0.85}, {'produto': 'Quindim', 'preco': 1.50}]

print('----- TABELA DE PREÇOS ABAIXO -----')
print('-----------------------------------')

for i in produtos:

    informacao = input(
        f'----- "{i["produto"]}", preço R$ {i["preco"]} reais, (Digite um valor para alterar, SE NÂO aperte ENTER para continuar ...):\n')
    try:
        os.system('clear')  # no windows cls
        # Alterando o valor do produto em específico
        i["preco"] = float(informacao)
        print(
            f'----- ALTERAÇÃO NO ITEM: "{i["produto"]}" NOVO preço R$ {i["preco"]} reais')
    except ValueError:
        # Se não foi digitado nuhum valor mostrar alerta de preço não alterado
        os.system('clear')  # no windows cls
        print(
            f'----- SEM ALTERAÇÕES NO ITEM: "{i["produto"]}" e preço R$ {i["preco"]} reais')
    print('\n')

print('--- TABELA DE PREÇOS ATUALIZADA COM SUCESSO ---')
print('\n')

# Montando carrinho de vendas
# Variaveis de inicialização e pesos
carrinho_compra = []
total_items = 0
indice = 0

for i in produtos:
    quantidade = input(f'Quantos "{i["produto"]}", você quer comprar? \n')

    # Tratando erro simples se digitar tecla errada quantidade valor 0
    try:
        quantidade = int(quantidade)
    except ValueError:
        quantidade = 0

    carrinho_compra.append(i)
    carrinho_compra[indice]['quantidade'] = quantidade
    carrinho_compra[indice]['sub_total_items'] = quantidade * i["preco"]
    total_items += (quantidade * i["preco"])
    indice += 1

# Calculando os 5% de imposto a cobrar quando seu paulo for depositar
imposto = (total_items * 0.05)

# Montagem de tela da vendas e informações
os.system('clear')  # no windows cls
print('\n')
print('----- CARRINHO DE COMPRAS DA PADARIA DO SEU PAULO ')
print('----- TELA DE VENDA (CAIXA) ---------------------------------------------------------------')
for i in carrinho_compra:
    print(f'----- {i["quantidade"]} X | "{i["produto"]}" - preço unitário R$ {i["preco"]:.2f} - sub_total R$ {i["sub_total_items"]:.2f}')
    # final do for

print('')
print(f'----- ### ----- Total faturado R$ {total_items:.2f} reais')
print('')
print(
    f'----- Seu Paulo deve guardar 10%, o valor para poupar é R$ {((total_items - imposto) * 0.1):.2f} '
    f'reais com o desconto de 5% inclúso de R$ {imposto:.2f} reais')
print('-------------------------------------------------------------------------------------------')
print('----------------------------------------FIM------------------------------------------------')