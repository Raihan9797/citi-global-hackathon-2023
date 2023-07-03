import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State



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

# Define the form layout
jo_input2layout = html.Div(
    className='google-form',
    style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'border':'solid blue'},
    # style=div_style,
    children=[
        html.Br(),
        html.Img(src='https://pentagram-production.imgix.net/wp/592ca89f19a1d/ps-citibank-01.jpg?crop=edges&fit=crop&h=630&rect=0%2C177%2C960%2C600&w=1200', className='logo', style={'width': '15%'}),
        html.Br(),
        html.Div(
            className='input-container',
            children=[
                dcc.Input(type='text', placeholder='Product', className='input-field', style=input_style),
                html.Br(),
                html.Br(),
                dcc.Input(type='text', placeholder='Country', className='input-field', style=input_style),
                html.Br(),
                html.Br(),
                dcc.Input(type='text', placeholder='Deal Type', className='input-field', style=input_style)
            ]
        ),
        html.Br(),
        html.Button('Submit', className='submit-button', style=button_style)
    ],
)

@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    State('product-input', 'value'),
    State('country-input', 'value'),
    State('deal-type-input', 'value')
)
def save_form_inputs(n_clicks, product, country, deal_type):
    if n_clicks is not None:
        return html.Div([
            html.P(f'Product: {product}'),
            html.P(f'Country: {country}'),
            html.P(f'Deal Type: {deal_type}')
        ])