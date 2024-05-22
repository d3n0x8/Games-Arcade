from random import randint
from programme.verif import bcolors

#fonction pour les allumettes

def allumettes_bot():
    """fonction tour bot

    Returns:
        int: un chiffre entre 1 et 3 
    """
    return randint(1, 3)



#fonction pour les devinettes

def propose_bot():
    """fonction choix nombre début de partie

    Returns:
        int: un nombre entre 1 et 100
    """
    return str(randint(1, 100))

def devine_bot(min: int, max: int):
    """fonction trouve pour le bot

    Args:
        borne_min (int): entier minimale où le nombre à trouver se situe
        borne_max (int): entier maximale où le nombre à trouver se situe

    Returns:
        int: un entier entre les borne_min et borne_max
    """
    return randint(min, max)


#fonction pour le morpion

def morpion_bot(tab : list):
    """fonction morpion

    Returns:
        str: une chaine de caractère correspondant à un nombre entre 1 et 9.
    """
    l = []
    for ligne in tab:
        for case in ligne:
            if not (case == bcolors.GREEN+'O'+bcolors.RESET or case == bcolors.RED+'X'+bcolors.RESET):
                l.append(case)
    return l[randint(0, len(l)-1)]
