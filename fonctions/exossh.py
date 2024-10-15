import random

def seconnecter():

    essai=10
    condition=True
    while condition==True:
      co = random.randint(0,1)
      etat=["reussi", "echec"]
      
      if etat[co]==0:
         print("connexion reussie ")
         compteur=0
      else:
         print("connexion echoué")
         compteur=compteur+1

         if compteur==3:
            condition=False
            print("connexion bloque ")
               
         break

             
seconnecter()
