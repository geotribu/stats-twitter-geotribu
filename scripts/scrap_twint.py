# Si vous passez par un Jupyter Notebook, pensez à activer les deux lignes suivantes
# import nest_asyncio
# nest_asyncio.apply()

import twint

# Crée un fichier avec les tweets contenant "geordp" depuis le 30 avril 2020
# et les stocke dans le fichier geordp-tweets.csv
c = twint.Config()
c.Search = "geordp"
c.Since = "2020-04-30"
c.Store_csv = True
c.Output = "geordp-tweets.csv"
twint.run.Search(c)

# Crée un fichier avec les tweets contenant "geotribu" depuis le 30 avril 2020
# et les stocke dans le fichier geotribu-tweets.csv
c = twint.Config()
c.Search = "geotribu"
c.Store_csv = True
c.Since = "2020-04-30"
c.Output = "geotribu-tweets.csv"
twint.run.Search(c)