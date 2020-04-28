class Animal:

    def __init__(self, prixAchat, crie):
        self.age = 0
        self.prixAchat = prixAchat
        self.crie = crie

    def vieillir(self):
        self.age += 1

    def getAge(self):
        return self.age

    def getPrixAchat(self):
        return self.prixAchat

    def crier(self):
        return self.crie

    # Methodes abstraites
    def vendreProduit(self):
        pass

    def vendreAnimal(self):
        pass


class Vache(Animal):

    def __init__(self):
        Animal.__init__(self,100,"meuuuuh")

    # Redéfinition des deux méthodes abstraites de la classe Animal
    def vendreProduit(self):
        if self.age >= 3 and self.age <= 10:
            # La vache produit du lait
            return 10
        else:
            # La vache ne produit pas de lait
            return 0

    def vendreAnimal(self):
        if self.age >= 3 and self.age <= 10:
            # La vache produit du lait
            return 120
        else:
            # La vache ne produit pas de lait
            return 50


class Oie(Animal):

    def __init__(self):
        Animal.__init__(self,15, "kwac")

    # Redéfinition des deux méthodes abstraites de la classe Animal
    def vendreProduit(self):
        return 0

    def vendreAnimal(self):
        if self.age < 3:
            return 15
        elif self.age > 5:
            return 20
        else:
            return 50


class Poule(Animal):

    def __init__(self):
        Animal.__init__(self,10, "cotcot")

    # Redéfinition des deux méthodes abstraites de la classe Animal
    def vendreProduit(self):
        if self.age >= 2 and self.age <= 8:
            return 30
        else:
            return 0

    def vendreAnimal(self):
        if self.age < 3:
            return 5
        elif self.age > 8:
            return 0
        else:
            return 20


def creerAnimal(nom):
    """
    Renvoie un objet du type de l'animal passé en paramètre
    Déclenche une erreur ValueError si le nom ne correspond à aucun animal connu
    """
    if nom == "vache":
        return Vache()
    elif nom == "oie":
        return Oie()
    elif nom == "poule":
        return Poule()
    else:
        raise ValueError()


# Test des classes
vache = Vache()
oie = Oie()