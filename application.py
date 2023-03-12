# import libraries
from dash import *
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
#from application import *
import dash
import dash_bootstrap_components as dbc

FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.10.2/css/all.css"]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE, dbc_css])
server = app.server

app.scripts.config.serve_locally = True
app.title = 'EmplacandoCars'



#Favicon from <div> Icons made by <a href="https://www.freepik.com" title="Freepik"> Freepik </a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com'</a></div>

#Variaveis

template_theme2 = "bootstrap"
template_theme1 = "slate"
url_theme1 = dbc.themes.BOOTSTRAP
url_theme2 = dbc.themes.SLATE
vencedor_auto = "assets/Automovel.png"
vencedor_com = "assets/Comercial.png"

# card and graph sStyles
tab_card = {'height': '100%'}

main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor": "top",
               "y": 0.9,
               "xanchor": "left",
               "x": 0.1,
               "title": {"text": None},
               "font": {"color": "white"},
               "bgcolor": "rgba(0,0,0,0.5)"},
    "margin": {"l": 10, "r": 10, "t": 10, "b": 10}

}
config_graph = {"displayModeBar": False, "showTips": False}

#Tema =  {'margin-top':'15px', 'margin-left':'30px'}
EstiloIconeClaro = {'margin-top':'8px', 'margin-left':'30px'}
EstiloIconeEscuro = {'margin-top':'15px', 'margin-left':'30px'}
style = EstiloIconeClaro

# ===== Reading n cleaning File ====== #
df = pd.read_csv('dataset_CarSales.csv')

df_auto = df['Categoria'] == 'Automoveis'
df_auto = df[df_auto]

df_com = df['Categoria'] == 'Comercial'
df_com = df[df_com]

df_original = df.copy()

df['Emplacados'] = df['Emplacados'].astype(int)
df['Mes'] = df['Mes'].astype(int)

# Options for filters

options_month = [{'label': 'Ano todo', 'value': 0}]
for i, j in zip(df_original['Mes'].unique(), df['Mes'].unique()):
    options_month.append({'label': i, 'value': j})
options_month = sorted(options_month, key=lambda x: x['value'])
options_month = sorted(options_month, key=lambda x: x['value'])

options_Fabricante = ['Todas'] #era 0
for i in df['Fabricante'].unique():
    options_Fabricante.append(i)

    def month_filter(month):
        if month == 0:
            mask = df['Mes'].isin(df['Mes'].unique())
        else:
            mask = df['Mes'].isin([month])
        return mask

    def fabricante_filter(fabricante):
        if fabricante == 'Todas':
            mask = df['Fabricante'].isin(df['Fabricante'].unique())
        else:
            mask = df['Fabricante'].isin([fabricante])
        return mask

    def convert_to_text(month):
        lista1 = ['Ano Todo', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                  'Outubro', 'Novembro', 'Dezembro']
        return lista1[month]

# =========  Layout  =========== #

app.layout = dbc.Container(children=[

    html.Div(

        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Página Inicial", href="http://127.0.0.1:8050/")),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Mais...", header=True),
                        dbc.DropdownMenuItem("Dados por Fabricante-modelo (Em breve)", href="#", disabled=True  ),
                        dbc.DropdownMenuItem("Detalhe Mercado (Em breve)", href="http://127.0.0.1:8050/", disabled=True  ),
                        dbc.DropdownMenuItem("Analytcs & Predictive data (Em breve)" , href="http://127.0.0.1:8050/", disabled=True  ),
                        dbc.DropdownMenuItem("👤Sobre o Autor [Linked In)", href="https://www.linkedin.com/in/sergiokmpos/"),
                        dbc.DropdownMenuItem("ℹ️Origem dos dados [Fenabrave]", href="https://www.fenabrave.org.br/"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Mais",

                ),

                #dbc.Col([' - ']),
                dbc.Col([
                    dbc.Row([
                   ThemeSwitchAIO(aio_id="theme", themes=[url_theme2, url_theme1], icons={"left":"fa fa-sun", "right":"fa fa-moon" }),
                    ], style={'margin-left': '30px', 'margin-top': '15px'})
                ]),
            ],

            brand="Dashboard de emplacamentos de veículos Brasil",
            brand_href="http://127.0.0.1:8050/",
            color="primary",
            dark=True,
            fixed=True,
        ) ,

    ),

    # Layout
    # Row 1
    dbc.Row([

        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.I(className='fa fa-database', style={'font-size': '250%'})
                            ], sm=2, align="center"),
                            dbc.Col([
                                html.Legend("EMPLACANDOCARS.COM")
                            ], sm=8),
                            dbc.Col([
                                html.I(className='fa fa-car', style={'font-size': '250%'})
                            ], sm=2, align="center")
                        ]),
                    ])
                ],style={'margin-bottom':'7px'}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph3', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='graph4', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ])
            ], className='g-2 my-auto', style={'margin-top': '7px'})
        ], sm=12, lg=3),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph1', className='dbc', config=config_graph)
                        ], sm=12, md=9),
                        dbc.Col([
                            dbc.Row(html.H5('Automoveis[Modelo]'), style={'text-align': 'center'}),
                            dcc.Graph(id='graph2', className='dbc', config=config_graph)
                        ], sm=12, lg=3),
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Row(html.H5('Comercial Leve[Modelo]'), style={'text-align': 'center'}),
                            dcc.Graph(id='graph2_2', className='dbc', config=config_graph)
                        ], sm=12, lg=3),
                        dbc.Col([
                            dcc.Graph(id='graph1_2', className='dbc', config=config_graph)
                        ], sm=12, md=9),
                    ]),


                ])
            ], style=tab_card)
        ], sm=12, lg=7),

dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(html.H5('📅 Mes'),),
                    dbc.Row([
                        dbc.Col([dcc.Dropdown([0,1,2,3,4,5,6,7,8,9,10,11,12],value=0, id='MesDropdown',  className='dbc', clearable=False )]),
                        dbc.Col([html.H5(id='month-select', style={'text-align': 'center', 'margin-top': '0px'},className='dbc')])
                    ]),
                    #dbc.Row(dcc.Dropdown([ '2021','2022','2023',], value='Ultimo Ano',className='dbc')),
                    dbc.Col([dcc.Dropdown(['Ultimo Ano'],'Ultimo Ano', id='AnoDropdown',  className='dbc', disabled=True ,clearable=False)]),

                ]),
            ],style={'margin-bottom':'7px'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(html.H5('🏭 Fabricante'), ),
                    dbc.Row(dbc.Col([dcc.Dropdown(options_Fabricante, value='Todas', id='FabricanteDropdown', className='dbc', clearable=False)])), #optionHeight=75


                ]),
            ], style={'margin-bottom': '7px'}),
            dbc.Card([
                dbc.Row(html.H5('🥇 Top 5 - Fabricante'), style={'margin-top': '10px', 'text-align': 'center'}),
                dcc.Graph(id='graph8', className='dbc', config=config_graph)
            ]),#,style=tab_card
        ], sm=12, lg=2),

    ], className='g-2 my-auto', style={'margin-top': '7px'}),

    # Row 2
    dbc.Row([
        dbc.Col([
            dbc.Row([

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row(html.H5('Quota de Mercado[Tipo]'),
                                    style={'margin-top': '0px', 'text-align': 'center'}),
                            dbc.Row([dcc.Graph(id='graph9', className='dbc', config=config_graph)])
                        ])
                    ], style=tab_card)

                ], sm=12, lg=2),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([html.H5("🏆 Mais vendidos e Porcentagem acima da media por categoria")]),
                            dbc.Row([
                            dbc.Col([dcc.Graph(id='graph5', className='dbc', config=config_graph), ],lg=2),
                            dbc.Col([html.Img(id='image_auto', src=vencedor_auto)],lg=4),
                            dbc.Col([dcc.Graph(id='graph6', className='dbc', config=config_graph), ],lg=2),
                            dbc.Col([html.Img(id='image_com', src=vencedor_com)],lg=4),

                            ])
                        ])
                    ], style=tab_card),
                ], sm=12, lg=6),


                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                        dcc.Graph(id='graph10', className='dbc', config=config_graph)
                        ])
                    ], style=tab_card)
                ],sm=12, lg=4),

            ], className='g-2'),

        ], sm=12, lg=12),

    ], className='g-2 my-auto', style={'margin-top': '7px'}),


    html.Footer(dbc.Card(["Todos direitos reservados - EmplacandoCars 2023 "], style={'text-align': 'center', 'margin-top': '7px'})),

], fluid=True, style={'height': '100vh'})

# ======= Callbacks ========== #

@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('month-select', 'children'),
    Input('MesDropdown', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph1(month, toggle):
    template = template_theme1 if toggle else template_theme2

    mask = month_filter(month)

    df_1 = df_auto.loc[mask]
    df_1 = df_1.groupby(['Modelo'])['Emplacados'].sum()
    df_1 = df_1.sort_values(ascending=False)
    df_1 = df_1.groupby('Modelo').head(1).reset_index()
    total = df_1['Emplacados'].sum()

    df_top5_auto = (df_1.head())
    totaltop5 = df_top5_auto['Emplacados'].sum()
    totaloutros = total - totaltop5
    df_top5_auto.loc[5] = ['Outros', totaloutros]

    # Gradicos
    fig2 = go.Figure(go.Pie(labels=df_top5_auto['Modelo'], values=df_top5_auto['Emplacados'], hole=.5))
    fig1 = go.Figure(go.Bar(x=df_1['Modelo'], y=df_1['Emplacados'], textposition='auto', text=df_1['Emplacados']))
    fig1.update_layout(main_config, height=225, template=template)
    fig2.update_layout(main_config, height=225, template=template, showlegend=False)

    select = html.H4(convert_to_text(month))

    return fig1, fig2, select,


@app.callback(
    Output('graph1_2', 'figure'),
    Output('graph2_2', 'figure'),
    # Output('month-select', 'children'),
    Input('MesDropdown', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph1com(month, toggle):
    template = template_theme1 if toggle else template_theme2

    mask2 = month_filter(month)

    df_1_com = df_com.loc[mask2]
    df_1_com = df_1_com.groupby(['Modelo'])['Emplacados'].sum()
    df_1_com = df_1_com.sort_values(ascending=False)
    df_1_com = df_1_com.groupby('Modelo').head(1).reset_index()
    total = df_1_com['Emplacados'].sum()

    df_top5_com = (df_1_com.head())
    totaltop5 = df_top5_com['Emplacados'].sum()
    totaloutroscom = total - totaltop5
    df_top5_com.loc[5] = ['Outros', totaloutroscom]

    # Graficos
    fig2com = go.Figure(go.Pie(labels=df_top5_com['Modelo'], values=df_top5_com['Emplacados'], hole=.5))
    fig1com = go.Figure(
        go.Bar(x=df_1_com['Modelo'], y=df_1_com['Emplacados'], textposition='auto', text=df_1_com['Emplacados']))
    fig1com.update_layout(main_config, height=225, template=template)
    fig2com.update_layout(main_config, height=225, template=template, showlegend=False)

    # select2 = html.H4(convert_to_text(month))

    return fig1com, fig2com,  # select2,


# Graph 3
@app.callback(
    Output('graph3', 'figure'),
    Input('FabricanteDropdown', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph3(fabricante, toggle):
    template = template_theme1 if toggle else template_theme2

    mask = fabricante_filter(fabricante)
    df_3 = df_auto.loc[mask]

    df_3 = df_3.groupby('Mes')['Emplacados'].sum().reset_index()
    fig3 = go.Figure(go.Scatter(
        x=df_3['Mes'], y=df_3['Emplacados'], mode='lines', fill='tonexty'))
    fig3.add_annotation(text='🚘 Automoveis por Mes',
                       xref="paper", yref="paper",
                        font=dict(
                            size=17,
                            color='gray'
                        ),
                        align="center", bgcolor="rgba(0,0,0,0.8)",
                        x=0.05, y=0.05, showarrow=False)
    fig3.add_annotation(text=f"Média : {round((df_3['Emplacados'].mean())/1000)}k",#, 0
                        xref="paper", yref="paper",
                        font=dict(
                            size=20,
                            color='gray'
                        ),
                        align="center", bgcolor="rgba(0,0,0,0.8)",
                        x=0.05, y=0.25, showarrow=False)

    fig3.update_layout(main_config, height=195, template=template)
    return fig3


# Graph 4
@app.callback(
    Output('graph4', 'figure'),
    Input('FabricanteDropdown', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph4(fabricante, toggle):
    template = template_theme1 if toggle else template_theme2

    mask = fabricante_filter(fabricante)
    df_4 = df_com.loc[mask]

    df_4 = df_4.groupby('Mes')['Emplacados'].sum().reset_index()
    fig4 = go.Figure(go.Scatter(
        x=df_4['Mes'], y=df_4['Emplacados'], mode='lines', fill='tonexty'))
    fig4.add_annotation(text='🛻 Comerciais leves por Mes',
                        xref="paper", yref="paper",
                        font=dict(
                            size=17,
                            color='gray'
                        ),
                        align="center", bgcolor="rgba(0,0,0,0.8)",
                        x=0.05, y=0.05, showarrow=False)
    fig4.add_annotation(text=f"Média : {round((df_4['Emplacados'].mean())/1000)}k",#, 0
                        xref="paper", yref="paper",
                        font=dict(
                            size=20,
                            color='gray'
                        ),
                        align="center", bgcolor="rgba(0,0,0,0.8)",
                        x=0.05, y=0.25, showarrow=False)

    fig4.update_layout(main_config, height=195, template=template)

    return fig4


# Indicators 1 and 2 ------ Graph 5 and 6

@app.callback(
    Output('graph5', 'figure'),
    Output('graph6', 'figure'),
    Output('image_auto', 'src'),
    Output('image_com', 'src'),
    Input('MesDropdown', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph5(month, toggle):
    template = template_theme1 if toggle else template_theme2

    mask = month_filter(month)
    df_5 = df_auto.loc[mask]

    df_5 = df_5.groupby(['Modelo', 'Fabricante'])['Emplacados'].sum()
    df_5.sort_values(ascending=False, inplace=True)
    df_5 = df_5.reset_index()
    fig5 = go.Figure()

    fig5.add_trace(go.Indicator(mode='number+delta',
                                title={
                                    "text": f"<span style='font-size 100%'>{df_5['Modelo'].iloc[0]}"
                                            f" - 🚘 </span><br>"},
                                # f"<span style='font-size:70%'>Em vendas - em relação a média</span><br>"},
                                value=df_5['Emplacados'].iloc[0],
                                number={'prefix': ""},  # R$
                                delta={'relative': True, 'valueformat': '.1%', 'reference': df_5['Emplacados'].mean()}
                                ), )

    df_6 = df_com.loc[mask]

    df_6 = df_6.groupby(['Modelo', 'Fabricante'])['Emplacados'].sum()
    df_6.sort_values(ascending=False, inplace=True)
    df_6 = df_6.reset_index()
    fig6 = go.Figure()

    fig6.add_trace(go.Indicator(mode='number+delta',
                                title={
                                    "text": f"<span style='font-size 100%'>{df_6['Modelo'].iloc[0]}"
                                            f" - 🛻 </span><br>"},
                                # f"<span style='font-size:70%'>Em vendas - em relação a média</span><br>"},
                                value=df_6['Emplacados'].iloc[0],
                                number={'prefix': ""},  # R$
                                delta={'relative': True, 'valueformat': '.1%', 'reference': df_6['Emplacados'].mean()}
                                ), )

    fig5.update_layout(main_config, height=190, template=template)
    fig6.update_layout(main_config, height=190, template=template)
    fig5.update_layout({"margin": {"l": 0, "r": 0, "t": 20, "b": 0}})
    fig6.update_layout({"margin": {"l": 0, "r": 0, "t": 20, "b": 0}})

    vencedor_auto2 = df_5['Modelo'].iloc[0]
    src = "assets/" + vencedor_auto2 + ".png"

    vencedor_com2 = df_6['Modelo'].iloc[0]
    src2 = "assets/" + vencedor_com2 + ".png"

    return fig5, fig6, src, src2



# Graph 8
@app.callback(
    Output('graph8', 'figure'),
    Input('MesDropdown', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph8(month, toggle):
    template = template_theme1 if toggle else template_theme2

    mask = month_filter(month)

    df_8 = df.loc[mask]

    df_8 = df_8.groupby('Fabricante')['Emplacados'].sum().reset_index()
    df_8.sort_values('Emplacados', ascending=True, inplace=True)
    df_8 = df_8.tail(5)
    fig8 = go.Figure(go.Bar(
        x=df_8['Emplacados'],
        y=df_8['Fabricante'],
        orientation='h',
        textposition='auto',
        text=df_8['Emplacados'],
        insidetextfont=dict(family='Times', size=12)))

    fig8.update_layout(main_config, height=250, template=template)
    return fig8


# Graph 9
@app.callback(
    Output('graph9', 'figure'),
    Input('MesDropdown', 'value'),
    Input('FabricanteDropdown', 'value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph9(month, fabricante, toggle):
    template = template_theme1 if toggle else template_theme2

    mask = month_filter(month)
    df_9 = df.loc[mask]

    mask = fabricante_filter(fabricante)
    df_9 = df_9.loc[mask]

    df_9 = df_9.groupby('Tipo')['Emplacados'].sum().reset_index()

    fig9 = go.Figure()
    fig9.add_trace(go.Pie(labels=df_9['Tipo'], values=df_9['Emplacados'], hole=.5))

    fig9.update_layout(main_config, height=190, template=template, showlegend=False)
    return fig9


# Graph 10
@app.callback(
    Output('graph10', 'figure'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def graph10(toggle):
    template = template_theme1 if toggle else template_theme2

    df_10 = df.groupby(['Mes', 'Tipo'])['Emplacados'].sum().reset_index()

    fig10 = px.line(df_10, y="Emplacados", x="Mes", color="Tipo")

    fig10.update_layout(main_config, yaxis={'title': 'Emplacados por tipo'}, xaxis={'title': None}, height=232,
                        template=template, legend={'traceorder': 'normal'}),
    fig10.update_layout(legend=dict(yanchor="top", y=1.0, xanchor="left", x=1.0, ))
    return fig10

# Run server
if __name__ == '__main__':
    app.run_server(debug=False)
