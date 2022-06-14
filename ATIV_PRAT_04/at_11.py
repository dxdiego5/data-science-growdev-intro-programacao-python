# 11) Crie um algoritmo para um jogo de adivinhação, onde o usuário tenta
# adivinhar um número aleatório gerado pelo computador. Esse número
# aleatório é inteiro e não negativo, e deve ser escolhido dentro de uma faixa
# estabelecida pelo usuário (por exemplo, o usuário pode estipular que esse
# número varie entre 0 e 10 ou entre 22 e 48, por exemplo). Após o usuário
# tentar adivinhar qual foi o número gerado, o algoritmo deve escrever esse
# número e dizer se indicar se o palpite do jogador estava correto, muito alto ou
# muito baixo.
# Dica: Para gerar um número aleatório utilize a função randint do módulo
# random.
import random # import random para gerar numeros aleatorios 

# Entrada de dados
num_inicio, num_fim = int(input('Digite um numero de inicio: \n')),int(input('Digite um numero de fim: \n'))
num_escolhido = int(input('Digite um numero para adivinhar o sorteio: \n'))

# Processamento
numero_gerado = random.randint(num_inicio, num_fim)



if num_escolhido == numero_gerado:
    print(f'---> O palpite do jogador esta correto! Nº {num_escolhido}, Nº sorteado {numero_gerado}, [ entre {num_inicio} ate {num_fim}]')
elif num_escolhido < numero_gerado:
    print(f'---> Não acertou!, foi baixo!, Nº sorteado {numero_gerado}')
elif num_escolhido > numero_gerado:
    print(f'---> Não acertou!, foi alto!, Nº sorteado {numero_gerado}')
else:
    print('Error: algo deu errado jogue novamente...')