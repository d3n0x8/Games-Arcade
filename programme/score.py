import pickle
from typing import BinaryIO

class Profil:
    nom : str
    total : int
    devinettes : int
    allumettes : int
    morpion : int

class CurrentProfil():
    j1 : Profil
    j2 : Profil

def update_total(c_profil : CurrentProfil):
    '''
    Procédure update_total
    met à jour les totaux des points de la structure CurrentProfil donné en paramètre
    '''
    c_profil.j1.total = c_profil.j1.devinettes + c_profil.j1.allumettes + c_profil.j1.morpion
    c_profil.j2.total = c_profil.j2.devinettes + c_profil.j2.allumettes + c_profil.j2.morpion


def profil_exist(nom : str, all_profil : list[Profil]) -> bool:
    '''
    Fonction profil_exist
    Entrée: 
        nom : str
        all_profil : list[Profil]
    Sortie: bool
    Recherche un profile de nom donné dans la liste de Profil. Retourne True s'il y est présent, False sinon.
    '''
    existe : bool = False
    id_profile : int = 0
    if not len(all_profil) == 0:
        while id_profile < len(all_profil) and not existe:
            if all_profil[id_profile].nom == nom:
                existe = True
            id_profile += 1
    return existe

def search_profil(nom : str, all_profil : list[Profil]) -> Profil:
    '''
    Fonction search_profil
    Entrée: 
        nom : str
        all_profil : list[Profil]
    Sortie:
        Profil
    Recherche un profile de nom donné dans une liste de Profil. S'il en trouve un, il le revoie.
    S'il ne trouve rien, il renvoie un profile vierge.
    '''
    res : Profil = Profil()
    res.nom = ''
    id_profile : int = 0
    if not len(all_profil) == 0:
        while id_profile < len(all_profil) and res.nom == '':
            if all_profil[id_profile].nom == nom:
                res = all_profil[id_profile]
            id_profile += 1
    if res.nom == '':
        res = create_profil(nom)
    return res

def create_profil(nom : str) -> Profil:
    '''
    Fonction create_profil
    Entrée: nom : str
    Sortie: Profil
    Créer une instance de Profil de nom donné et de 0 pour le reste de ses attributs puis le renvoie
    '''
    profil : Profil = Profil()

    profil.nom = nom
    profil.total = 0
    profil.devinettes = 0
    profil.allumettes = 0  
    profil.morpion = 0

    return profil

def save(all_profil : list[Profil]):
    '''
    Procédure save
    entrée: all_profil : list[Profil] (liste des profils)
    sauvegarde les profils dans save.txt
    '''
    fichier : BinaryIO = open('programme/save.txt', 'wb')
    pickle.dump(all_profil, fichier)
    fichier.close

def load() -> list[Profil]:
    '''
    Fonction load
    sortie: list[Profil] (liste des profils)
    renvoie la liste des profils sauvegardé dans save.txt
    '''
    f : BinaryIO 
    liste_profil : list[Profil]
    try:
        with open('programme/save.txt', 'rb') as f:
            liste_profil = pickle.load(f)
    except FileNotFoundError:
        liste_profil = []
    return liste_profil



