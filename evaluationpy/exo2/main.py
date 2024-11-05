from compter_mots import compter_mots
from nettoyer_texte import nettoyer_texte
from detecter_mot_suspect import detecter_mot_suspects

def analyser_texte():
    texte=input("saisir le texte : ")
    nettoyer_texte(texte)
    compter_mots(texte)
    mot_suspect=input("saisir un mot a chercher : ")
    detecter_mot_suspects(texte, mot_suspect)

analyser_texte()
