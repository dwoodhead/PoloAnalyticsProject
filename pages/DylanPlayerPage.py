import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash

from dash import dash_table, callback
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

# Import Data
df = pd.read_csv('data/master_data_all.csv')
df = df.fillna(0)
df.drop(df.columns[0], axis=1, inplace=True)
df['Outcome'] = df['Outcome'].replace('W', 1)
df['Outcome'] = df['Outcome'].replace('L', 0)
df['Last'] = df['Last'].astype(str) + ' ' + df['First'].astype(str).str[0] + '.'

# get list of teams
teamlist = sorted(df.Team.unique().tolist())

# Lists
# OpNames = {'Opponent': 'TeamT', 'Team': 'OpponentO',
#             'Goals': 'Goals Ag', 'Shots': 'Shots Ag',
#             'Action Goals': 'Action Goals Ag', 'Action Shots': 'Action Shots Ag',
#             'Center Goals': 'Center Goals Ag', 'Center Shots': 'Center Shots Ag',
#             'Extra Goals': 'Extra Goals Ag', 'Extra Shots': 'Extra Shots Ag',
#             'Foul Goals': 'Foul Goals Ag', 'Foul Shots': 'Foul Shots Ag',
#             'CA Goals': 'CA Goals Ag', 'CA Shots': 'CA Shots Ag',
#             'PS Goals': 'PS Goals Ag', 'PS Shots': 'PS Shots Ag',
#             'TF': 'TF Ag', 'ST': 'ST Ag', 'BL': 'BL Ag',
#             'CP EX': 'CP DEX', 'FP EX': 'FP DEX',
#             'DE EX':'DE DEX', 'P EX': 'P DEX',
#             'Total EX': 'Total DEX'}
# PAVG_NAMES = {'Goals': 'Goals pg', 'Shots': 'Shots pg',
#              'Action Goals': 'Action Goals pg', 'Action Shots': 'Action Shots pg',
#              'Extra Goals': 'Extra Goals pg', 'Extra Shots': 'Extra Shots pg',
#              'Center Goals': 'Center Goals pg', 'Center Shots': 'Center Shots pg',
#              'Foul Goals': 'Foul Goals pg', 'Foul Shots': 'Foul Shots pg',
#              'PS Goals': 'PS Goals pg', 'PS Shots': 'PS Shots pg',
#              'CA Goals': 'CA Goals pg', 'CA Shots': 'CA Shots pg',
#              'TF': 'TF pg', 'ST': 'ST pg', 'BL': 'BL pg',
#              'SP Won': 'SP Won pg', 'SP Attempts': 'SP Attempts pg',
#              'CP EX': 'CP EX pg', 'FP EX': 'FP EX pg',
#              'DE EX': 'DE EX pg', 'P EX': 'P EX pg',
#              'Total EX': 'Total EX pg', 'Outcome': 'Games'}
# PAVG_COLS = {'Goals': 'mean', 'Shots': 'mean',
#              'Action Goals': 'mean', 'Action Shots': 'mean',
#              'Extra Goals': 'mean', 'Extra Shots': 'mean',
#              'Center Goals': 'mean', 'Center Shots': 'mean',
#              'Foul Goals': 'mean', 'Foul Shots': 'mean',
#              'PS Goals': 'mean', 'PS Shots': 'mean',
#              'CA Goals': 'mean', 'CA Shots': 'mean',
#              'TF': 'mean', 'ST': 'mean', 'BL': 'mean',
#              'SP Won': 'mean', 'SP Attempts': 'mean',
#              'CP EX': 'mean', 'FP EX': 'mean', 'DE EX': 'mean', 'P EX': 'mean',
#              'Total EX': 'mean', 'Outcome': 'count'}
# TAVG_NAMES = {'Goals': 'Goals pg', 'Shots': 'Shots pg',
#              'Action Goals': 'Action Goals pg', 'Action Shots': 'Action Shots pg',
#              'Extra Goals': 'Extra Goals pg', 'Extra Shots': 'Extra Shots pg',
#              'Center Goals': 'Center Goals pg', 'Center Shots': 'Center Shots pg',
#              'Foul Goals': 'Foul Goals pg', 'Foul Shots': 'Foul Shots pg',
#              'PS Goals': 'PS Goals pg', 'PS Shots': 'PS Shots pg',
#              'CA Goals': 'CA Goals pg', 'CA Shots': 'CA Shots pg',
#              'TF': 'TF pg', 'ST': 'ST pg', 'BL': 'BL pg',
#              'SP Won': 'SP Won pg', 'SP Attempts': 'SP Attempts pg',
#              'CP EX': 'CP EX pg', 'FP EX': 'FP EX pg',
#              'DE EX': 'DE EX pg', 'P EX': 'P EX pg',
#              'Total EX': 'Total EX pg',
#              'Goals Ag': 'Goals Ag pg', 'Shots Ag': 'Shots Ag pg',
#              'Action Goals Ag': 'Action Goals Ag pg', 'Action Shots Ag': 'Action Shots Ag pg',
#              'Extra Goals Ag': 'Extra Goals Ag pg', 'Extra Shots Ag': 'Extra Shots Ag pg',
#              'Center Goals Ag': 'Center Goals Ag pg', 'Center Shots Ag': 'Center Shots Ag pg',
#              'Foul Goals Ag': 'Foul Goals Ag pg', 'Foul Shots Ag': 'Foul Shots Ag pg',
#              'PS Goals Ag': 'PS Goals Ag pg', 'PS Shots Ag': 'PS Shots Ag pg',
#              'CA Goals Ag': 'CA Goals Ag pg', 'CA Shots Ag': 'CA Shots Ag pg',
#              'TF Ag': 'TF Ag pg', 'ST Ag': 'ST Ag pg', 'BL Ag': 'BL Ag pg',
#              'CP DEX': 'CP DEX pg', 'FP DEX': 'FP DEX pg',
#              'DE DEX': 'DE DEX pg', 'P DEX': 'P DEX pg',
#              'Total DEX': 'Total DEX pg', 'Outcome': 'Games'}
# TAVG_COLS = {'Goals': 'mean', 'Shots': 'mean',
#              'Action Goals': 'mean', 'Action Shots': 'mean',
#              'Extra Goals': 'mean', 'Extra Shots': 'mean',
#              'Center Goals': 'mean', 'Center Shots': 'mean',
#              'Foul Goals': 'mean', 'Foul Shots': 'mean',
#              'PS Goals': 'mean', 'PS Shots': 'mean',
#              'CA Goals': 'mean', 'CA Shots': 'mean',
#              'TF': 'mean', 'ST': 'mean', 'BL': 'mean',
#              'SP Won': 'mean', 'SP Attempts': 'mean',
#              'CP EX': 'mean', 'FP EX': 'mean',
#              'DE EX': 'mean', 'P EX': 'mean', 'Total EX': 'mean',
#              'Goals Ag': 'mean', 'Shots Ag': 'mean',
#              'Action Goals Ag': 'mean', 'Action Shots Ag': 'mean',
#              'Extra Goals Ag': 'mean', 'Extra Shots Ag': 'mean',
#              'Center Goals Ag': 'mean', 'Center Shots Ag': 'mean',
#              'Foul Goals Ag': 'mean', 'Foul Shots Ag': 'mean',
#              'PS Goals Ag': 'mean', 'PS Shots Ag': 'mean',
#              'CA Goals Ag': 'mean', 'CA Shots Ag': 'mean',
#              'TF Ag': 'mean', 'ST Ag': 'mean', 'BL Ag': 'mean',
#              'CP DEX': 'mean', 'FP DEX': 'mean',
#              'DE DEX': 'mean', 'P DEX': 'mean', 'Total DEX': 'mean', 'Outcome': 'count'}

# Styles
tableheaderstyle = {'backgroundColor': 'rgb(220, 220, 220)',
                    'color': 'black',
                    'fontWeight': 'bold'}
tablestyle = {'whiteSpace': 'normal',
              'textAlign': 'center',
              'font_size': '14px',
              }

# groups by Team and Opponent, merges two df, swaps ex cols
def filterplayerdf(player, tournament, result, df2):
    dff = df2
    dff = dff.drop(dff[dff.Last != player].index)
    if tournament != "All":
        dff = dff.drop(dff[dff.Tournament != tournament].index)
    if result != "All":
        if result == 'W':
            dff = dff.drop(dff[dff.Outcome != 1].index)
        else:
            dff = dff.drop(dff[dff.Outcome != 0].index)

    dff['Minutes'] = (((dff['Minutes'] * 60) + dff['Seconds']) / 60)

    return dff
def gettables(playerstats):

    table1 = playerstats.filter(['Opponent', 'Goals', 'Shots', 'Total EX', 'BL', 'ST', 'TF',
                                 'Minutes'], axis=1)
    table2 = playerstats.filter(['Opponent', 'Action Goals', 'Action Shots', 'Extra Goals', 'Extra Shots',
                                 'Center Goals', 'Center Shots', 'CA Goals', 'CA Shots', 'Foul Goals', 'Foul Shots',
                                 'PS Goals', 'PS Shots'], axis=1)
    table3 = playerstats.filter(['Opponent', 'Total EX', 'CP EX', 'FP EX', 'DE EX', 'P EX'], axis=1)

    table1.loc[len(table1.index)] = table1.mean(numeric_only=True)
    table1.at[table1.index[-1], 'Opponent'] = 'Average'

    table2.loc[len(table2.index)] = table2.mean(numeric_only=True)
    table2.at[table2.index[-1], 'Opponent'] = 'Average'

    table3.loc[len(table3.index)] = table3.mean(numeric_only=True)
    table3.at[table3.index[-1], 'Opponent'] = 'Average'

    table1.style.highlight_max(color='lightgreen', axis=0)

    return table1.round(2), table2.round(2), table3.round(2)
# def playercompile(df2):
#     playerComp = df2.groupby('Last').sum(numeric_only=True).reset_index()
#     playerAvg = df2.groupby('Last').agg(PAVG_COLS).rename(columns=PAVG_NAMES).reset_index()
#
#     playerAvg['Minutes pg'] = (((playerComp['Minutes'] * 60) + playerComp['Seconds']) / 60) / playerAvg['Games']
#     playerAvg['Shooting %'] = playerComp['Goals'] * 100 / playerComp['Shots']
#     playerAvg['Extra Shooting %'] = playerComp['Extra Goals'] * 100 / playerComp['Extra Shots']
#     playerAvg['Center Shooting %'] = playerComp['Center Goals'] * 100 / playerComp['Center Shots']
#     playerAvg['Action Shooting %'] = playerComp['Action Goals'] * 100 / playerComp['Action Shots']
#     playerAvg['Foul Shooting %'] = playerComp['Foul Goals'] * 100 / playerComp['Foul Shots']
#     playerAvg['PS Shooting %'] = playerComp['PS Goals'] * 100 / playerComp['PS Shots']
#     playerAvg['CA Shooting %'] = playerComp['CA Goals'] * 100 / playerComp['CA Shots']
#
#     playerComp['Shooting %'] = playerComp['Goals'] * 100 / playerComp['Shots']
#     playerComp['Extra Shooting %'] = playerComp['Extra Goals'] * 100 / playerComp['Extra Shots']
#     playerComp['Center Shooting %'] = playerComp['Center Goals'] * 100 / playerComp['Center Shots']
#     playerComp['Action Shooting %'] = playerComp['Action Goals'] * 100 / playerComp['Action Shots']
#     playerComp['Foul Shooting %'] = playerComp['Foul Goals'] * 100 / playerComp['Foul Shots']
#     playerComp['PS Shooting %'] = playerComp['PS Goals'] * 100 / playerComp['PS Shots']
#     playerComp['CA Shooting %'] = playerComp['CA Goals'] * 100 / playerComp['CA Shots']
#
#     return playerComp.round(2), playerAvg.round(2)

players_master = df.drop(df[df.stat_type != 'Player'].index)

