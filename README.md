# Comparaison des statistiques de fréquentation du site GeTribu avec les statistiques Twitter

## Contenu

Vous trouverez dans ce répertoire les scripts ayant permis de :

- Récupérer les tweets en lien avec l'activité GeoTribu, grâce à [Twint](https://github.com/twintproject/twint)
- Préparer les données précédemment récupérées grâce à [Pandas](https://pandas.pydata.org/)
- Visualiser ces données en graphique avec [Plotly](https://plotly.com/python/)

Ils sont divisés en 3 :
- <https://github.com/geotribu/stats-twitter-geotribu/tree/main/scripts/scrap-twint.py> pour le scraping de Twitter via Twint
- <https://github.com/geotribu/stats-twitter-geotribu/tree/main/scripts/prepa-visu-geordp-ga.py> pour la préparation et la visualisation des données des GeoRDP et des utilisateurs de GeoTribu
- <https://github.com/geotribu/stats-twitter-geotribu/tree/main/scripts/prepa-visu-geordp-articles-ga.py> pour la préparation et la visualisation des données des GeoRDP et des articles, avec celles des utilisateurs de GeoTribu

Les 2 graphiques présents dans l'article GeoTribu, se trouvent également dans ce répertoire :

- [Nombre de likes et retweets sur les tweets GeoRDP, comparés au nombre d'utilisateurs du site GeoTribu](https://geotribu.github.io/stats-twitter-geotribu/geordp.html)
- [Nombre de likes et retweets sur les tweets GeoRDP et articles, comparés au nombre d'utilisateurs du site GeoTribu](https://geotribu.github.io/stats-twitter-geotribu/articles.html)

## Processus

Le processus de récupération des données, préparation et visualisation est expliqué dans l'article geotribu METTRE LIEN.

Concernant l'utilisation des scripts, le premier sur la récupération va Twint des données de Twitter est nécessaire au bon fonctionnement des 2 autres.  
Pas de données, pas de graphique !

Une fois le premier exécuté, les 2 autres sont indépendants et peuvent être exécutés individuellement.

## Crédits

- [Aurélien Chaumet](https://static.geotribu.fr/team/acha/), [Geotribu](https://static.geotribu.fr)
