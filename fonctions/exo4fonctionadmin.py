def saisir():
    tentative=0
    mot_de_pass="1234"
    condition=True
    while condition==True:
          mot_utilisateur=input("quel est le mot de pass : ")
          if mot_utilisateur==mot_de_pass:
            print("vous etes connecté")
            tentative=0
            break
          else:
            tentative=tentative+1
            if tentative==3:

                print("votre compte est bloque")
                condition=False
                break 

            

saisir()

# Écrivez une fonction qui permet à un utilisateur d'essayer de se connecter à un système en saisissant un mot de passe. La fonction doit :
# 1. Prendre un mot de passe défini à l’avance (comme "admin123") et permettre à l'utilisateur d'entrer son mot de passe.
# 2. Limiter à 3 tentatives. Si l'utilisateur entre un mauvais mot de passe trois fois de suite, une alerte est affichée et l'accès est bloqué.
# 3. Si le mot de passe est correct avant d'atteindre la troisième tentative, afficher un message indiquant que l'accès est autorisé.