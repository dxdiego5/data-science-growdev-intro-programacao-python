# Enunciado:
# 3) Mostre a quantidade de homens e mulheres na base de dados.
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from functions import conv_data_files

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

men = 0
women = 0
for data in data_frame:
    if data['sexo'].upper() == 'M':# se for homen
        men += 1
    else:  # se for mulher
        women += 1
# ---- END FOR ----

app = Dash(__name__)

df = pd.DataFrame({
    'gender':['homens','mulheres'],
    'values':[men,women]
})
fig = px.pie(df, names='gender', values='values',color='gender')
fig.update_traces(textposition='inside', textinfo='percent+value+label')
app.layout = html.Div(children=[
    html.H3(children='''
       Quantidade de homens e mulheres na base de dados.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# grafico_03:

