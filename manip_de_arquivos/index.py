import json
import os
import pathlib # para ler arquivos

os.system('clear')

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve() # pega exatamente a ultima pasta ate no projeto raiz
DATA_PATH = BASE_PATH.joinpath("dados.json").resolve() # adiciona ao camniho o arquivo que queira abrir

with open(DATA_PATH,'r') as f:
    dados = json.load(f)


for i in (dados):
    print('-' * 20)
    print(i['reference'])
    print(i['phrase'])