dash.register_page(__name__, name="Player Analysis")

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Player Game Stats",
                        className='text-center, mb-4'),
                width=12)
    ]),     # Title
    dbc.Row([
        dbc.Col([
            "Select a Team",
            dcc.Dropdown(
                id='team_dropdown_ppg',
                options=[{'label': t, 'value': t} for t in teamlist],
                value='USA',
            )], width={'size': 2, 'offset': 2}, id='team_output_ppg', className='mb-4'),
        dbc.Col([
            "Select Player",
            dcc.Dropdown(
                id='player_dropdown_ppg',
                options=[],
                value='BOWEN A.',
            )], width={'size': 2}, id='player_output_ppg', className='mb-4'),
        dbc.Col([
            "Tournament Filter",
            dcc.Dropdown(
                id='tournament_dropdown_ppg',
                options=[],
                value='All',
            )], width={'size': 2}, id='tournament_output_ppg', className='mb-4'),
        dbc.Col([
            "Result Filter",
            dcc.Dropdown(
                id='result_dropdown_ppg',
                options=['All', 'W', 'L'],
                value='All',
            )], width={'size': 2}, id='result_output_ppg', className='mb-4'),
    ]),     # Dropdowns
    dbc.Row([
        dbc.Col(html.H4("Player General Stats", className='text-center, mb-4'),
                width=12),

        dbc.Col(
            dash_table.DataTable(id='playerGen_table',  # initiate table
                                 css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                                 style_cell=tablestyle,
                                 style_header=tableheaderstyle,
                                 ), className='mb-4')
    ]),     # Gen Table
    dbc.Row([
        dbc.Col(html.H4("Player Shooting Stats", className='text-center, mb-4'),
                width=12),

        dbc.Col(
            dash_table.DataTable(id='playerShooting_table',  # initiate table
                                 css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                                 style_cell=tablestyle,
                                 style_header=tableheaderstyle,
                                 ), className='mb-4')
    ]),     # Shooting Table
    dbc.Row([
        dbc.Col(html.H4("Player Exclusion Stats", className='text-center, mb-4'),
                width=12),

        dbc.Col(
            dash_table.DataTable(id='playerEX_table',  # initiate table
                                 css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                                 style_cell=tablestyle,
                                 style_header=tableheaderstyle,
                                 ), className='mb-4')
    ]),     # EX Table
])

@callback(
    Output('playerGen_table', 'data'),
    Output('playerShooting_table', 'data'),
    Output('playerEX_table', 'data'),
    Output('player_dropdown_ppg', 'options'),
    Input('player_dropdown_ppg', 'value'),
    Input('tournament_dropdown_ppg', 'value'),
    Input('result_dropdown_ppg', 'value'),
    Input('team_dropdown_ppg', 'value'))
def update_tables(player, tournament, result, team):
    playerstats = players_master

    playerstats = filterplayerdf(player, tournament, result, playerstats)

    # playerstats = playercompile(playerstats)

    table1, table2, table3 = gettables(playerstats)

    # Tables
    dash_table.DataTable(id='player-table',
                         columns=[{'id': c, 'name': c} for c in table1.columns.values])  # apply to table
    playergentable = table1.to_dict('records')

    dash_table.DataTable(id='team-table',
                         columns=[{'id': c, 'name': c} for c in table2.columns.values])  # apply to table
    playershoottable = table2.to_dict('records')

    dash_table.DataTable(id='op-table',
                         columns=[{'id': c, 'name': c} for c in table3.columns.values])  # apply to table
    playerextable = table3.to_dict('records')

    dff = players_master[players_master.Team == team]
    players = sorted(dff.Last.unique().tolist())
    options = [{'label': p, 'value': p} for p in players]

    return playergentable, playershoottable, playerextable, options

@callback(
    Output('tournament_dropdown_ppg', 'options'),
    Input('team_dropdown_ppg', 'value'))
def updatedropdowns(team):
    dff = df[df.Team == team]
    tournaments = sorted(dff.Tournament.unique().tolist())
    options = [{'label': p, 'value': p} for p in tournaments]
    return options

