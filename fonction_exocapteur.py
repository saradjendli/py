import random

def gestion(seuil):
    for element in range(3):
        debit = random.uniform(20, 40)
        
        if debit > seuil:
            print(f"Itération {element + 1}. Débit réseau {debit:.2f} Mbp a dépassé le seuil {seuil}.")
        else:
            print(f"Itération {element + 1}. Débit réseau {debit:.2f} Mbp est inférieur au seuil, donc c'est bon.")

seuil = float(input('Quel est le seuil (en Mbp) ? : '))
gestion(seuil)

