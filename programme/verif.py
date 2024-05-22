from time import time

def verif(string : str, borne_min : int = -1, borne_max : int = -1, egal : bool = True) -> str:
    '''
    fonction verif.
    paramètres : 
        string (str)
        borne_min (int), valeur par défaut : -1
        borne_max (int), valeur par défaut : -1
        egal : bool, valeur par défaut True
    avec : n (int), valeur de string convertie en int.
    vérifie que le string entré est convertible en int, 
    et qu'il se trouve dans l'intervalle [borne_min, borne_max] s'il est précisé et si egal est sur True.
    si egal est sur False, l'intervalle est ]borne_min, borne_max[
    renvoie l'erreur s'il yen a une, sinon renvoie un str 'pass'
    ne fonctionne que sur l'intervalle [0,+infini]
    '''
    n : int
    try:
        n = int(string)
        if borne_max != -1:
            if egal:
                if n > borne_max : 
                    return f'{bcolors.RED}n doit être compris entre {borne_min} et {borne_max} compris{bcolors.RESET}'
                if n < borne_min:
                    return f'{bcolors.RED}n doit être compris entre {borne_min} et {borne_max} compris{bcolors.RESET}'
                return 'pass'
            else:
                if n >= borne_max: 
                    return f'{bcolors.RED}n doit être compris entre {borne_min} et {borne_max} non compris{bcolors.RESET}'
                if n <= borne_min:
                    return f'{bcolors.RED}n doit être compris entre {borne_min} et {borne_max} non compris{bcolors.RESET}'
                return 'pass'
    except ValueError:
        return f'{bcolors.RED}n doit être un entier{bcolors.RESET}'
    
class bcolors:
    GREEN = "\033[92m"  # GREEN
    YELLOW = "\033[93m"  # YELLOW
    RED = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR
    HIDE = "\033[8m" #hide color

def get_time(epoch : float) -> float:
    """Renvoie le nombre temps passé depuis epoch en milisecondes

    Args:
        epoch (float): temps de départ

    Returns:
        float: temps passé depuis epoch en milisecondes
    """
    res : float = (time() - epoch) * 1000
    return res


