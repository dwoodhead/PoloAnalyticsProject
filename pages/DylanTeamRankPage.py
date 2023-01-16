import dash
from dash import dash_table, callback
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

df = pd.read_csv('data/master_data_all.csv')
df = df.fillna(0)
df.drop(df.columns[0], axis=1, inplace=True)
df['Outcome'] = df['Outcome'].replace('W', 1)
df['Outcome'] = df['Outcome'].replace('L', 0)
df['Last'] = df['Last'].astype(str) + ' ' + df['First'].astype(str).str[0] + '.'

# Lists
TOP_8 = ['ITA', 'GRE', 'SRB', 'USA', 'HUN', 'ESP', 'CRO', 'MNE']
KNOCK_GAMES = ['OLY2020-31', 'OLY2020-32', 'OLY2020-33', 'OLY2020-34', 'OLY2020-35', 'OLY2020-36',
               'OLY2020-37', 'OLY2020-38', 'OLY2020-39', 'OLY2020-40', 'OLY2020-41', 'OLY2020-42',
               'WC2022-41', 'WC2022-42', 'WC2022-43', 'WC2022-44', 'WC2022-45', 'WC2022-46',
               'WC2022-47', 'WC2022-48', 'WC2022-35', 'WC2022-36', 'WC2022-37', 'WC2022-38']
OpNames = {'Opponent': 'TeamT', 'Team': 'OpponentO',
           'Goals': 'Goals Ag', 'Shots': 'Shots Ag',
           'Action Goals': 'Action Goals Ag', 'Action Shots': 'Action Shots Ag',
           'Center Goals': 'Center Goals Ag', 'Center Shots': 'Center Shots Ag',
           'Extra Goals': 'Extra Goals Ag', 'Extra Shots': 'Extra Shots Ag',
           'Foul Goals': 'Foul Goals Ag', 'Foul Shots': 'Foul Shots Ag',
           'CA Goals': 'CA Goals Ag', 'CA Shots': 'CA Shots Ag',
           'PS Goals': 'PS Goals Ag', 'PS Shots': 'PS Shots Ag',
           'TF': 'TF Ag', 'ST': 'ST Ag', 'BL': 'BL Ag',
           'CP EX': 'CP DEX', 'FP EX': 'FP DEX',
           'DE EX': 'DE DEX', 'P EX': 'P DEX',
           'Total EX': 'Total DEX'}
PAVG_NAMES = {'Goals': 'Goals pg', 'Shots': 'Shots pg',
              'Action Goals': 'Action Goals pg', 'Action Shots': 'Action Shots pg',
              'Extra Goals': 'Extra Goals pg', 'Extra Shots': 'Extra Shots pg',
              'Center Goals': 'Center Goals pg', 'Center Shots': 'Center Shots pg',
              'Foul Goals': 'Foul Goals pg', 'Foul Shots': 'Foul Shots pg',
              'PS Goals': 'PS Goals pg', 'PS Shots': 'PS Shots pg',
              'CA Goals': 'CA Goals pg', 'CA Shots': 'CA Shots pg',
              'TF': 'TF pg', 'ST': 'ST pg', 'BL': 'BL pg',
              'SP Won': 'SP Won pg', 'SP Attempts': 'SP Attempts pg',
              'CP EX': 'CP EX pg', 'FP EX': 'FP EX pg',
              'DE EX': 'DE EX pg', 'P EX': 'P EX pg',
              'Total EX': 'Total EX pg', 'Outcome': 'Games'}
PAVG_COLS = {'Goals': 'mean', 'Shots': 'mean',
             'Action Goals': 'mean', 'Action Shots': 'mean',
             'Extra Goals': 'mean', 'Extra Shots': 'mean',
             'Center Goals': 'mean', 'Center Shots': 'mean',
             'Foul Goals': 'mean', 'Foul Shots': 'mean',
             'PS Goals': 'mean', 'PS Shots': 'mean',
             'CA Goals': 'mean', 'CA Shots': 'mean',
             'TF': 'mean', 'ST': 'mean', 'BL': 'mean',
             'SP Won': 'mean', 'SP Attempts': 'mean',
             'CP EX': 'mean', 'FP EX': 'mean', 'DE EX': 'mean', 'P EX': 'mean',
             'Total EX': 'mean', 'Outcome': 'count'}
