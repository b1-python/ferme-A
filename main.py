import plantes
import random

money = 10
#tableau des instances des legumes
legumes = []
saison = 0

couleursDesSaisons = ["rose", "rouge", "blanc", "jaune", "bleu", "vert", "violet", "orange"]

#boucle principal du jeu
while True:
    saison +=1
    couleurDeLaSaison = random.choice(couleursDesSaisons)
    print("Nous sommes au début de l'année ", saison)
    #boucle de la saison en cours
    while True:
        print("Vous avez ", money, "euros, acheter des semences ? (O: acheter des semences, Q finir la saison)")
        choix = input()
        #Condition pour verifier le choix de l'utilisateur
        if(choix=="O"):
            try :
                nomLegume = input("Nom de la semence : ")
                # création de l'instance avec le nom du legume depuis plantes
                legume = plantes.creerPlante(nomLegume)
                # On soutrait le prix d'achat de la semence à l'argent total du joueur
                money -= legume.getPrixAchat()
                # On ajoute l'instance dans un tableau
                legumes.append(legume)
            except ValueError:
                print("ce legume n'existe pas !")
        elif(choix=="Q"):
            print("la saison ", saison, " est terminée, voici le résultat des ventes : ")
            #On boucle sur les instances des legumes
            for legume in legumes:
                # On calcule le prix du vente du légume
                vente = int(legume.vendre())
                if(vente !=0 ):

                    # Vérification de la couleur de la fleur le cas échéant
                    if isinstance(legume, plantes.Fleur):
                        # La plante est une fleur => on vérifie sa couleur pour doubler éventuellement son prix de vente
                        fleur = legume # On sait ici que légume est une fleur (inutile, mais changer le nom de la variable clarifie les choses
                        if couleurDeLaSaison == fleur.getCouleur():
                            vente *= 2
                            print("Wouhou, la " + fleur.getNom()  + " est à la mode cette saison !")

                    print(legume.getNom(), " => " , vente)
                    money += vente
                else:
                    print("Vous n'avez pas vendu : ", legume.getNom())
            legumes = []
            break


    print("----------------------------------")