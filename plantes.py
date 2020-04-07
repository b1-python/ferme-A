import random
class Legume:
    def __init__(self,nom,prixsemence,prixVente,proba):
        self.nomLegume = nom
        self.prixSemence = prixsemence
        self.prixDeVente = prixVente
        self.probabiliteMaturite = proba

    def getNom(self):
        return self.nomLegume

    def getPrixAchat(self):
        return self.prixSemence

    def vendre(self):
        nombre = random.randint(1,100)
        if nombre > self.probabiliteMaturite:
            return 0
        else:
            return self.prixDeVente

class Fleur(Legume):
    def __init__(self,nom,prixsemence,prixVente,proba,couleur):
        Legume.__init__(self,nom,prixsemence,prixVente,proba)
        self.couleur = couleur 

    def getCouleur(self):
        return self.couleur

def creerPlante(nom):
    """
    Créer le légume et renvoie le legume selon les valeurs du tableau (prix achat, vente, probabilité)

    :return Une instance de la classe Legume qui correspond à la plante demandée
    """
    if nom == "courgette" :
        return Legume(nom,0.5,2,75)
    elif nom == "tomate":
        return Legume(nom,0.4,3,50)
    elif nom == "patate":
        return Legume(nom,0.9,1.5,90)
    elif nom == "tulipe":
        return Fleur(nom,2,4,80,"rose")
    elif nom == "rose":
        return Fleur(nom, 3, 7, 50, "rouge")
    elif nom == "muguet":
        return Fleur(nom, 1, 2, 90, "blanc")
    else:
        raise ValueError()

courgette = creerPlante("courgette")
tomate = creerPlante("tomate")

patate = creerPlante("patate")

print("vente courgette : ", courgette.vendre())

print("vente tomate : ", tomate.vendre())

print("vente patate : ", patate.vendre())