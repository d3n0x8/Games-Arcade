import os
from programme.verif import verif, bcolors, get_time
from random import shuffle
import programme.bot_debutant as bot_debutant
import programme.bot_expert as bot_expert
from time import time

def afficher_board(tab : list[list]):
	'''
	Procédure afficher_board
	entrée: tab : list[list]
	afficher la grille de jeu
	'''
	count_colonne = 0
	for ligne in tab:
		count_ligne = 0
		for case in ligne:
			print(case, end = '')
			if count_ligne < 2:
				print(' | ', end = '')
			count_ligne += 1
		if count_colonne < 2:
			print('\n---------')
		count_colonne += 1
	print('\n')

def find(case : str, tab : list[list]) -> tuple[int]:
	'''
	Fonction find
	entrée:
		case : str, tableau : list[list]
	sortie: tuple
	recherche l'élément case dans le tableau et renvoie son indice dans un tuple (i,j)
	si l'élément est absent de la liste, on renvoie (-1,-1)
	'''
	coord : tuple[int] = (-1,-1)
	for i in range(len(tab)):
		for j in range(len(tab[i])):
			if tab[i][j] == case:
				coord = (i,j)
	return coord

def saisi_case() -> str:
	'''
	fonction saisi_case
	sortie: str
	permet de saisir l'indice d'une case et la renvoie.
	'''
	string : str
	string = input('entrer une case (numéroté de comme un pavé tactile) : ')
	while verif(string, 1, 9) != 'pass':
		print(verif(string, 1, 9))
		string = input('entrer une case (numéroté de comme un pavé tactile) : ')
	return string

def change_tour(tour : str) -> str:
	'''
	fonction change_tour
	entrée: tour : str
	sortie: str
	change le tour en x ou o selon si c'est x ou o
	'''
	if tour == bcolors.GREEN+'O'+bcolors.RESET:
		return bcolors.RED+'X'+bcolors.RESET
	else:
		return bcolors.GREEN+'O'+bcolors.RESET
	
def alone_in_tab(element : str, tab : list[str]) -> bool:
	'''
	fonction alone_in_tab
	entré:
		element : str
		tab : list[str]
	sortie: booléen
	renvoir True si la liste n'est composé que de l'élément d'entré
	'''
	boolean : bool = True
	for e in tab:
		if e != element:
			boolean = False
	return boolean

def tab_complet(tab : list[list[str]]) -> bool:
	'''
	Fonction tab_complet
	Entré: list[list[str]] (grille de jeu)
	sortie: booléen
	renvoie True si le tableau à été rempli par les joueurs
	False sinon.
	'''
	booléen : bool = True

	for i in range(len(tab)):
		for j in range(len(tab[i])):
			if tab[i][j] in ['1','2','3','4','5','6','7','8','9']:
				booléen = False
	return booléen
	
def win(tab : list[list[str]]) -> str:
	'''
	fonction win
	entré: tab : list[list[str]] (grille de jeu)
	sortie : str
	avec la liste des positions gagnante sur le tableau.
	vérifie s'il y a un gagnant et renvoie soit le signe du gagnant s'il y en a un, "None" sinon.
	'''
	ligne1 : tab[str] = [tab[0][0],tab[0][1],tab[0][2]]
	ligne2 : tab[str] = [tab[1][0],tab[1][1],tab[1][2]]
	ligne3 : tab[str] = [tab[2][0],tab[2][1],tab[2][2]]

	colonne1 : tab[str] = [tab[0][0],tab[1][0],tab[2][0]]
	colonne2 : tab[str] = [tab[0][1],tab[1][1],tab[2][1]]
	colonne3 : tab[str] = [tab[0][2],tab[1][2],tab[2][2]]

	diag1 : tab[str] = [tab[0][0],tab[1][1],tab[2][2]]
	diag2 : tab[str] = [tab[2][0],tab[1][1],tab[0][2]]

	pos_win : tab[tab[str]] = [ligne1, ligne2, ligne3, colonne1, colonne2, colonne3, diag1, diag2]

	string : str = 'None'

	for pos in pos_win:
		if alone_in_tab(bcolors.GREEN+'O'+bcolors.RESET, pos):
			string = 'O'
		elif alone_in_tab(bcolors.RED+'X'+bcolors.RESET, pos):
			string = 'X'
	return string

def initialisation_tour(j1 : str, j2 : str) -> list[str]:
	'''
	Fonction initialisation_tour
	Entré: ji, j2 : str (nom des joueurs)
	sortie: tuple de str (l'ordre des joueurs)
	renvoie un tuple contenant le nom des joueurs dans un ordre aléatoire.
	'''
	ordre = [j1, j2]
	shuffle(ordre)
	return ordre

def jouer(j1 : str, j2 : str) -> str:
	'''
	fonction game
	entré: nom des 2 joueurs
	sortie: strfind
	Lance le mini jeu et renvoie le nom du gagnant.
	affiche le tableau de jeu, 
	fait saisir une case,
	change la case du tableau en fonction du joueur jouant,
	change le tour, 
	vérifie s'il y un gagnant ou si le tableau est complet.
	si oui: on retourne le nom du gagnant ou l'égalité sinon: on recommence.
	'''
	tour : str = bcolors.GREEN+'O'+bcolors.RESET
	tab : list[list[str]] = [
		['7','8','9'],
		['4','5','6'],
		['1','2','3']
	] 
	#grille de jeu

	joueurs : list[str] = initialisation_tour(j1,j2)
	joueuro : str = bcolors.GREEN+joueurs[0]+bcolors.RESET
	joueurx : str = bcolors.RED+joueurs[1]+bcolors.RESET
	print(f'{joueurs[0]} est O, {joueurs[1]} est X')

	case : str #numéro de la case séléctionné
	while win(tab) == 'None' and not tab_complet(tab):
		afficher_board(tab)
		if tour == bcolors.GREEN+'O'+bcolors.RESET:
			print('à : ' + joueuro)
			if joueurs[0] in ['bot1D', 'bot1E', 'bot2D', 'bot2E']:
				input(f'{joueuro} joue...')
				if joueurs[0][-1] == 'D':
					case = bot_debutant.morpion_bot(tab)
				else:
					case = bot_expert.morpion_bot(tab, tour)
			else:
				case = saisi_case()
		else:
			print('à : ', joueurx)
			if joueurs[1] in ['bot1D', 'bot1E', 'bot2D', 'bot2E']:
				input(f'{joueurx} joue...')
				if joueurs[1][-1] == 'D':
					case = bot_debutant.morpion_bot(tab)
				else:
					case = bot_expert.morpion_bot(tab, tour)
			else:
				case = saisi_case()
		index = find(case, tab)
		while index == (-1,-1):
			print(bcolors.RED+'Cette case est déjà prise.'+bcolors.RESET)
			case = saisi_case()
			index = find(case, tab)
		tab[index[0]][index[1]] = tour
		tour = change_tour(tour)
		os.system('clear')

	
	afficher_board(tab)

	if win(tab) == 'None':
		input('Egalité !')
		return 'Tie'
	else:
		if win(tab) == 'O':
			input(joueuro + ' à gagné !')
			return joueurs[0]
		else:
			input(joueurx + ' à gagné !')
			return joueurs[1]
		



def quick_play(j1 : str, j2 : str) -> tuple:
	"""Version alternative de la fonction jouer() utilisé par le fichier get_stat()

	Args:
		j1 (str): Nom du joueur 1
		j2 (str): Nom du joueur 2

	Returns:
		tuple: (pts_j1, pts_j2, time_j1, time_j2) avec time_j1 et time_j2 le temps de réponse moyen des bots.
	"""
	time_o : float
	time_x : float

	time_j1 : float
	time_j2 : float

	time_responses : tuple[list[float]] = ([], [])
	epoch : float

	pts_j1 : int
	pts_j2 : int

	tour : str = bcolors.GREEN+'O'+bcolors.RESET
	tab : list[list[str]] = [
		['7','8','9'],
		['4','5','6'],
		['1','2','3']
	] 
	#grille de jeu

	joueurs : list[str] = initialisation_tour(j1,j2)

	case : str #numéro de la case séléctionné
	while win(tab) == 'None' and not tab_complet(tab):
		if tour == bcolors.GREEN+'O'+bcolors.RESET:
			if joueurs[0][-1] == 'D':
				epoch = time()
				case = bot_debutant.morpion_bot(tab)
				time_responses[0].append(get_time(epoch))
			else:
				epoch = time()
				case = bot_expert.morpion_bot(tab, tour)
				time_responses[0].append(get_time(epoch))
		else:
			if joueurs[1][-1] == 'D':
				epoch = time()
				case = bot_debutant.morpion_bot(tab)
				time_responses[1].append(get_time(epoch))
			else:
				epoch = time()
				case = bot_expert.morpion_bot(tab, tour)
				time_responses[1].append(get_time(epoch))
		index = find(case, tab)

		tab[index[0]][index[1]] = tour
		tour = change_tour(tour)
		
	time_o = sum(time_responses[0])/len(time_responses[0])
	time_x = sum(time_responses[1])/len(time_responses[1])

	if joueurs[0] == j1:
		time_j1, time_j2 = time_o, time_x
	else:
		time_j1, time_j2 = time_x, time_o

	if win(tab) == 'None':
		pts_j1, pts_j2 = 0, 0
	else:
		if win(tab) == 'O':
			if joueurs[0] == j1:
				pts_j1, pts_j2 = 1, 0
			else:
				pts_j1, pts_j2 = 0, 1
		else:
			if joueurs[1] == j1:
				pts_j1, pts_j2 = 1, 0
			else:
				pts_j1, pts_j2 = 0, 1

	return (pts_j1, pts_j2, time_j1, time_j2)
