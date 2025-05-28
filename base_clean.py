import pandas as pd

# Charger le CSV
df = pd.read_csv("effectif_age_sexe.csv", sep=";")

# Supprimer les colonnes vides (colonnes où toutes les valeurs sont nulles)
df = df.dropna(axis=1, how='all')

df = df[:-1]

# Sauvegarder dans un nouveau fichier propre
df.to_csv("effectif_age_sexe_2025.csv", sep=";", index=False)