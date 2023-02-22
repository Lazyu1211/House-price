from dash import Dash, html, dcc
import plotly.express as px
from utill import get_view

def render(app):
    df = get_view()
    fig = px.pie(df, values = 'view', names = "index", title = 'View')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart")