# 18)Um saco de biscoitos contém 40 unidades que, de acordo com as informações
# do rótulo, equivalem a 10 porções. Ainda de acordo com o rótulo, uma porção
# possui 300 calorias. Baseado nessas informações, crie um algoritmo que permita
# ao usuário inserir o número de biscoitos que ele consumiu e imprima na tela a quantidade de calorias correspondentes.

# 1 saco de biscoito tem 40 uni equivale a 10 porções
# 1 porção possui 300 calorias

# Entrada de dados
biscoitos = int(input('Quantos biscoitos você comeu ? \n'))

# Processando
porcao_por_biscoito = 10 / 40 # 0.25 -> Cada unidade (biscoito tem em porção)
caloria_por_porcao = 0.25 * 300 # 75 -> Cada porção por unidade de biscoito tem em calorias

# Total porção consumida
porcao_consumida = porcao_por_biscoito * biscoitos

# Total calorias consumida 
calorias_total = caloria_por_porcao * biscoitos

# Saida de dados
print('')
print('>>>>>>>>>>>> TABELA DE CONSUMO <<<<<<<<<<<<')
print(f'--- BISCOITOS CONSUMIDOS: {biscoitos} Unidades')
print(f'--- PORÇÃO CONSUMIDA: (%) {porcao_consumida}')
print(f'--- CALORIAS TOTAL: (cal) {calorias_total}')
print('')
print(f'------- PORÇÃO POR BISCOITO: -- (%) {porcao_por_biscoito}')
print(f'--- CALORIAS POR BISCOITO: -- (cal) {caloria_por_porcao}')
print('>>>>>>>>>>>> TABELA DE CONSUMO <<<<<<<<<<<<')