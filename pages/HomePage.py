
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="Home")

tab1_content = dbc.Card(
    dbc.CardBody([
            html.Div([
                html.H3("WELCOME"),
                html.Img(src='assets/Bowen.jpg', style={'height':'70%', 'width':'70%'}, className='center'),
                html.Br(),
                html.Br(),
                ], style={'textAlign': 'Center'}, className='mb-4'),

            html.Div([
                html.H4("Mission"),
                html.P("Our mission was to utilize current statistical data on International Water Polo Teams and "
                       "Players to better understand our sport's trends. We hope that by combining tournaments of "
                       "data, we can illuminate findings about individuals and teams that go unnoticed. We also "
                       "believe that with hard data we can not only get a better understanding of who we are as "
                       "a team, but also help guide us one where we should be going and how we can improve."),
            ], style={'textAlign': 'left'}, className='mb-4'),

        ]), className="mt-3")

tab2_content = dbc.Card(
    dbc.CardBody([
            html.H3("Website Guide"),
            html.Br(),

            dbc.Button("Player Analysis", color="primary", size='sm', href='/dylanplayerpage'),
            html.P("The Player Analysis Page allows you to look at an individual players game stats of the course"
                   " of different tournaments and different game results."),
            html.Br(),

            dbc.Button("Team Analysis", color="primary", size='sm', href='/dylanteampage'),
            html.P("The Team Analysis Page allows you to analyze how Teams score, earn, and give up their goals,"
                   " exclusions, shots, and general stats. It allows you to filter by opponent (who they play), "
                   " the result (analyze games where a team won or lost), and by specific tournaments. The page"
                   " also gives a breif summary of the players on the team and their influence on the team's "
                   " statisitcs"),
            html.Br(),

            dbc.Button("Ref Analysis", color="primary", size='sm', href='/dylanrefpage'),
            html.P("The Ref Analysis page allows you to see referee trends: how each referee calls the game"
                   " compared to the average ref. You can filter the data by the tournament, level or quality"
                   " of the game, and who is reffing"),

            html.Br(),

            dbc.Button("Player Rank", color="primary", size='sm', href='/dylanrankpage'),
            html.P("The Player Rank page allows you to search for the best players in certain stat categories. Filter"
                   " by tournament and sort the results by total stats, stats pg, or stats per minute."),

            html.Br(),

            dbc.Button("Team Rank", color="primary", size='sm', href='/dylanteamrankpage'),
            html.P("The Team Rank page allows you to search for the best teams in certain stat categories. Filter"
                   " by tournament and sort the results by total stats or stats pg."),

        ]), className="mt-3")

tabs = dbc.Tabs([
    dbc.Tab(tab1_content, label="Mission"),
    dbc.Tab(tab2_content, label="Website Guide")])

layout = dbc.Container([
    tabs
])
