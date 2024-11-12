donnees_geographiques={"paris":75}



def ajouter ():

    commune=input("quelle est la commune que vous cherchez? : " )
    code=input("quelle est le code de cette commune? :")
    if commune in donnees_geographiques :
        print ("existe")
    else:
        # pour ajouter une ville 
          donnees_geographiques[commune]=code
          print("j'ai ajouter")




def chercher():
      commune=input("quelle est la commune que vous cherchez? : " )

      if commune in donnees_geographiques :
        print ("cette ville est dans le dictionnaire ")
      else:
        # pour ajouter une ville 
         print("elle existe pas rajoutez la si vous voulez")


def afficher():
    print(donnees_geographiques.items())  


while True:
    choix=input("""que voulez vous choisir :
            1-ajouter la ville 
            2-chercher la ville
            3-afficher
            """)
    match choix:
        case "1": 
            ajouter ()
        case "2":
            chercher()
        case "3":
            afficher()
        case "4":
            print("vous avez quitter")
        case _:
            print("votre demande n'a pas été prise en compte")