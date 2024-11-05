def est_segment_valide(segment):
    validation=0
    if 0<segment.isdigit()<255:
        # if 0<int(segment)<255:
        print ("c'est un entier entre 0 et 255")
        validation=validation+1
        if validation==4:
                return True
        else:
                return False
    else:
        print("entrez un nombre valide entre 0 et 255")

   