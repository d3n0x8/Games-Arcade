import os
from programme.verif import verif, bcolors, get_time
import programme.bot_debutant as bot_debutant
import programme.bot_expert as bot_expert
from time import time

def order(n1 : int, n2 : int) -> str:
	'''
	fonction order
	entré: n1, n2 : int
	renvoie +, - ou = en fonction des affinité entre n1 et n2
	'''
	if n1 > n2:
		return '+'
	elif n1 < n2:
		return '-'
	else:
		return '='


def saisi_n(poseur) -> int:
	'''
	fonction saisi_n
	sortie: int
	permet de saisir le nombre à deviner et le renvoie en int
	'''
	string : str
	if poseur not in ['bot1D', 'bot1E', 'bot2D', 'bot2E']:
		string = input(bcolors.RESET + poseur + ', choisissez un nombre entre 1 et 100 : ' + bcolors.HIDE)
		while verif(string, 1, 100) != 'pass':
			print(bcolors.RESET +''+ verif(string, 1, 100))
			string = input(bcolors.RESET + poseur + ', choisissez un nombre entre 1 et 100 : ' + bcolors.HIDE)
	elif poseur[-1] == 'D':
		string = bot_debutant.propose_bot()
	elif poseur[-1] == 'E':
		string = bot_expert.propose_bot()
	return int(string)


def manche(poseur : str, devineur : str) -> int:
	"""Fonction qui lance une manche de devinettes

	Args:
		poseur (str): Nom du poseur (qui choisit un nombre)
		devineur (str): Nom du devineur (qui essaye de deviner ce nombre)

	Returns:
		int: Nombre de coups pris par le devineur pour trouver le nom.
	"""
	borne_min : int = 1
	borne_max : int = 100

	essai_str : str
	essai : int
	n_coups : int = 0
	n : int
 
	indice = ''
	
	n = saisi_n(poseur)

	while indice != '=':
		if devineur in ['bot1D', 'bot1E', 'bot2D', 'bot2E']:
			input(f'{bcolors.RESET}{devineur} joue...')
			if devineur[-1] == 'D':
				essai_str = bot_debutant.devine_bot(borne_min, borne_max)
			elif devineur[-1] == 'E':
				essai_str = bot_expert.devine_bot(borne_min, borne_max)
		else:
			essai_str = input(bcolors.RESET + devineur + ', devinez un nombre entre 1 et 100 : ')
			while verif(essai_str, borne_min, borne_max) != 'pass':
				print(bcolors.RED + verif(essai_str, borne_min, borne_max) + bcolors.RESET)
				essai_str = input(devineur + ', devinez un nombre entre 1 et 100 : ')
		essai = int(essai_str)
		print('\n')
		n_coups += 1

		print(f'nombre = {essai} ')
		if poseur in ['bot1D', 'bot1E', 'bot2D', 'bot2E']:
			indice = order(n, essai)
		else:
			indice = input(poseur + ', Est-ce +, -, ou = ? ')
			while not (indice in ['+', '-', '='] and order(n, essai) == indice):
				if indice in ['+', '-', '=']:
					print(bcolors.RED + "C'est faux" + bcolors.RESET)
				else:
					print('commande inexistante')
				indice = input(poseur + ', Est-ce +, -, ou = ? ')
		print('\n')
		if indice == '+':
			borne_min = essai + 1
			print("C'est plus.")
		elif indice == '-':
			borne_max = essai - 1
			print("C'est moins.")
		else:
			input(f'{bcolors.GREEN}Bravo, vous avez trouvé en {n_coups} coups !{bcolors.HIDE}')
			
	return n_coups


def jouer(j1 : str, j2 : str) -> tuple[int]:
	'''
	boucle principale du mini-jeu
	entré: nom des deux joueurs
	renvoie le nombre de coups
	'''
	pts_j1 : int
	pts_j2 : int
	
	input(f'{bcolors.RESET}{j1} commence à faire deviner !{bcolors.HIDE}')
	pts_j1 = manche(j1, j2)
	os.system('clear || cls')
	input(f'{bcolors.RESET}à {j2} de faire deviner !{bcolors.HIDE}')
	pts_j2 = manche(j2, j1)

	os.system('clear || cls')
	input(f'{bcolors.RESET}{j1} à gagné {pts_j1}pts | {j2} à gagné {pts_j2}pts'+ bcolors.HIDE)

	return (pts_j1, pts_j2)


def quick_play(j1 : str, j2 : str) -> tuple:
	"""Fonction alternative de la fonction jouer utiliser pour comparer les bots dans le fichier get_stat.py

    Args:
        j1 (str): nom du bot 1
        j2 (str): nom du bot 2

    Returns:
        tuple: (pts_j1, pts_j2, time_j1, time_j2) avec time_j1 et time_j2 le temps de réponse moyen des bots.
    """
	pts_j1 : int
	pts_j2 : int
	time_j1 : float
	time_j2 : float
	
	pts_j1, time_j1 = quick_manche(j1, j2)
	pts_j2, time_j2 = quick_manche(j2, j1)

	return (pts_j1, pts_j2, time_j1, time_j2)





def quick_manche(poseur : str, devineur : str) -> tuple:
	"""Version alternative de la fonction manche qui n'affiche rien et renvoie d'autres informations

	Args:
		poseur (str): nom du poseur
		devineur (str): nom du devineur

	Returns:
		tuple: (nombre de coups, temps de réponse moyen)
	"""
	time_responses : list[float] = []
	epoch : float

	borne_min : int = 1
	borne_max : int = 100

	essai_str : str
	essai : int
	n_coups : int = 0
	n : int
 
	indice = ''
	
	n = saisi_n(poseur)

	while indice != '=':
		if devineur[-1] == 'D':
			epoch = time()
			essai_str = bot_debutant.devine_bot(borne_min, borne_max)
			time_responses.append(get_time(epoch))
		else:
			epoch = time()
			essai_str = bot_expert.devine_bot(borne_min, borne_max)
			time_responses.append(get_time(epoch))

		essai = int(essai_str)
		n_coups += 1

		indice = order(n, essai)
		if indice == '+':
			borne_min = essai + 1
		elif indice == '-':
			borne_max = essai - 1
			
	return (n_coups, sum(time_responses)/len(time_responses))