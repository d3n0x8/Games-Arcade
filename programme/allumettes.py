from programme.verif import verif, bcolors, get_time
from random import randint
import os
import programme.bot_debutant as bot_debutant
import programme.bot_expert as bot_expert
from time import time

def debut_partie() -> list:
    '''
	fonction debut de partie
	paramètres : 
		aucun
	avec : nb_allumette (list), liste de toutes les allumettes allumettes
	initialise la liste des allumettes
	'''
    nb_allumette: list
    nb_allumette = ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I']    
    return nb_allumette

def afficher_allumette(nb_allumette: list):
    '''
	fonction affichage allumette
	paramètres : 
		nb_allumette (list)
	avec : resultat (str), liste des éléments de nb_allumette sans les guillemets
	affiche toute la liste nb_allumette initialisée en chaine de caractère
	'''
    resultat: str
    resultat = ' '.join(nb_allumette)
    print("")
    print(resultat)

def tour(joueurs: str, nb_allumette: list) -> list:
    '''
	fonction tour de jeu
	paramètres : 
		joueurs (str), nom des joueurs
        nb_allumette (list), liste des allumettes restantes
	avec : allumette_enleve (int)
           compteur (int)
    demande au joueur combien il veut enlever d'allumettes
    puis retire le nombre saisis à la liste nb_allumette
    et enfin affiche la liste des allumettes restantes
	'''
    allumette_enleve: str
    compteur: int
    if joueurs in ['bot1D', 'bot1E', 'bot2D', "bot2E"]:
        input(f"{joueurs} joue...")
        if joueurs[-1] == 'D':
            allumette_enleve = str(bot_debutant.allumettes_bot())
        else:
            allumette_enleve = str(bot_expert.allumettes_bot(len(nb_allumette)))
    else:
        print(joueurs, "combien veux-tu en enlever ?")
        allumette_enleve = input()
        while verif(allumette_enleve, 1, 3) != 'pass':
                print(verif(allumette_enleve, 1, 3))
                print(joueurs, "combien veux-tu en enlever ?")
                allumette_enleve = input()
    
    for compteur in range(int(allumette_enleve)):
        if 'I' in nb_allumette:
            nb_allumette.remove('I')
    return nb_allumette

def jouer(j1, j2) -> str:
    '''if joueur1[-1] == 'D':
                        nb_allumette = tour_bot()
	paramètres : 
        aucun
	avec : nb_allumette (list)
           j1, j2 (str)
           c (int)
    récupère la liste entières d'allumettes,
    récupère le noms des 2 joueurs, 
    dis si lors du tour c'est au j1 ou j2 de jouer et 
    retourne le gagnant en str
	'''
    choix_joueur = randint(0 ,1)
    if choix_joueur == 1:
        joueur1 = j2
        joueur2 = j1
    else:
        joueur1 = j1
        joueur2 = j2

    nb_allumette = debut_partie()
    afficher_allumette(nb_allumette)
    c = 1
    
    while len(nb_allumette) > 1:
            if c % 2 == 1:
                nb_allumette = tour(joueur1, nb_allumette)
            else:
                nb_allumette = tour(joueur2, nb_allumette)
            os.system('clear || cls')
            print("\nIl reste",bcolors.RED, len(nb_allumette),bcolors.RESET, "allumettes !")
            afficher_allumette(nb_allumette)
            c += 1
    os.system('clear || cls')
    if len(nb_allumette) == 0:
        if c % 2 == 1:
            input(bcolors.YELLOW + joueur1 + ' a gagné !' + bcolors.HIDE)
            return joueur1
        else:
            input(bcolors.YELLOW + joueur2+ ' a gagné !' + bcolors.HIDE)
            return joueur2
    else:
        if c % 2 == 1:
            input(bcolors.YELLOW + joueur2+ ' a gagné !' + bcolors.HIDE)
            return joueur2
        else:
            input(bcolors.YELLOW + joueur1+ ' a gagné !' + bcolors.HIDE)
            return joueur1
        



def quick_play(j1 : str, j2 : str) -> tuple:
    """Fonction alternative de la fonction jouer utiliser pour comparer les bots dans le fichier get_stat.py

    Args:
        j1 (str): nom du bot 1
        j2 (str): nom du bot 2

    Returns:
        tuple: (pts_j1, pts_j2, time_j1, time_j2) avec time_j1 et time_j2 le temps de réponse moyen des bots.
    """
    winner : str
    time_j1 : float
    time_j2 : float

    time_responses : tuple(list[float]) = ([], [])
    epoch : float

    choix_joueur : int = randint(0 ,1)

    if choix_joueur == 1:
        joueur1 = j2
        joueur2 = j1
    else:
        joueur1 = j1
        joueur2 = j2

    nb_allumette : list = debut_partie()
    c = 1
    
    while len(nb_allumette) > 1:
            if c % 2 == 1:
                if joueur1[-1] == 'D':
                    epoch = time()
                    allumette_enleve = str(bot_debutant.allumettes_bot())
                    time_responses[0].append(get_time(epoch))
                else:
                    epoch = time()
                    allumette_enleve = str(bot_expert.allumettes_bot(len(nb_allumette)))
                    time_responses[0].append(get_time(epoch))
            else:
                if joueur2[-1] == 'D':
                    epoch = time()
                    allumette_enleve = str(bot_debutant.allumettes_bot())
                    time_responses[1].append(get_time(epoch))
                else:
                    epoch = time()
                    allumette_enleve = str(bot_expert.allumettes_bot(len(nb_allumette)))
                    time_responses[1].append(get_time(epoch))
            for _ in range(int(allumette_enleve)):
                if 'I' in nb_allumette:
                    nb_allumette.remove('I')
            c += 1
    time_j1, time_j2 = sum(time_responses[0])/len(time_responses[0]), sum(time_responses[1])/len(time_responses[1])
    
    if len(nb_allumette) == 0:
        if c % 2 == 1:
            winner = joueur1
        else:
            winner = joueur2
    else:
        if c % 2 == 1:
            winner = joueur2
        else:
            winner = joueur1
    
    if winner == j1:
        return (1,0, time_j1,time_j2)
    else:
        return (0,1, time_j1,time_j2)