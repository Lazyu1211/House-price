from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_bed, get_bath, get_floor


def render(app):
    list_bedroom = get_bed()
    all_bedroom = [{'label':i,'value':i} for i in list_bedroom]
    @app.callback(
    Output(component_id='bedroom_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_bedroom(n):
        return list_bedroom

    return html.Div(
        children=[
            html.H6("Select Bedroom"),
            dcc.Dropdown(
                options=all_bedroom,
                multi=True,
                id = "bedroom_dropdown",
                value= 0
            )]
            )

def render1(app):
    list_bathroom = get_bath()
    all_bathroom = [{'label':i,'value':i} for i in list_bathroom]
    @app.callback(
    Output(component_id='bathroom_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_bedroom(n):
        return list_bathroom

    return html.Div(
        children=[
            html.H6("Select Bathroom"),
            dcc.Dropdown(
                options=all_bathroom,
                multi=True,
                id = "bathroom_dropdown",
                value= 0
            )]
            )
        
def render2(app):
    list_floor = get_floor()
    all_floor = [{'label':i,'value':i} for i in list_floor]
    @app.callback(
    Output(component_id='floor_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_bedroom(n):
        return list_floor

    return html.Div(
        children=[
            html.H6("Select Floor"),
            dcc.Dropdown(
                options=all_floor,
                multi=True,
                id = "floor_dropdown",
                value= 1
            ),
            dbc.Button(
                children=["Select all"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )