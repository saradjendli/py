texte = "exemple@gmail.com"

# Étape 1 : Séparer avec un seul @
parties = texte.split('@', 1)  # Le 1 signifie qu'on divise au maximum une fois

# Étape 2 : Gérer les points dans les deux parties séparément
nom_utilisateur = parties[0]
domaine = parties[1].split('.', 1)  # Divise la partie du domaine en deux par le premier point

print(nom_utilisateur)  # 'exemple'
print(domaine[0])       # 'gmail'
print(domaine[1])       # 'com'
