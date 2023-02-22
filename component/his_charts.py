from dash import Dash,html,dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_base_price

def render(app):
    df = get_base_price()
    fig = px.histogram(df, x="sqft_basement", title="Basement Sqft")
    return html.Div(dcc.Graph(figure=fig), id="his")
    return html.Div(id="his")