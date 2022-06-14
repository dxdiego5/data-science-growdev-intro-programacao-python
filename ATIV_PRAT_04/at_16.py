# 16) Construa um algoritmo que, a partir do valor do comprimento dos três lados
# de um triângulo, classifique-o em equilátero, isósceles ou escaleno. Lembre,
# um triângulo é equilátero quando o comprimento de todos os seus lados for
# igual, 
# é isósceles quando apenas um dos lados tiver comprimento diferente e
# é escaleno quando todos os lados tiverem comprimentos diferentes dos
# demais lados.

(x1, x2, x3) = float(input('Digite o comprimento do 1 lado do triangulo: \n')),float(input('Digite o comprimento do 2 lado do triangulo: \n')),float(input('Digite o comprimento do 3 lado do triangulo: \n'))

if x1 == x2 and x1 == x3:
    print('O triangulo é: Equilátero, quando o comprimento de todos os seus lados for igual')

elif x1 == x2 or x1 == x3 or x2 == x3:
    print('O triangulo é: Isósceles, quando apenas um dos lados tiver comprimento diferente')
    
elif x1 != x2 and x1 != x3 and x2 != x3:
    print('O triangulo é: Escaleno, quando todos os lados tiverem comprimentos diferentes dos demais lados.')