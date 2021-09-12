# Lesson from : https://github.com/Olivierpepin/30-Days-Of-Python/blob/master/25_Day_Pandas/25_pandas.md

import pandas as pd # Utilisation de la librairie Pandas

df = pd.read_csv("2020-covid19.csv", encoding="ISO-8859-1") # Lecture du fichier 2020-covide19.csv avec encodage general.

# df # Print du fichier en format prettier de pandas

# print(df) # Print en raw

# df.head(50) # Print les 50 premieres lignes (5 par defaut)

# df.tail() # Print les 5 dernieres lignes par defaut

# df.shape # Retourne le nombre de lignes et de colonnes

df.columns # Retourne les entetes des colonnes

# df['size'].shape

df.describe() # Donne des statistics de base (mean, std, min, max etc)

# Creation column

df['new_value'] = df['value'] - 10

# Modification

import pandas as pd

df = pd.read_csv("2020-covid19.csv", encoding="ISO-8859-1")

df['value'] = df['value'] * 1.15

df['value']

df

# possibilite de format (ie : changer en integer, round etc etc)

df['value'] = (int(df['value']))

# Check le type de données

df['value'].dtype

# Supprimer une column 

df = df.drop(['new_value'], axis = 1)

# ou pour sauvegarder diirectement sur le df

df.drop(['new_value'], axis = 1, inplace=True)

# Fonction creation nouvelle colonne (eviter les boucles sur DF)

'''
def new_column():
    liste = df['value']
    nliste = []
    for e in liste :
        nliste.append(e/10)
    return nliste'''

# UDF = User Define Function https://en.wikipedia.org/wiki/User-defined_function


# Indexation une colonne

df['value'] # == une serie

# Indexation plusieurs colonnes

df[['value', 'size']] # == dataframes

# Acces Lignes

df[1:5] # 4 lignes du debut du dataframe
df.iloc[1:5] # 4 lignes du debut du dataframe - iLoc
df.iloc[4] # Acces sur une seule ligne

# Combined Access
df[['value', 'size']][1:10]

# Filtres
df[df['value'] > 600][1:2]

df[((df['value'] > 600) & (df['value'] < 1000))]
df[(df['value'] > 600) | (df['value'] < 300)]

# keyword : jupyter notebook

# Librairies Data Analyst

# Bokeh : interactif graph
# Numpy
# Seaborn
# Matplotlib
# Pandas
# Sklearn (datasets.load.iris)
