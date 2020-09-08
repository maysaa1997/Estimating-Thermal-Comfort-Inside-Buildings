__author__ = 'maysaa.khalil@utt.fr'

import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import json
import datetime
from datetime import timedelta
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def datenum_to_datetime(datenum):
    datenum = float(datenum)
    days = datenum % 1
    return datetime.fromordinal(int(datenum)) \
           + timedelta(days=days) \
           - timedelta(days=366)


# Load data
df = pd.read_csv("ContData.txt", parse_dates=['Time'])

df['datetime'] = df['Time'].apply(datenum_to_datetime)

# Group by day and compute the max temp per day
df.index = df['datetime']

# Identify the day, month and year
df['day'] = df['datetime'].map(lambda x: x.day)
df['month'] = df['datetime'].map(lambda x: x.month)
df['year'] = df['datetime'].map(lambda x: x.year)

# Axis Labels
x = [str(i) for i in range(1, 32)]
y = ['AUG', 'SEPT', 'OCT', 'NOV', 'DEC', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL']

z = []
for month, group in df.groupby('month'):
    tmp = [0] * 31
    for index, row in group.iterrows():
        i = row['day'] - 1
        tmp[i] = row['Predicted Mean Vote (PMV)']
    z.append(tmp)

app.layout = html.Div([
    dcc.Graph(

        id='heatmap',
        figure={

            'data': [{
                'z': z,
                'x': x,
                'y': y,
                'type': 'heatmap',
                'colorscale': 'RdWhBu'
            }]
        }
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('heatmap', 'hoverData'),
     Input('heatmap', 'clickData')])
def display_hoverdata(hoverData, clickData):
    return [
        json.dumps(hoverData, indent=2),
        html.Br(),
        json.dumps(clickData, indent=2)
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
