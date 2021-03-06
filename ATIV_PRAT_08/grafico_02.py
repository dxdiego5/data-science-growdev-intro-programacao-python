# Enunciado:
# 2) Exiba um gráfico que mostre a quantidade total de compras
# agrupadas por anos.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from functions import conv_data_files

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

total_speding_for_year = []
years = []

for data in data_frame:
    if data['ano'] in years:
        for info in total_speding_for_year:
            if info[0] == data['ano']:
                info[1] += 1
    else:
        years.append(data['ano'])
        total_speding_for_year.append([data['ano'], 1])

total_speding_for_year.sort()

app = Dash(__name__)

df = pd.DataFrame({
    'years': [y[0] for y in total_speding_for_year],
    'total': [s[1] for s in total_speding_for_year]
})

fig = px.bar(df, x='years', y='total', color='total', text_auto=True)

app.layout = html.Div(children=[
    html.H3(children='''
      Exiba um gráfico que mostre a quantidade total de compras por anos.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
