# Importe la bibliothèque Pandas
import pandas as pd
# Importe les bibliothèques de Plotly nécessaires à la visualisation
import plotly.express as px
import plotly.graph_objects as go
import datetime
from plotly.subplots import make_subplots
from plotly.graph_objs import *

# 1ère partie préparant les données pour l'affichage des statistiques des GeoRDP et de la fréquentation de GeoTribu
# Lit les tweets récupérés via Twint
geordp_tweets = pd.read_csv("geordp-tweets.csv")

# On ne garde que les tweets de publication d'origine avec les colonnes nous intéressant
geordp = geordp_tweets[['date','likes_count','retweets_count','geordp','geordp_date']].loc[geordp_tweets["geordp"]=="oui"].loc[geordp_tweets['date'] < '2021-01-01']

# On regroupe les tweets originels avec les retweets cités
geordp_retweets = geordp.groupby(['geordp_date']).sum().reset_index()

# Crée une colonne pour les années et une autre pour les numéros de semaine pour les tweets geordp
geordp_retweets['geordp_date'] = pd.to_datetime(geordp_retweets['geordp_date'])
geordp_retweets['Week_Number'] = geordp_retweets['geordp_date'].dt.isocalendar().week

# Lit les statistiques utilisateurs de Google Analytics de GeoTribu
users = pd.read_csv("ga_users.csv").rename(columns={"Index des jours": "date", "Utilisateurs": "nb_users"})

# On ne garde que la période qui nous intéresse
# Ici du 1er mai au 31 décembre 2020
users['date'] = pd.to_datetime(users['date'], dayfirst=True)
users_geordp = users.loc[(users['date'] >= '2020-04-30') & (users['date'] < '2021-01-01')]

# Crée une colonne pour les années et une autre pour les numéros de semaine pour les users
users_geordp['Week_Number'] = users_geordp['date'].dt.isocalendar().week
users_geordp['Year_Number'] = users_geordp['date'].dt.isocalendar().year

# Renvoie le nombre d'utilisateurs en entier
users_geordp['nb_users'] = users_geordp['nb_users'].astype(str).astype(int)

# Somme sur le nombre d'utilisateurs par semaine
users_geordp_w = users_geordp.groupby(['Year_Number','Week_Number']).sum().reset_index()

# On récupéère une date de chaque semaine pour afficher les données
dates = users_geordp_w.Year_Number*100+users_geordp_w.Week_Number

# Décale les données Google Analytics pour qu'elles osient plus comparables aux stats des tweets
users_geordp_w['date'] = pd.to_datetime(dates.astype(str) + '0', format='%Y%W%w') - pd.DateOffset(14)

# On itère sur les semaines pour sommer le nb_users toutes les 2 semaines sur 2020
users_geordp_w_2020 = users_geordp_w.loc[(users_geordp_w['Year_Number'] == 2020)]

two_weeks = []
for w in users_geordp_w_2020['Week_Number']:
    if (w % 2) != 0:
        u = users_geordp_w_2020['nb_users'][w-19] + users_geordp_w_2020['nb_users'][w-18]
        two_weeks.append(u)
    else:
        two_weeks.append(0)

users_geordp_w_2020['two_weeks'] = two_weeks

users_geordp_two_w = users_geordp_w_2020.loc[users_geordp_w_2020['two_weeks'] != 0]


# 2ème partie créant le graphique
# Crée un layout pour le graphique
layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Crée la figure principale
fig = go.Figure(layout=layout)

# Ajoute les 3 traces dans la figure principale
fig.add_trace(go.Scatter(x=geordp_retweets['geordp_date'],
                         y=geordp_retweets['likes_count'],
                         mode='lines+markers',
                         name='Likes',
                         text = geordp_retweets['likes_count'].astype(str)+' likes',
                         hoverinfo='x+text'))

fig.add_trace(go.Scatter(x=geordp_retweets['geordp_date'],
                         y=geordp_retweets['retweets_count'],
                         mode='lines+markers',
                         name='Retweets',
                         text = geordp_retweets['retweets_count'].astype(str)+' retweets',
                         hoverinfo='text'))

fig.add_trace(go.Scatter(x=users_geordp_two_w['date'],
                         y=users_geordp_two_w['two_weeks'],
                         mode='lines',
                         name="Nombre d'utilisateurs GeoTribu",
                         yaxis="y2",
                         line = dict(color='#75ca9b'),
                         text = users_geordp_two_w['two_weeks'].astype(str)+' utilisateurs',
                         hoverinfo='x+text'))

# Liste les dates de publications des GeoRDP
geordp_publi = ['2020-12-24', '2020-12-11', '2020-11-27', '2020-11-13', '2020-10-30', '2020-10-16', '2020-10-02', '2020-09-18',
                '2020-09-04', '2020-08-21', '2020-08-07', '2020-07-27', '2020-07-10', '2020-06-26', '2020-06-12', '2020-05-29', '2020-05-15', '2020-04-30']

# Les ajoute à la figure
for date in geordp_publi:
    fig.add_vline(x=date,
                 line=dict(color='#FFB299',
                           width=1,
                           dash='dash'))

# Ajoute le logo GeoTribu en fond
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/aurelienchaumet/aurelienchaumet.github.io/master/data/geotribu_stats/geotribu_banner_1000x760.jpg",
        x=0,
        y=1,
        xref="paper",
        yref="paper",
        sizex=1,
        sizey=1,
        sizing="stretch",
        layer="below",
        opacity=0.2
        )
)

# Ajoute l'annotation pour les publis GeoRDP
fig.add_annotation(
    xref="x domain",
    yref="y",
    x=0.105,
    y=55,
    text="Publication des GeoRDP",
    axref="x domain",
    ayref="y",
    ax=0.2,
    ay=60,
    arrowhead=2,
    arrowcolor='#FFB299',
    font = {'color':'#CC8E7A'}
)

# Crée le titre, les légends des axes et la légende
fig.update_layout(
    title={'text':"Nombre de likes et retweets sur les tweets GeoRDP, <br>comparés au nombre d'utilisateurs du site GeoTribu",
           'x':0.5,
           'y':0.95,
           'xanchor': 'center'},
    hovermode='x',
    yaxis=dict(
        title="Nombre de likes et retweets",
        titlefont=dict(color="#1f77b4"),
        tickfont=dict(color="#1f77b4")
    ),
    yaxis2=dict(
        title="Nombre d'utilisateurs GeoTribu",
        titlefont=dict(
            color="#75ca9b"
        ),
        tickfont=dict(
            color="#75ca9b"
        ),
        anchor="x",
        overlaying="y",
        side="right"
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1)
)

# Supprime les grilles horizontales et verticales de la figure
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

# Dans un Jupyter Notebook, permet l'affichage du graph
#fig.show()

# Exporte le graphique dans un fichier HTML
fig.write_html("geordp.html")