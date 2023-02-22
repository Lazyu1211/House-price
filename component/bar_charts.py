from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_bed_price, get_bath_price, get_floor_price, get_condition_price, get_year

def render(app):
    df = get_bed_price()

    @app.callback(
        Output("bar_volume", component_property='children'),
        Input("bedroom_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("bedrooms in @dropdown")
        fig = px.bar(
                filtered_data,
                x="bedrooms",
                y="price",
                title="Average price of Bedrooms")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume")
    return html.Div(id="bar_volume")

def render1(app):
    df = get_bath_price()

    @app.callback(
        Output("bar_volume1", component_property='children'),
        Input("bathroom_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("bathrooms in @dropdown")
        fig = px.bar(
                filtered_data,
                x="bathrooms",
                y="price",
                title="Average price of Bathrooms")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume1")
    return html.Div(id="bar_volume1")

def render2(app):
    df = get_floor_price()

    @app.callback(
        Output("bar_volume2", component_property='children'),
        Input("floor_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("floors in @dropdown")
        fig = px.bar(
                filtered_data,
                x="floors",
                y="price",
                title="Average price of Floors")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume2")
    return html.Div(id="bar_volume2")

def render3(app):
    df = get_condition_price()
    fig = px.bar(
                df,
                x="condition",
                y="price",
                title="Average price of Condition")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume3")

def render4(app):
    df = get_year()
    fig = px.bar(
                df,
                x="yr_built",
                y="price",
                title="Top 150 Average price of Built year")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume4")