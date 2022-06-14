# 12) A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.


valor = int(input('Digite um valor: \n'))

posicao_3 = 0
posicao_2 = 1
posicao_1 = 0
fibo = []
for i in range(1, (valor)):
    posicao_3 = posicao_1 + posicao_2
    fibo.append(posicao_3)

    posicao_2 = posicao_1
    posicao_1 = posicao_3

    if valor <= posicao_3:
        break
    
print(fibo)