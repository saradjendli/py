donnee_meteo={"Paris":{"temperature":20.0, "humidité":60},
              "New York":{"temperature":25.0, "humidité":70},
              "Tokyo":{"temperature":28.0, "humidité":80}
}

def afficher():
    print(donnee_meteo.items())


def saisie():
    ville=input("de quelle ville voulez vous avoir des info?")
    if ville in donnee_meteo:
        print(donnee_meteo.)


def ajouter():
    ville=input("ajouter une ville")
    temperature=input("ajouter la temperature")
    humidite=input("entrez l'humidité")

    if ville in donnee_meteo:
        donnee_meteo[ville]={temperature, humidité}
                                                                                                                             