from dash import Dash, dcc, html, Output, Input, State
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
# from teammate_code_chunks.ws_table import wstable
import teammate_code_chunks.ws_table
from prepare_data import prepare_deals, filter_deals, prepare_clients, filter_clients, prepare_employees, filter_employees
import pickle
import numpy as np
# from jo_input2 import jo_input2layout

### import pickled models
# pickled_model = pickle.load(open('clustering.pickle', 'rb'))
# encoded_employees = pd.read_excel("encoded_employees.xlsx")

# build your app
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# build your components
# header = dbc.Row(
#     dbc.Col(html.H1("Client Reccomendation Program"))
# )
mytext = dcc.Markdown(children="")
myinput = dbc.Input(id="myinput", type="text", placeholder="Enter text")


## import data
# clients = pd.read_csv("1116_clients.csv")
# print(clients)

## import deals
deals = pd.read_csv("1116_deals.csv")
deals = prepare_deals(deals)
# print(deals)
## data table
raitable = dash_table.DataTable(
    data = deals.to_dict('records'),
    editable=True,
    # filter_action="native",
    sort_action='native',
    sort_mode="multi"
)

raitable_layout = html.Div(
    children = [
        raitable
    ]
)
## basic input
mytext = dcc.Markdown(children="")
myinput = dbc.Input(id="myinput", type="text", placeholder="Enter text")
# myinput text callback
# @app.callback(
#     Output(mytext, component_property="children"),
#     Input(myinput, component_property="value"),
# )
# def update_title(input_value):
#     return input_value
## basic input

### JOLENE INPUT 2
input_style = {'font-size': '15px', 'padding': '10px', 'border-radius': '10px', 'border': '2px solid #ccc', 'background-color': '#fff','color': '#003b71'
}

button_style = {
    'width': '100px',
    'height': '35px',
    'background-color': '#003b71',
    'color': 'white',
    'border': 'none',
    'border-radius': '3px',
    'font-size': '16px',
    'cursor': 'pointer'
}

div_style ={
        'display': 'flex', 'flex-direction': 'column', 'align-items': 'center',
        'background-color': '#003b71', 'color': 'white', 'height': '115px',
        'font-family': 'Arial, sans-serif'
}
jo_input2layout = html.Div(
    className='google-form',
    style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', },
    # style=app_style,
    children=[
        html.Br(),
        html.Img(src='https://pentagram-production.imgix.net/wp/592ca89f19a1d/ps-citibank-01.jpg?crop=edges&fit=crop&h=630&rect=0%2C177%2C960%2C600&w=1200', className='logo', style={'width': '15%'}),
        html.Br(),
        html.Div(
            className='input-container',
            children=[
                # coy dept
                dcc.Input(id='region-input', type='text', placeholder='Region', className='input-field', style=input_style),
                html.Br(),
                html.Br(),
                # industry
                dcc.Input(id='industry-input', type='text', placeholder='Industry', className='input-field', style=input_style),
                html.Br(),
                html.Br(),
                # region
                dcc.Input(id='deal-type-input', type='text', placeholder='Deal Type', className='input-field', style=input_style),
                html.Br(),
                html.Br(),

            ]
        ),
        html.Br(),
        html.Button('Submit', className='submit-button', id='submit-button', style=button_style),
        html.Div(id='output-container')
    ]
)

def create_filtered_data_table(filtered_df):
    table = dash_table.DataTable(
        data = filtered_df.to_dict('records'),
        editable=True,
        # filter_action="native",
        sort_action='native',
        sort_mode="multi"
    )
    return table

def gen_data_df(dept, industry, region, clientcap, expyears):
    collist = [dept, industry, region, clientcap, expyears]
    # row = pd.DataFrame([dept, industry, region, clientcap, expyears]).T
    # row.rename(columns={
    #     0:"Company Department",
    #     1:"Industry",
    #     2:"Region",
    #     3:"clientcap",
    #     4:"expyears",
    # }, inplace=True)
    # return row
    numpyarr = np.array(collist).reshape(-1, 1)
    row = pd.DataFrame(numpyarr).T
    print(row)
    return row


from sklearn import preprocessing
def encode_row(transformed_test):
    to_encode = ["Company Department","Industry", "Region","Designation"]
    # transformed_test = transformed_test.fillna('na')
    for column in transformed_test.columns:
        if column in to_encode:
            le = preprocessing.LabelEncoder()
            le.fit(transformed_test[column].astype(str))
            transformed_test[column]=le.transform(transformed_test[column])
            keys = le.classes_
            values = le.transform(le.classes_)
            dictionary = dict(zip(keys, values))
            print(dictionary)

clients = pd.read_csv('1116_clients.csv')
clients = prepare_clients(clients)

employees = pd.read_csv('1116_employees.csv')
employees = prepare_employees(employees)

@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    State('region-input', 'value'),
    State('industry-input', 'value'),
    State('deal-type-input', 'value'),
)
def save_form_inputs(n_clicks, product, country, deal_type):
    if n_clicks is not None:
        # res = filter_deals(deals, product, country, deal_type)
        # res = filter_clients(clients, product, country, deal_type)
        res = filter_employees(employees, product, country, deal_type)
        res_table = create_filtered_data_table(res)
        if len(res) == 0:
            return html.Div([
                html.Br(),
                html.Br(),
                html.H4("No employees found!")
            ])
        else:
            return html.Div([
                html.Br(),
                res_table
            ])

app.layout = dbc.Container(
    [
        jo_input2layout,
        # header,
        # myinput,
        # mytext,
        html.Br(),
        # raitable_layout,
        # wstable,
    ],
)



# run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)