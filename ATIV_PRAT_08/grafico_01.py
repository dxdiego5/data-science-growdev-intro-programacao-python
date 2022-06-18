# Enunciado:
# 1) Exiba um gráfico que mostre a quantidade total de gastos com
# compras agrupadas por anos.
# agrupadas por anos.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from functions import conv_data_files

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

total_sales_for_year = []
years = []

for data in data_frame:
    if data['ano'] in years:
        for info in total_sales_for_year:
            if info[0] == data['ano']:
                info[1] += data['compra']
    else:
        years.append(data['ano'])
        total_sales_for_year.append([data['ano'], data['compra']])

total_sales_for_year.sort()

app = Dash(__name__)

df = pd.DataFrame({
    'years': [y[0] for y in total_sales_for_year],
    'spending': [s[1] for s in total_sales_for_year]
})

fig = px.bar(df, x='years', y='spending', color='spending', text_auto=True)

app.layout = html.Div(children=[
    html.H3(children='''
      Exiba um gráfico que mostre a quantidade total de gastos por anos.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
