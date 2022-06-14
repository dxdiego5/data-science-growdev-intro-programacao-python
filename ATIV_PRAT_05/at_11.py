# 11) Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja
# 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
# programa que calcule e escreva o número de anos necessários para que a
# população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

#  A seja da ordem de 80000 habitantes taxa anual de crescimento de 3%
#  B seja 200000 habitantes taxa de crescimento de 1.5%.

is_maior = False

populaca_a = 80000
populaca_b = 200000
e_maior = False
contador_ano = 0

while e_maior == False:
    populaca_a += (populaca_a * 0.03)
    populaca_b += (populaca_b * (1.5 /100))
    if (populaca_a > populaca_b):
        e_maior = True
    
    contador_ano += 1

print(f' A populacao A precisou de {contador_ano} anos')