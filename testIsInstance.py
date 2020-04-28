import plantes

class Toto:
    def __init__(self):
        pass


courgette = plantes.creerPlante("courgette")
tulipe = plantes.creerPlante("tulipe")
entier = 5
toto = Toto()
chaine = "je suis une chaine de caractères"
float = 5.5

print("-- Is a Legume ? --")
print("courgette", isinstance(courgette,plantes.Legume))
print("tulipe", isinstance(tulipe,plantes.Legume))
print("entier", isinstance(entier,plantes.Legume))
print("toto", isinstance(toto,plantes.Legume))
print("chaine", isinstance(chaine,plantes.Legume))
print("float", isinstance(float,plantes.Legume))
##
#courgette True
#tulipe True
#entier False
#toto False
#chaine False
#float False

print("-- Is a Fleur ? --")
print("courgette", isinstance(courgette,plantes.Fleur))
print("tulipe", isinstance(tulipe,plantes.Fleur))
##
#courgette False
#tulipe True