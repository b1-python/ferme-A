import plantes

money = 10
#tableau des instances des legumes
legumes = []
saison = 0

#boucle principal du jeu
while True:
    saison +=1
    print("Nous sommes au début de l'année ", saison)
    #boucle de la saison en cours
    while True:
        print("Vous avez ", money, "euros, acheter des semences ? (O: acheter des semences, Q finir la saison)")
        choix = input()
        #Condition pour verifier le choix de l'utilisateur
        if(choix=="O"):
            try :
                nomLegume = input("Nom de la semence : ")
                #création de l'instance avec le nom du legume depuis plantes
                nomLegume = plantes.creerPlante(nomLegume)
                #On soutrait le prix d'achat de la semence à l'argent total du joueur
                money -= nomLegume.getPrixAchat()
                #On ajoute l'instance dans un tableau
                legumes.append(nomLegume)
            except ValueError:
                print("ce legume n'existe pas !")
        elif(choix=="Q"):
            print("la saison ", saison, " est terminée, voici le résultat des ventes : ")
            #On boucle sur les instances des legumes
            for legume in legumes:
                #On c
                vente = int(legume.vendre())
                if(vente !=0 ):
                    print(legume.getNom(), " => " , vente)
                    money += vente
                else:
                    print("Vous n'avez pas vendu : ", legume.getNom())
            legumes = []
            break


    print("----------------------------------")