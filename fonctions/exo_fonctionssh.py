import random

compteur = 0
for i in range (10):
    hazar = random.randint(0,1)
    etat = ["echec", "succes"]
    if etat[hazar] == "echec":
        print(f"Tentative {i}: Connexion échouée")
        compteur += 1
    else:
        print(f"Tentative {i}: Connexion réussie")
        compteur = 0
    if compteur ==3:
        print("Fin")
        break


    # print(f"{i}: {etat[hazar]}")