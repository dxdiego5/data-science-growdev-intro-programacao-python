# Enunciado:
# 4) Exiba o valor total de compras por modo de pagamento.
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from functions import conv_data_files

# chamada da funcao de leitura de arquivo
data_frame = conv_data_files.init_app()

form_payment = {'debito': 0, 'credito': 0, 'dinheiro': 0}
for data in data_frame:

    if data['pagamento'] == 'debito':
        form_payment['debito'] += 1

    if data['pagamento'] == 'credito':
        form_payment['credito'] += 1

    if data['pagamento'] == 'dinheiro':
        form_payment['dinheiro'] += 1


app = Dash(__name__)

df = pd.DataFrame({
    'payment': [item for item in form_payment.keys()],
    'values': [item for item in form_payment.values()]
})

fig = px.pie(df, names='payment', values='values', color='payment')
fig.update_traces(textposition='inside', textinfo='percent+value+label')
app.layout = html.Div(children=[
    html.H3(children='''
        Exiba o valor total de compras por modo de pagamento.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