TAVG_NAMES = {'Goals': 'Goals pg', 'Shots': 'Shots pg',
              'Action Goals': 'Action Goals pg', 'Action Shots': 'Action Shots pg',
              'Extra Goals': 'Extra Goals pg', 'Extra Shots': 'Extra Shots pg',
              'Center Goals': 'Center Goals pg', 'Center Shots': 'Center Shots pg',
              'Foul Goals': 'Foul Goals pg', 'Foul Shots': 'Foul Shots pg',
              'PS Goals': 'PS Goals pg', 'PS Shots': 'PS Shots pg',
              'CA Goals': 'CA Goals pg', 'CA Shots': 'CA Shots pg',
              'TF': 'TF pg', 'ST': 'ST pg', 'BL': 'BL pg',
              'SP Won': 'SP Won pg', 'SP Attempts': 'SP Attempts pg',
              'CP EX': 'CP EX pg', 'FP EX': 'FP EX pg',
              'DE EX': 'DE EX pg', 'P EX': 'P EX pg',
              'Total EX': 'Total EX pg',
              'Goals Ag': 'Goals Ag pg', 'Shots Ag': 'Shots Ag pg',
              'Action Goals Ag': 'Action Goals Ag pg', 'Action Shots Ag': 'Action Shots Ag pg',
              'Extra Goals Ag': 'Extra Goals Ag pg', 'Extra Shots Ag': 'Extra Shots Ag pg',
              'Center Goals Ag': 'Center Goals Ag pg', 'Center Shots Ag': 'Center Shots Ag pg',
              'Foul Goals Ag': 'Foul Goals Ag pg', 'Foul Shots Ag': 'Foul Shots Ag pg',
              'PS Goals Ag': 'PS Goals Ag pg', 'PS Shots Ag': 'PS Shots Ag pg',
              'CA Goals Ag': 'CA Goals Ag pg', 'CA Shots Ag': 'CA Shots Ag pg',
              'TF Ag': 'TF Ag pg', 'ST Ag': 'ST Ag pg', 'BL Ag': 'BL Ag pg',
              'CP DEX': 'CP DEX pg', 'FP DEX': 'FP DEX pg',
              'DE DEX': 'DE DEX pg', 'P DEX': 'P DEX pg',
              'Total DEX': 'Total DEX pg', 'Outcome': 'Games'}
TAVG_COLS = {'Goals': 'mean', 'Shots': 'mean',
             'Action Goals': 'mean', 'Action Shots': 'mean',
             'Extra Goals': 'mean', 'Extra Shots': 'mean',
             'Center Goals': 'mean', 'Center Shots': 'mean',
             'Foul Goals': 'mean', 'Foul Shots': 'mean',
             'PS Goals': 'mean', 'PS Shots': 'mean',
             'CA Goals': 'mean', 'CA Shots': 'mean',
             'TF': 'mean', 'ST': 'mean', 'BL': 'mean',
             'SP Won': 'mean', 'SP Attempts': 'mean',
             'CP EX': 'mean', 'FP EX': 'mean',
             'DE EX': 'mean', 'P EX': 'mean', 'Total EX': 'mean',
             'Goals Ag': 'mean', 'Shots Ag': 'mean',
             'Action Goals Ag': 'mean', 'Action Shots Ag': 'mean',
             'Extra Goals Ag': 'mean', 'Extra Shots Ag': 'mean',
             'Center Goals Ag': 'mean', 'Center Shots Ag': 'mean',
             'Foul Goals Ag': 'mean', 'Foul Shots Ag': 'mean',
             'PS Goals Ag': 'mean', 'PS Shots Ag': 'mean',
             'CA Goals Ag': 'mean', 'CA Shots Ag': 'mean',
             'TF Ag': 'mean', 'ST Ag': 'mean', 'BL Ag': 'mean',
             'CP DEX': 'mean', 'FP DEX': 'mean',
             'DE DEX': 'mean', 'P DEX': 'mean', 'Total DEX': 'mean', 'Outcome': 'count'}
PER_STATS = {'Shooting %', 'Extra Shooting %', 'Center Shooting %', 'Action Shooting %',
          'Foul Shooting %', 'PS Shooting %', 'CA Shooting %'}

# Styles
tableheaderstyle = {'backgroundColor': 'rgb(220, 220, 220)',
                    'color': 'black',
                    'fontWeight': 'bold'}
tablestyle = {'whiteSpace': 'normal',
              'textAlign': 'center',
              'font_size': '14px',
              }
pietitlestyle = {
    'y': 0.95,  # new
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'  # new
}
bartitlestyle = {
    'y': 0.95,  # new
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'  # new
}

