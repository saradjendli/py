from validation_de_segement import est_segment_valide


def est_ip_valide(ip):
     adresse=ip.split(".")
     if len(adresse)==4:
        print("le segment est correcte")
        for element in adresse:
            int(element)
            est_segment_valide(element)
     else:
        print("Erreur: il n'y a pas 4 segments dans l'addresse ip")
      














