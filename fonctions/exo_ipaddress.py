#adresse="123 123 123 123"
#adress=adresse.replace(" ", ",")
#print(adresse)
#txt = "apple#banana#cherry#orange"

#x = txt.replace("#", ",") #la methode .replace pour remplacer 

#print(x)
   #tableau.append()//ajouter des choses dans un tableau 


#address=input(f'entrez une adresse ip entre chaque octet laissez un espace : ')
address="123.123.200.156"
address_correcte=address.split(".") # split fait deja un tableau 

if len(address_correcte)==4:
    for element in address_correcte:
        nombre=int(element) 
        if nombre<255 and nombre>0:
            invalide=0
            continue
        else:
            print ("l'adresse est incorrecte")
            invalide=1
            break
else :
            print("votre addresse est invalide")

if invalide == 0:
      print("IP bien")


