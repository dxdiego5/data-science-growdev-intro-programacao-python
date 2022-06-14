print("Informe a quantidade de torcedores do time X: ")
torcedores_x = int(input())

print("Informe a quantidade de torcedores do time Y: ")
torcedores_y = int(input())

print("Informe a quantidade de torcedores do time Z: ")
torcedores_z = int(input())

total_torcedores = torcedores_x + torcedores_y + torcedores_z

porcentagem_x = torcedores_x / total_torcedores * 100
porcentagem_y = torcedores_y / total_torcedores * 100
porcentagem_z = torcedores_z / total_torcedores * 100

print("Torcedores X: {:.1f}%".format(porcentagem_x))
print("Torcedores Y: {:.1f}%".format(porcentagem_y))
print("Torcedores Z: {:.1f}%".format(porcentagem_z))