# 8) Escreva uma função que conte o número de espaços em branco em uma
# frase passada como parâmetro.

def blank_space_in_text(text):
    count = 0
    for t in text:
        if t == ' ':
            count += 1
    return count

print('\n')
text = input('Digite um pequeno texto: \n')
number_of_spaces = blank_space_in_text(text)
print('\n')
print(f'O numero de espaço em branco no seu texto é: {number_of_spaces}')