import os
from programme.score import *
from programme.verif import bcolors, verif
from programme import allumettes
from programme import devinettes
from programme import morpion


def menu_principal() -> str:
    """Fonction menu_principal
    Affiche les options du menu principal
    puis renvoie le choix du joueur

    Returns:
        str: choix du joueur
    """
    choix : str

    print(bcolors.RESET)
    print('\n ~Menu Principal~ \n')
    print('[D] devinettes')
    print('[A] allumettes')
    print('[M] morpion')
    print('[S] scores')
    print('[E] exit')

    choix = input("Que voulez vous faire ? ").upper()

    return choix

def menu_score() -> str:
    '''
    fonction menu score
    parametre: aucun
    avec: 
        choix: int
    retourne le choix de l'utilisateur
    '''
    choix: int
    print(bcolors.RESET)
    print("[T] Score Total")
    print("[D] Score Devinettes")
    print("[A] Score Allumettes")
    print("[M] Score Morpion")
    print("[X] Réinitialiser les scores")
    print("[R] Retour")
    choix = input("Saisissez votre choix : ").upper()
    return choix

def entrer_nom() -> str:
    """Fonction entrer_nom
    Permet d'entrer le nom d'un joueur

    Returns:
        str: nom du joueur entré
    """
    joueur : str = input("Entrez un nom: ")
    while joueur in ['bot1D', 'bot1E', 'bot2D', "bot2E", '', ' ']:
        if joueur == '' or joueur == ' ':
            print(f'{bcolors.RED}Votre nom ne peux pas être vide !{bcolors.RESET}')
        else:
            print(f'{bcolors.RED}Ce nom est indisponible.{bcolors.RESET}')
        joueur = input("Entrez un nom: ")
    return joueur

def separator(wait : bool = False):
    """Procédure separateur
    Permet d'afficher un séparateur sur le terminal. 
    Si wait est sur true, la fonction mettra le programme sur pause 
    jusqu'à ce que la touche entré soit pressé.

    Args:
        wait (bool, optional): booléen permettant de faire attendre le programme si sur True  False par défaut.
    """
    print('\n')
    print('-----------------------------------')
    if wait:
        input('\n'+ bcolors.HIDE)
    else:
        print('\n')
        
def select_difficulty(pos : str) -> str:
    """Fonction, permet de choisir la difficulté d'un bot en position donnée.

    Args:
        pos (str): position du bot (joueur 1 ou joueur 2)

    Returns:
        str: nom du bot
    """
    difficulty = input('D : débutant | E : expert  --->  ').upper()
    while difficulty != 'D' and difficulty != 'E':
        if difficulty != 'D' and difficulty != 'E':
            print(bcolors.RED + 'Erreur, commande innexistante' + bcolors.RESET)
        difficulty = input('D : débutant | E : expert   --->  ').upper()
    return "bot" + pos + difficulty

