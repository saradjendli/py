from validation_de_segement import est_segment_valide
from validation_de_ladresse_ip import est_ip_valide


def saisir_ip():
     condition=True
     while condition==True:    
        ip=input("saisir une adresse ip valide : ")
        est_ip_valide(ip)
        resultat=est_segment_valide(ip)

        if resultat==False:
            print ("Adresse ip invalide")
        else:
            print("Adresse ip valide")
        condition=False

saisir_ip()