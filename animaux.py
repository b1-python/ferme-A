class Animal:
    """
    Classe ABSTRAITE Animal.
    Sert à représenter un Animal. On ne créera jamais d'instance de type Animal, mais
    on créera des instances des sous classes.
    Cette classe implémente la logique commune à tous les animaux, et déclare deux méthodes abstraites
    qui seront redéfinies pour chaque type d'animal => c'est du POLYMORPHISME.
    """
    def __init__(self, nom, prixAchat, crie):
        self.nom = nom
        self.age = 0
        self.prixAchat = prixAchat
        self.crie = crie

    def getNom(self):
        return self.nom

    def vieillir(self):
        """ Fait veillir l'animal d'un an """
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

    def toString(self):
        """ Renvoie une chaine de caractère qui représente l'animal """
        return self.nom + "("+str(self.age)+")"


class Vache(Animal):
    """ Représente une Vache """

    def __init__(self):
        Animal.__init__(self,"vache", 100,"meuuuuh")

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
    """ Représente une Oie """

    def __init__(self):
        Animal.__init__(self, "oie", 15, "kwac")

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
    """ Représente une Poule """

    def __init__(self):
        Animal.__init__(self, "poule", 10, "cotcot")

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