if __name__ == '__main__':
    c_profil : CurrentProfil = CurrentProfil()
    all_profil : list[Profil] = load()
    
    joueur1 : str
    joueur2 : str

    choix : str = ''

    n : int

    os.system('clear  || cls')

    print(bcolors.RESET + ' Bienvenue ! ')

    str_n_joueuer = input('Veuillez entrer le nombre de joueur(s) réel(s): ')
    while verif(str_n_joueuer, 0, 2) != 'pass':
        print(verif(str_n_joueuer, 0, 2))
        str_n_joueuer = input('Veuillez entrer le nombre de joueur(s) réel(s): ')
    n = int(str_n_joueuer)

    #Entré des joueurs
    if n != 0:
        print("Joueur 1")
        joueur1 = entrer_nom()
        
    else:
        print('Selectionnez la difficulté du bot joueur 1')
        joueur1 = select_difficulty('1')
    c_profil.j1 = search_profil(joueur1, all_profil)
    if not profil_exist(joueur1, all_profil):
        all_profil.append(c_profil.j1)
    
    if n == 2:
        print('Joueur 2')
        joueur2 = entrer_nom()
    else:
        print('Veuillez entrer le niveau de difficulté du bot joeuur 2:')
        joueur2 = select_difficulty('2')
    c_profil.j2 = search_profil(joueur2, all_profil)
    if not profil_exist(joueur2, all_profil):
        all_profil.append(c_profil.j2)


    print('-----------------------------------')

    #boucle principale

    while choix!='E':
        os.system('clear || cls')

        choix = menu_principal()

        os.system('clear || cls')
        
        if choix=='D':
            print("~~ Devinettes ~~ \n  Un joueur choisit un nombre entre 1 et 100. \n L'autre doit deviner ce nombre: à chacune de ses propositions. \nLe premier joueur répond '+' si c'est trop petit, '-' si trop grand et '=' si c'est gagné")
            choix = input('[J] Jouer    [r] Retour  |  ').lower()
            if choix != 'r':
                os.system('clear  || cls')
                resultat_devinette = devinettes.jouer(joueur1, joueur2)
                c_profil.j1.devinettes += resultat_devinette[0]
                c_profil.j2.devinettes += resultat_devinette[1]


        elif choix=='A':
            print("~~ Allumettes ~~ \n  On dispose d'un tas de 20 allumettes. Chaque joueur à tour de rôles peut en prélever 1, 2 ou 3. le perdant est celui qui prend la dernière allumette.")
            choix = input('[J] Jouer    [r] Retour  |  ').lower()
            if choix != 'r':
                os.system('clear  || cls')
                resultat_allumette = allumettes.jouer(joueur1, joueur2)
                if resultat_allumette == joueur1:
                    c_profil.j1.allumettes += 1
                else:
                    c_profil.j2.allumettes += 1


        elif choix=='M':
            print("~~ Morpion ~~ \n Chaque joueur pose sa marque (un O ou un X) à tour de rôle dans les cases d'une grille de 3x3. \n Le premier qui aligne 3 marques a gagné.")
            choix = input('[J] Jouer   [r] Retour  |  ').lower()
            if choix != 'r':
                os.system('clear  || cls')
                resultat_morpion = morpion.jouer(joueur1, joueur2)
                if resultat_morpion == joueur1:
                    c_profil.j1.morpion += 1
                elif resultat_morpion == joueur2:
                    c_profil.j2.morpion += 1
                else:
                    c_profil.j1.morpion += 1
                    c_profil.j2.morpion += 1


        elif choix=='S':
            update_total(c_profil)
            varbool_menu = True            
            while choix != 'R':
                os.system('clear  || cls')
                choix = menu_score()
                os.system('clear  || cls')
                if choix == 'T':
                    separator()
                    print('~~SCORE TOTAL~~\n')
                    print(f'score {joueur1}: ', c_profil.j1.total, f'| score {joueur2}: ', c_profil.j2.total)
                    separator(True)
                elif choix == 'D':
                    separator()
                    print('~~SCORE DEVINETTES~~\n')
                    print(f'score {joueur1}: ', c_profil.j1.devinettes, f'| score {joueur2}: ', c_profil.j2.devinettes)
                    separator(True)
                elif choix == 'A':
                    separator()
                    print('~~SCORE ALUMETTES~~\n')
                    print(f'score {joueur1}: ', c_profil.j1.allumettes, f'| score {joueur2}: ', c_profil.j2.allumettes)
                    separator(True)
                elif choix == 'M':
                    separator()
                    print('~~SCORE MORPION~~\n')
                    print(f'score {joueur1}: ', c_profil.j1.morpion, f'| score {joueur2}: ', c_profil.j2.morpion)
                    separator(True)
                elif choix == 'X':
                    try:
                        all_profil = []
                        c_profil.j1 = create_profil(joueur1)
                        c_profil.j2 = create_profil(joueur2)
                        update_total(c_profil)
                        os.remove('save.txt')
                        print("\n")
                        print('Score réinitialisé !')
                        input('\n'+ bcolors.HIDE)
                    except:
                        print("\n")
                        print('Score réinitialisé !')
                        input('\n'+ bcolors.HIDE)
                elif choix == 'R':
                    print('retour')
                else:
                    input('commande inexistante'+ bcolors.HIDE)
            separator()
            
        elif choix=='E':
            print("Au revoir !")
            update_total(c_profil)
            save(all_profil)

        else:
            input(f'\n {bcolors.RED}Commande inexistante !{bcolors.RESET}')











































































#https://www.kebab-frites.com/