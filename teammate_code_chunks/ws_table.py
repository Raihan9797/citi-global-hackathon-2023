from dash import Dash, dash_table, html
import pandas as pd

data = {
    'Rank': [1, 2, 3, 4, 5],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [100, 90, 85, 80, 75]
}
df = pd.DataFrame(data)

wstable = html.Div(
    className='leaderboard',
    children=[
        html.H1('Game Leaderboard', className='title'),
        dash_table.DataTable(
            id='leaderboard-table',
            data=df.to_dict('records'),
            columns=[
                {'name': 'Rank', 'id': 'Rank'},
                {'name': 'Employee', 'id': 'Employee'},
                {'name': 'Score', 'id': 'Score'}
            ],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'color': 'black',
                'fontWeight': 'bold'
            },
            style_cell={
                'backgroundColor': 'rgb(250, 250, 250)',
                'color': 'black'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(240, 240, 240)'
                }
            ],
            style_table={
                'maxWidth': '800px',
                'margin': 'auto'
            }
        )
    ]
)