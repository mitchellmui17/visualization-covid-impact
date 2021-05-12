import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import app1, app2, bar_chart, linecharts, scatterplotmat, scatterplotmat2, djia_vis
styling = {
    'background': '#111111',
    'text': '#7FDBFF',
    'padding': '14px',
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('App1 | ', href='/apps/app1'),
        dcc.Link('Heatmap | ', href='/apps/app2'),
        dcc.Link('Line Chart | ', href='/apps/linecharts'),
        dcc.Link('BarChart | ', href='/apps/barchart'),
        dcc.Link('djia | ', href='/apps/djia_vis'),
        dcc.Link('Scatterplot Matrix  | ', href='/apps/scatterplotmat2'),
    ], className="row", style={"background": "black", 'color': '#7FDBFF'}),
    html.Div(id='page-content', children=[],style={"background": "black", 'color': '#7FDBFF'}, className = 'styling')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    if pathname =='/apps/scatterplotmat':
        return scatterplotmat.layout
    if pathname =='/apps/scatterplotmat2':
        return scatterplotmat2.layout
    if pathname == '/apps/djia_vis':
        return djia_vis.layout
    if pathname == '/apps/app2':
        return app2.layout
    if pathname == '/apps/linecharts':
        return linecharts.layout
    if pathname == '/apps/barchart':
        return bar_chart.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
