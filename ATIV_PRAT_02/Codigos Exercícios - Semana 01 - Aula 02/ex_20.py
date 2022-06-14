print("Informe a quantidade de ações compradas: ")
acao_compra_quantidade = int(input())

print("Informe o valor da ação comprada: ")
acao_compra_valor = float(input())

print("Informe a taxa cobrada pela compra: ")
acao_compra_taxa = float(input())

print("Informe a quantidade de ações vendidas: ")
acao_venda_quantidade = int(input())

print("Informe o valor da ação vendida: ")
acao_venda_valor = float(input())

print("Informe a taxa cobrada pela venda: ")
acao_venda_taxa = float(input())

valor_total_compra = acao_compra_quantidade * acao_compra_valor

taxa_compra = valor_total_compra * acao_compra_taxa / 100

valor_total_compra += taxa_compra

ganho_venda = acao_venda_quantidade * acao_venda_valor

taxa_venda = ganho_venda * acao_venda_taxa / 100

ganho_venda -= taxa_venda

diferenca = ganho_venda - valor_total_compra