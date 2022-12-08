import dash
from dash import Dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href='/')),
        dbc.NavItem(dbc.NavLink("Team Analysis", href='/dylanteampage')),
        dbc.NavItem(dbc.NavLink("Ref Analysis", href='/dylanrefpage')),
        dbc.NavItem(dbc.NavLink("Player Rank", href='/dylanrankpage')),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="/dylanrankpage"),
        #         dbc.DropdownMenuItem("Page 3", href="/dylanteampage"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     color="primary",
        #     label="More",
        # ),
    ],
    brand="Water Polo Data Analysis",
    color="primary",
    dark=True,
    className="mb-2",
)

for x in dash.page_registry.values():
    print(x)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=False)
