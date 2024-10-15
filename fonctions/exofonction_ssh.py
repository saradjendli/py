import random


def seconnecter():

    essai=10
    condition=0
    while condition<essai:
      compteur=0
      co = random.uniform(1, 10)
      if co==3:
         print("connexion reussi ")
         break
      else:
         print("connexion echoué")
         compteur=compteur+1
         condition>essai

            # if compteur==tentatives:
            #      print("connexion bloque ")
            #      essai=4



       
seconnecter()
