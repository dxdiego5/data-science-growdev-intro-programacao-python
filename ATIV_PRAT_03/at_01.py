# 1) Considere as variáveis abaixo, inicializadas como segue:
numero1 = 300
numero2 = 100
numero3 = 5
string1 = "Rinoceronte"
string2 = "Zebra"
string3 = "bug"

# Para cada uma das seguintes expressões booleanas, classifique-a como
# Verdadeira, Falsa ou Ilegal.
print(numero1 == numero3) # ---> False
print(numero1 > numero3) # ---> True
print(numero2 < numero3) # ---> False
print(numero1 == string1) # ---> False
print(numero1 == "Um") # ---> False
print(numero1 == "Trezentos") # ---> False
print(numero1 == "300") # ---> False
print(string2 == "Dois") # ---> False
print(string1 == "Rinoceronte") # ---> True
print(string3 != "inoceronte") # ---> True
print(string3 != "Rinoceronte" or numero1 > 1000) # ---> True
print(numero2 <= numero1 / 3) # ---> True
print(numero1 >= 200) # ---> True
print(numero1 >= numero2 + numero3) # ---> True
print(numero1 > numero2 and numero1 < numero3) # ---> False
print(numero1 < 10 or numero3 > 10) # ---> False
print(numero1 == 30 and numero2 == 100 or numero3 == 100) # ---> False

# pronto