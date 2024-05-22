from programme import allumettes
from programme import devinettes
from programme import morpion

from typing import TextIO

class BotProfil:
    nom : str
    total : int
    devinettes : int
    allumettes : int
    morpion : int

    time_devinettes : list[float]
    time_allumettes : list[float]
    time_morpion : list[float]

    mt_devinettes : float
    mt_allumettes : float
    mt_morpion : float

class CurrentBot():
    j1 : BotProfil
    j2 : BotProfil

def update_moyenne_time(profil : BotProfil):
    """Update les moyennes des temps de réponses pour chaques jeux

    Args:
        profil (BotProfil): profil dont il faut update les moyennes
    """
    profil.mt_allumettes = sum(profil.time_allumettes)/len(profil.time_allumettes)
    profil.mt_devinettes = sum(profil.time_devinettes)/len(profil.time_devinettes)
    profil.mt_morpion = sum(profil.time_morpion)/len(profil.time_morpion)

def update_total(c_profil : CurrentBot):
    '''
    Procédure update_total
    met à jour les totaux des points de la structure CurrentProfil donné en paramètre
    '''
    c_profil.j1.total = c_profil.j1.devinettes + c_profil.j1.allumettes + c_profil.j1.morpion
    c_profil.j2.total = c_profil.j2.devinettes + c_profil.j2.allumettes + c_profil.j2.morpion
    update_moyenne_time(c_profil.j1)
    update_moyenne_time(c_profil.j2)

def create_botprofil(nom : str) -> BotProfil:
    '''
    Fonction create_botprofil
    Entrée: nom : str
    Sortie: Profil
    Créer une instance de BotProfil en initialisant tous ces attributs.
    '''
    profil : BotProfil = BotProfil()

    profil.nom = nom
    profil.total = 0
    profil.devinettes = 0
    profil.allumettes = 0  
    profil.morpion = 0
    profil.time_allumettes = []
    profil.time_devinettes = []
    profil.time_morpion = []
    profil.mt_allumettes = 0.0
    profil.mt_devinettes = 0.0
    profil.mt_morpion = 0.0

    return profil

def make_play(n : int, choix : str):
    """Récupère les données des resultats de chaques jeux en faisant jouer 2 bots entre eux puis les mets dans un

    Args:
        n (int): Nombre de parties
        choix (str): définies quel difficulté de bots jourons. 
    """
    fic : TextIO

    resultat_allumette : str
    resultat_devinettes : tuple
    resultat_morpion : str

    profils : CurrentBot = CurrentBot()

    bot1D : BotProfil = create_botprofil("bot1D")
    bot1E : BotProfil = create_botprofil("bot1E")
    bot2D : BotProfil = create_botprofil("bot2D")
    bot2E : BotProfil = create_botprofil("bot2E")

    if choix == 'DvE':
        profils.j1 = bot1D
        profils.j2 = bot2E
    elif choix == 'DvD':
        profils.j1 = bot1D
        profils.j2 = bot2D
    elif choix == 'EVE':
        profils.j1 = bot1E
        profils.j2 = bot2E

    for _ in range(n):
        resultat_allumette = allumettes.quick_play(profils.j1.nom, profils.j2.nom)
        profils.j1.allumettes += resultat_allumette[0]
        profils.j2.allumettes += resultat_allumette[1]
        profils.j1.time_allumettes.append(resultat_allumette[2])
        profils.j2.time_allumettes.append(resultat_allumette[3])
        
        resultat_devinettes = devinettes.quick_play(profils.j1.nom, profils.j2.nom)
        profils.j1.devinettes += resultat_devinettes[0]
        profils.j2.devinettes += resultat_devinettes[1]
        profils.j1.time_devinettes.append(resultat_devinettes[2])
        profils.j2.time_devinettes.append(resultat_devinettes[3])

        resultat_morpion = morpion.quick_play(profils.j1.nom, profils.j2.nom)
        profils.j1.morpion += resultat_morpion[0]
        profils.j2.morpion += resultat_morpion[1]
        profils.j1.time_morpion.append(resultat_morpion[2])
        profils.j2.time_morpion.append(resultat_morpion[3])

        update_total(profils)

    if choix == 'DvE':
        fic = open('resultat_DvE.txt', 'w')
    elif choix == 'DvD':
        fic = open('resultat_DvD.txt', 'w')
    elif choix == 'EVE':
        fic = open('resultat_EvE.txt', 'w')
    
    fic.write(f'n = {n}\njoueur1 : {profils.j1.nom}\n   devinettes : {profils.j1.devinettes} | {profils.j1.mt_devinettes}ms\n   allumettes : {profils.j1.allumettes} | {profils.j1.mt_allumettes}ms\n   morpion : {profils.j1.morpion} | {profils.j1.mt_morpion}ms\njoueur2 : {profils.j2.nom}\n   devinettes : {profils.j2.devinettes} | {profils.j2.mt_devinettes}ms\n   allumettes : {profils.j2.allumettes} | {profils.j2.mt_allumettes}ms\n   morpion : {profils.j2.morpion} | {profils.j2.mt_morpion}ms\nTotaux :\n   {profils.j1.nom} : {profils.j1.total}\n   {profils.j2.nom} : {profils.j2.total}')
    fic.close()

if __name__ == '__main__':

    n : int = int(input('Entrez le nombre de parties : '))

    make_play(n, 'DvE')
    make_play(n, 'DvD')
    make_play(n, 'EVE')

    print('finished')