# groups by Team and Opponent, merges two df, swaps ex cols
def mergeteamdf(data):
    dff = data.drop(data[data.stat_type != "Team"].index)
    dff = dff.drop(['Last', 'First', 'Play Time', 'Minutes', 'Seconds', 'Match Number', 'Ref 1', 'Ref 2'], axis=1)

    team = dff
    op = dff
    op = op.drop(['SP Won', 'SP Attempts', 'Outcome'], axis=1)

    op = op.rename(columns=OpNames)
    op.set_index('TeamT')
    team.set_index('Team')

    for i in range(len(op)):
        num = i % 2
        if num == 0:
            temp = op.iloc[i]
            op.iloc[i] = op.iloc[i + 1]
            op.iloc[i + 1] = temp

    master = pd.concat([team, op], axis=1)
    master = master.drop(['TeamT', 'OpponentO', 'stat_type'], axis=1).set_index('Team')

    return master

def filterteamdf(tournament, gamet, data):
    dff = data
    if tournament != "All":
        dff = dff.drop(dff[dff.Tournament != tournament].index)
    if gamet != "All":
        if gamet == "TOP 8":
            dff = dff[dff['Opponent'].isin(TOP_8)]
        if gamet != "TOP 8":
            dff = dff[dff['Match Number'].isin(KNOCK_GAMES)]
    return dff

def teamcompile(dff):
    teamComp = dff.groupby('Team').sum(numeric_only=True).reset_index()
    teamAvg = dff.groupby('Team').agg(TAVG_COLS).rename(columns=TAVG_NAMES).reset_index()
    teamComp = teamComp.rename(columns={'Outcome': 'Wins'})

    teamComp['Games'] = teamAvg['Games']
    teamComp['Shooting %'] = teamComp['Goals'] * 100 / teamComp['Shots']
    teamComp['Extra Shooting %'] = teamComp['Extra Goals'] * 100 / teamComp['Extra Shots']
    teamComp['Center Shooting %'] = teamComp['Center Goals'] * 100 / teamComp['Center Shots']
    teamComp['Action Shooting %'] = teamComp['Action Goals'] * 100 / teamComp['Action Shots']
    teamComp['Foul Shooting %'] = teamComp['Foul Goals'] * 100 / teamComp['Foul Shots']
    teamComp['PS Shooting %'] = teamComp['PS Goals'] * 100 / teamComp['PS Shots']
    teamComp['CA Shooting %'] = teamComp['CA Goals'] * 100 / teamComp['CA Shots']

    teamComp['Op Shooting %'] = teamComp['Goals Ag'] * 100 / teamComp['Shots Ag']
    teamComp['Op Extra Shooting %'] = teamComp['Extra Goals Ag'] * 100 / teamComp['Extra Shots Ag']
    teamComp['Op Center Shooting %'] = teamComp['Center Goals Ag'] * 100 / teamComp['Center Shots Ag']
    teamComp['Op Action Shooting %'] = teamComp['Action Goals Ag'] * 100 / teamComp['Action Shots Ag']
    teamComp['Op Foul Shooting %'] = teamComp['Foul Goals Ag'] * 100 / teamComp['Foul Shots Ag']
    teamComp['Op PS Shooting %'] = teamComp['PS Goals Ag'] * 100 / teamComp['PS Shots Ag']
    teamComp['Op CA Shooting %'] = teamComp['CA Goals Ag'] * 100 / teamComp['CA Shots Ag']

    teamAvg['Shooting %'] = teamComp['Goals'] * 100 / teamComp['Shots']
    teamAvg['Extra Shooting %'] = teamComp['Extra Goals'] * 100 / teamComp['Extra Shots']
    teamAvg['Center Shooting %'] = teamComp['Center Goals'] * 100 / teamComp['Center Shots']
    teamAvg['Action Shooting %'] = teamComp['Action Goals'] * 100 / teamComp['Action Shots']
    teamAvg['Foul Shooting %'] = teamComp['Foul Goals'] * 100 / teamComp['Foul Shots']
    teamAvg['PS Shooting %'] = teamComp['PS Goals'] * 100 / teamComp['PS Shots']
    teamAvg['CA Shooting %'] = teamComp['CA Goals'] * 100 / teamComp['CA Shots']
    teamAvg['Win %'] = teamComp['Wins'] / teamComp['Games']

    teamAvg['Op Shooting %'] = teamComp['Goals Ag'] * 100 / teamComp['Shots Ag']
    teamAvg['Op Extra Shooting %'] = teamComp['Extra Goals Ag'] * 100 / teamComp['Extra Shots Ag']
    teamAvg['Op Center Shooting %'] = teamComp['Center Goals Ag'] * 100 / teamComp['Center Shots Ag']
    teamAvg['Op Action Shooting %'] = teamComp['Action Goals Ag'] * 100 / teamComp['Action Shots Ag']
    teamAvg['Op Foul Shooting %'] = teamComp['Foul Goals Ag'] * 100 / teamComp['Foul Shots Ag']
    teamAvg['Op PS Shooting %'] = teamComp['PS Goals Ag'] * 100 / teamComp['PS Shots Ag']
    teamAvg['Op CA Shooting %'] = teamComp['CA Goals Ag'] * 100 / teamComp['CA Shots Ag']

    return teamComp.round(2), teamAvg.round(2)