# @callback(
#     Output('TeamShootbar', 'figure'),
#     Output('OpShootbar', 'figure'),
#     Output('DEXpie', 'figure'),
#     Output('EXpie', 'figure'),
#     Output('AVGEXpie', 'figure'),
#     Output('TeamGoalbar', 'figure'),
#     Output('OpGoalbar', 'figure'),
#     Input('team_dropdown_tpg', 'value'),
#     Input('tournament_dropdown_tpg', 'value'),
#     Input('result_dropdown_tpg', 'value'),
#     Input('opponent_dropdown_tpg', 'value'))
# def update_charts(team, tournament, result, opponent):
#     teamstats = teams_master
#     teamstats = filterteamdf(team, tournament, result, opponent, teamstats)
#
#     teamComp, teamAvg = teamcompile(teamstats)
#     teamAvg = addaverages(teamAvg)
#
#     tshoot_fig, opshoot_fig, tdex_fig, opex_fig, avgex_fig, tgoals_fig, ogoals_fig = getchartdfs(teamAvg, team)
#
#     return buildbar(tshoot_fig, team, "Team Shooting %", opponent),
#     buildbar(opshoot_fig, team, "Opponent Shooting %", opponent), \
#            buildpie(tdex_fig, team, "Team DEX pg"), buildpie(opex_fig, team, "Team EX pg"), \
#             buildpie(avgex_fig, team, "Top 8 Avg EX"), \
#            buildbar(tgoals_fig, team, "Goals pg", opponent), buildbar(ogoals_fig, team, "Opponent Goals pg", opponent)
#
# @callback(
#     Output('opponent_dropdown_tpg', 'options'),
#     Output('opponent_dropdown_copy_tpg', 'options'),
#     Input('team_dropdown_tpg', 'value'),
#     Input('tournament_dropdown_tpg', 'value'),
#     Input('result_dropdown_tpg', 'value'))
# def updatedropdowns(team, tournament, result):
#     teamstats = filterteamdf(team, tournament, result, 'All', teams_master)
#     oplistdf = teamstats.drop(teamstats[teamstats.Team != team].index)
#     oplist = sorted(oplistdf.Opponent.unique().tolist())
#
#     check = any(item in oplist for item in TOP_8)
#
#     if check is True:
#         oplist.insert(0, "TOP 8")
#
#     oplist.insert(0, "All")
#     return [{'label': t, 'value': t} for t in oplist], [{'label': t, 'value': t} for t in oplist]
#
# @callback(
#     [Output('result_dropdown_tpg', 'value'),
#      Output('result_dropdown_copy_tpg', 'value'),
#      Output('opponent_dropdown_tpg', 'value'),
#      Output('opponent_dropdown_copy_tpg', 'value')],
#     [Input('result_dropdown_tpg', 'value'),
#      Input('result_dropdown_copy_tpg', 'value'),
#      Input('opponent_dropdown_tpg', 'value'),
#      Input('opponent_dropdown_copy_tpg', 'value')])
# def linkdropdowns(result, result_copy, opponent, opponent_copy):
#     ctx = callback_context
#     trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     result_value = result if trigger_id == 'result_dropdown_tpg' else result_copy
#     opponent_value = opponent if trigger_id == 'opponent_dropdown_tpg' else opponent_copy
#
#     return result_value, result_value, opponent_value, opponent_value
#
# @callback(
#     Output('team_dropdown_tpg', 'options'),
#     Output('tournament_dropdown_tpg', 'options'),
#     Input('team_dropdown_tpg', 'value'),
#     Input('tournament_dropdown_tpg', 'value'))
# def updatedropdowns(team, tournament):
#
#     teamdf = df.filter(['Team', 'Tournament'])
#     teamdf = teamdf.drop(teamdf[teamdf.Team != team].index)
#     tournlis = sorted(teamdf['Tournament'].unique().tolist())
#     tournlis.insert(0, "All")
#
#     tourndf = df.filter(['Team', 'Tournament'])
#     if tournament != 'All':
#         tourndf = tourndf.drop(tourndf[tourndf.Tournament != tournament].index)
#         teamlis = sorted(tourndf['Team'].unique().tolist())
#     else:
#         teamlis = teamlist
#
#     return [{'label': t, 'value': t} for t in teamlis], [{'label': t, 'value': t} for t in tournlis]
