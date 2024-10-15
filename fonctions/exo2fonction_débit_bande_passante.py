import random

def gestion(seuil):
    tentatives=0
    for element in range(10):
        debit = random.uniform(20, 200)
        
        if debit > seuil:
            print(f"Itération {element + 1}. Débit réseau {debit:.2f} Mbp a dépassé le seuil {seuil}.")
            tentatives=tentatives+1
            if tentatives==3:
                 print("on coupe la conexion")
                 break
            
            else:
                continue
        else:
            print(f"Itération {element + 1}. Débit réseau {debit:.2f} Mbp est inférieur au seuil, donc c'est bon.")
    
        



seuil = float(input('Quel est le seuil (en Mbp) ? : '))
gestion(seuil)