def gettable(teamComp, teamAvg, stat, sort):
    table1 = teamComp.filter(['Team', stat], axis=1)

    table1[stat + ' pg'] = teamAvg[stat + ' pg']
    table1['Win %'] = teamComp['Wins'] / teamAvg['Games']

    if sort == 'Total':
        table1 = table1.sort_values(by=[stat], ascending=False)
    if sort == 'Per Game':
        table1 = table1.sort_values(by=[stat + ' pg'], ascending=False)
    if sort == 'Win %':
        table1 = table1.sort_values(by=['Win %'], ascending=False)

    return table1.round(2)

players_master = df.drop(df[df.stat_type != 'Player'].index)
teams_master = mergeteamdf(df).reset_index()

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
dash.register_page(__name__, name="Team Ranking")

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Team Rank Page",
                        className='text-center, mb-4'),
                width=12)
    ]),  # Title
    dbc.Row([
        dbc.Col([
            "Select a Stat",
            dcc.Dropdown(
                id='stat_dropdown_trpg',
                options=['Goals', 'Shots', 'Total EX',
                         'Action Goals', 'Action Shots', 'Extra Goals', 'Extra Shots',
                         'Center Goals', 'Center Shots', 'Foul Goals', 'Foul Shots',
                         'PS Goals', 'PS Shots', 'CA Goals',
                         'CA Shots', 'TF', 'ST', 'BL', 'SP Won', 'SP Attempts',
                         'CP EX', 'FP EX', 'DE EX', 'P EX'],
                value='Goals',
            )], width={'size': 2, 'offset': 1}, className='mb-4'),
        dbc.Col([
            "Tournament Filter",
            dcc.Dropdown(
                id='tournament_dropdown_trpg',
                options=['All', 'OLY2020', 'WC2022', 'EC2022'],
                value='All',
            )], width={'size': 2}, className='mb-4'),
        dbc.Col([
            "Game Type Filter",
            dcc.Dropdown(
                id='gamet_dropdown_trpg',
                options=['All', 'TOP 8', 'Knockout Round'],
                value='All'
            )], width={'size': 2}, className='mb-4'),
        dbc.Col([
            "Sort by",
            dcc.Dropdown(
                id='sort_dropdown_trpg',
                options=['Total', 'Per Game', 'Win %'],
                value='Total'
            )], width={'size': 2}, className='mb-4')
    ]),  # Dropdowns
    dbc.Row([
        dbc.Col(html.H4("Team Stats", className='text-center, mb-4'),
                width=12),

        dbc.Col(
            dash_table.DataTable(id='teamStats_table_trpg',  # initiate table
                                 css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                                 style_cell=tablestyle,
                                 style_header=tableheaderstyle,
                                 ), className='mb-4')
    ]),  # Team Table
])

@callback(
    Output('teamStats_table_trpg', 'data'),
    Input('stat_dropdown_trpg', 'value'),
    Input('tournament_dropdown_trpg', 'value'),
    Input('gamet_dropdown_trpg', 'value'),
    Input('sort_dropdown_trpg', 'value'))
def update_tables(stat, tournament, gamet, sort):
    teamstats = teams_master

    teamstats = filterteamdf(tournament, gamet, teamstats)

    teamComp, teamAvg = teamcompile(teamstats)

    table1 = gettable(teamComp, teamAvg, stat, sort)

    # Tables
    dash_table.DataTable(id='player-table',
                         columns=[{'id': c, 'name': c} for c in table1.columns.values])  # apply to table
    team_table = table1.to_dict('records')

    return team_table