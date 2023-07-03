
### input code
# Define some basic styles for the form elements
input_style = {
    'width': '50%',
    'padding': '12px 20px',
    'margin': '8px 0',
    'box-sizing': 'border-box',
    'border': '2px solid #ccc',
    'border-radius': '4px',
    'font-size': '16px',
}

label_style = {
    'font-size': '16px',
    'font-weight': 'bold',
    'margin-bottom': '6px',
}

button_style = {
    'background-color': '#4CAF50',
    'border': 'none',
    'color': 'white',
    'padding': '12px 20px',
    'text-align': 'center',
    'text-decoration': 'none',
    'display': 'inline-block',
    'font-size': '16px',
    'border-radius': '4px',
    'cursor': 'pointer',
    'margin-top': '10px',
}

my_input = html.Div(children=[
    html.H1(children='Form Example', style={'text-align': 'center'}),
    html.Div(children='''
        Enter your information below:
    ''', style={'text-align': 'center'}),
    html.Label('Name', style=label_style),
    dcc.Input(type='text', placeholder='Enter your name', style=input_style),
    html.Br(),
    html.Label('Email', style=label_style),
    dcc.Input(type='email', placeholder='Enter your email', style=input_style),
    html.Br(),
    html.Label('Ageyo', style=label_style),
    dcc.Input(type='number', placeholder='Enter your age', style=input_style),
    html.Br(),
    html.Button('Submit', type='submit', style=button_style)
], style={'width': '50%', 'margin': 'auto'})


@app.callback(
    Output('output', 'children'),
    Input('submit-button', 'n_clicks'),
    State('name-input', 'value'),
    State('email-input', 'value'),
    State('age-input', 'value')
)

def predict(n_clicks, name, email, age):
    if n_clicks:
        # Perform whatever preprocessing is necessary on the form data
        # and pass it to your machine learning model for prediction
        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Age: {age}')
        return 'Form data submitted successfully!'