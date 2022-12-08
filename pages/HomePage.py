
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="Home")

tab1_content = dbc.Card(
    dbc.CardBody([
            html.Div([
                html.H3("WELCOME"),
                html.Img(src='assets/Bowen.jpg', style={'height':'70%', 'width':'70%'}, className='center'),
                ], style={'textAlign': 'center'}, className='mb-4'),
            html.P("Welcome to our Water Polo Analytics Website. If you have any feedback or suggestions,"
                   "email us at email@email.com. Enjoy!")
        ]), className="mt-3")

tab2_content = dbc.Card(
    dbc.CardBody([
            html.H3("Mission"),
            html.P("Our mission was to utilize current statistical data on International Water Polo Teams and "
                     "Players to better understand our sport's trends. We hope that by combining tournaments of "
                     "data, we can illuminate findings about individuals and teams that go unnoticed. We also "
                     "believe that with hard data we can not only get a better understanding of who we are as "
                     "a team, but also help guide us one where we should be going and how we can improve."),
            html.Div([
                html.Img(src='assets/Chun.jpg', style={'height': '80%', 'width': '80%'}, className='center'),
            ], style={'textAlign': 'center'}),
        ]), className="mt-3")

tab3_content = dbc.Card(
    dbc.CardBody([
            html.H3("Website Guide"),
            html.B("Team Analysis"),
            html.P("The Team Analysis Page allows you to analyze how Teams score, earn, and give up their goals,"
                   "exclusions, shots, and general stats. It allows you to filter by opponent (who they play), "
                   "the result (analyze games where a team won or lost), and by specific tournaments. The page"
                   "also gives a breif summary of the players on the team and their influence on the team's "
                   "statisitcs"),
            dbc.Button("Team Analysis", color="primary", size='sm', href='/dylanteampage', className='mb-4'),
            html.Br(),
            html.B("Ref Analysis"),
            html.P("The Ref Analysis page allows you to see referee trends: how each referee calls the game"
                   "compared to the average ref. You can filter the data by the tournament, level or quality"
                   "of the game, and who is reffing"),
            dbc.Button("Ref Analysis", color="primary", size='sm', href='/dylanrefpage', className='mb-4'),
            html.Br(),
            html.B("Rank Page"),
            html.P("The Rank page allows you to search for the best players in certain stat categories. Filter"
                   "by tournament and sort the results by total stats, stats pg, or stats per minute."),
            dbc.Button("Rank Page", color="primary", size='sm', href='/dylanrankpage', className='mb-4'),
        ]), className="mt-3")

tabs = dbc.Tabs([
    dbc.Tab(tab1_content, label="Contact"),
    dbc.Tab(tab2_content, label="Mission"),
    dbc.Tab(tab3_content, label="Website Guide")])

layout = dbc.Container([
    tabs
])