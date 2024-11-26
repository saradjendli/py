
reseau= {
    101:{"nom":"Capteur de temperature", "etat":"inactif"},
    102:{"nom":"Capteur d'humidite", "etat":"actif"},
    103:{"nom":"Capteur de pression", "etat":"inactif"}
}


def ajouter_peripherique(id, nom, etat,reseau):
    # id=int(input("saisisez l'id:"))

    if id in reseau:
        print("l'id est deja utilise choisissez un autre")
    else:   
        # nom=input("saisisez le nom:")
        # etat=input("indiquez l'etat:")

        reseau[id]={"nom":nom, "etat":etat}
        print(f"j'ai ajouter le peripherique numero {id}")
        


def supprimer_peripherique(id, reseau):
        if id not in reseau:
             print("l'id n'est pas reconnu dans le dictionnaire")
        else:
            del reseau[id]
            print(f"jai supprime le peripherique {id}")


def afficher_peripheriques():
    print(reseau.items())

def modifier_etat(id,etat,reseau):
     if id in reseau:
          reseau[id]={"etat":etat}
          print(f"Les donnees ont ete mises a jour.")
     else:
          print("l'id n'est pas reconnu")
         





def afficher_peripheriques_actifs(reseau):
    tous_actifs = all(reseau=="actif"
    for element in reseau.values())
    print(tous_actifs)








while True:
    choix=input("""que voulez vous choisir :
            1-ajouter un peripherique
            2-supprimer un peripherique
            3-mofier l'etat
            4-afficher les peripheriques 
            5-afficher les peripheriques actifs
            6-quitter
             """)
    match choix:
        case "1": 
             ajouter_peripherique(104,"capteur","actif", reseau)
        case "2":
            supprimer_peripherique(101, reseau)
        case "3":
            modifier_etat(101,"actif", reseau)   
        case "4":
             afficher_peripheriques()
        case "5":
                afficher_peripheriques_actifs(reseau)
        case "6":
             print("vous avez quitter")
        case _:
             print("votre demande n'a pas ete prise en compte")