from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_data


def render(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="long", 
            y="lat",
            title="Price by longitude and latitude",
            color="price",
            size="sqft_above",
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter")


def render1(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="sqft_above", 
            y="price",
            title="Price by Sqft",
            color="price",
            size="price"
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter1")
