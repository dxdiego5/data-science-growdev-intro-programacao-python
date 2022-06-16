import pathlib # para ler caminhos ate chegar no arquivos desejado
import csv

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve() # pega exatamente a ultima pasta ate no projeto raiz
DATA_PATH = BASE_PATH.joinpath("../data/compras.csv").resolve() # adiciona ao camniho ao arquivo que deseja analisar

def init_app():
    data_frame = []
    with open(DATA_PATH,'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        # csv_reader.__next__() ->> pula a primeira linha a qual pode ser os nomes dos indices das colunas
        
        for row in csv_reader:
            # conversão linha por linha  
            row['idade'] = int(row['idade'])
            row['compra'] = float(row['compra'])
            row['ano'] = int(row['ano'])
            # adiciona a lnha convertida em dict e dados corrigidos para a lista 
            data_frame.append(row)
    
    return data_frame