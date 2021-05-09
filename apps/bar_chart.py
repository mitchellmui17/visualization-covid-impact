import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
import statistics
app = dash.Dash(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("Unemployment-2007-2021.csv"))
#years = ["2008", "2009", "2010", "2011", "2012", "2013", "2014","2015", "2016", "2017", "2018", "2019", "2020"]


app.layout = html.Div([
    html.H1("United States Unemployment Statistics 2008 - 2020", style = {"textAlign": "center", "width": "100%", "fontSize": "150%"}),
    
    html.Div([
        
        
        html.Div([
        html.Pre(children="Year", style = {"textAlign": "center", "width": "100px", "fontSize": "150%"}),
        dcc.Dropdown(
            style = {"textAlign": "center", "width": "100px"},
            id="dropdown",
            options=[{"label": x, "value": x} for x in sorted(df["Year"].unique())],
            value=2008,
            clearable=False,
        )
        ], className = 'six columns'),

        html.Div([
        html.Pre(children="States", style = {"textAlign": "center", "width": "100px", "fontSize": "150%"}),
        dcc.Dropdown(
            style = {"textAlign": "center", "width": "100px"},
            id="dropdown-state",
            options=[{"label": x, "value": x} for x in sorted(df["State"].unique())],
            value="Alabama",
            clearable=False,
        )
        ], className = 'six columns'),
    ], className = 'row'),
    
    dcc.Graph(id="bar-chart"),
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value"),
    Input("dropdown-state", "value")]
    )
def update_bar_chart(year, state):
    year_df = df[(df['Year'] == year) & (df['State'] == state)]
    #year_df = year_df.groupby(["Month"])[['Unemployment Total']]
    fig = px.bar(
        year_df, 
        y="Unemployment Total", 
        x="Month", 
        hover_data=["State", "Unemployment Rate", "Year", "Month"], 
        color = "Unemployment Rate",
        orientation = "v",
        barmode="group")
    return fig

app.run_server(debug=True)