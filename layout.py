from dash import Dash,html
import dash_bootstrap_components as dbc
from component import pie_charts, bar_charts, dropdown, scatter_charts, his_charts

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXXZ2AcWw5wdNmD_EJmINiHZ3X3UEPoeiB2A&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbt_nyN1pmMX4hQyFAyyK8S1lmncgHnwBLrmKhRYweNP2ToU5bV0N2UoLTJBsAda2G6IA&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="🏘️🏘️🏘️🏘️🏘️🏘️🏘️✨✨✨✨✨✨✨✨✨", className="header-emoji"),
        html.H1(
                "Housing Price Analysis", className="header-title"
              ),
        html.P(
                "Base on the dataset we can analysis the relationship between house price and other features!!!🔥🔥🔥✨✨✨",
                className="header-description",
                ),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        dropdown.render(app),
        dropdown.render1(app),
        dropdown.render2(app)
        
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(bar_charts.render(app),lg=4),
            dbc.Col(bar_charts.render1(app),lg=4),
            dbc.Col(bar_charts.render2(app),lg=4),
            dbc.Col(scatter_charts.render(app),lg=12),
            dbc.Col(his_charts.render(app),lg=6),
            dbc.Col(pie_charts.render(app),lg=6),
            dbc.Col(scatter_charts.render1(app),lg=12),
            dbc.Col(bar_charts.render4(app),lg=6),
            dbc.Col(bar_charts.render3(app),lg=6)
        ],className="mt-4")
    ])