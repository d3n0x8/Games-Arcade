from random import randint
from programme.verif import bcolors

#devinettes
def propose_bot() -> int:
    return str(randint(1,100))

def devine_bot(borne_min : int, borne_max : int) -> int:
    return (borne_min + borne_max) // 2

#allumettes
def allumettes_bot(n_allumettes : int) -> int:
    if n_allumettes % 4 == 0:
        return 3
    if n_allumettes % 4 == 1:
        return 2
    if n_allumettes % 4 == 2:
        return 1
    if n_allumettes % 4 == 3:
        return 2
    
#morpion

def play_random(tab : [list[str]]):
    l = []
    for ligne in tab:
        for case in ligne:
            if not (case == bcolors.GREEN+'O'+bcolors.RESET or case == bcolors.RED+'X'+bcolors.RESET):
                l.append(case)
    return l[randint(0, len(l)-1)]

def board_vide(board : list[list[str]]):
    boolean : bool = True
    for ligne in board:
        for case in ligne:
            if case == bcolors.GREEN+'O'+bcolors.RESET or case == bcolors.RED+'X'+bcolors.RESET:
                boolean = False
    return boolean

def get_voide(tab : list[str], sign):
    if sign == bcolors.GREEN+'O'+bcolors.RESET:
        nosign = bcolors.RED+'X'+bcolors.RESET
    else:
        nosign = bcolors.GREEN+'O'+bcolors.RESET
        
    n_s = 0
    for item in tab:
        if item == sign:
            n_s += 1
            
    n_ns = 0
    for item in tab:
        if item == nosign:
            n_ns += 1
            
    empty_case = 'none'
    if n_s == 2 and n_ns == 0:
        for case in tab:
            if case != sign and case != nosign:
                empty_case = case
    return empty_case

def having_win_pos(tab : list[list[str]], sign : str):
    ligne1 : tab[str] = [tab[0][0],tab[0][1],tab[0][2]]
    ligne2 : tab[str] = [tab[1][0],tab[1][1],tab[1][2]]
    ligne3 : tab[str] = [tab[2][0],tab[2][1],tab[2][2]]

    colonne1 : tab[str] = [tab[0][0],tab[1][0],tab[2][0]]
    colonne2 : tab[str] = [tab[0][1],tab[1][1],tab[2][1]]
    colonne3 : tab[str] = [tab[0][2],tab[1][2],tab[2][2]]

    diag1 : tab[str] = [tab[0][0],tab[1][1],tab[2][2]]
    diag2 : tab[str] = [tab[2][0],tab[1][1],tab[0][2]]

    pos_win : tab[tab[str]] = [ligne1, ligne2, ligne3, colonne1, colonne2, colonne3, diag1, diag2]
    
    all_win_case = []
    
    for pos in pos_win:
        if get_voide(pos, sign) != 'none':
            all_win_case.append(get_voide(pos, sign))
    
    return all_win_case
            

def morpion_bot(board : list[list[str]], bot_sign : str) -> str:
    if bot_sign == bcolors.GREEN+'O'+bcolors.RESET:
        p_sign = bcolors.RED+'X'+bcolors.RESET
    else:
        p_sign = bcolors.GREEN+'O'+bcolors.RESET
        
    if board_vide(board):
        return ['1', '3', '7', '9'][randint(0,3)]
    else:
        if having_win_pos(board, bot_sign) != []:
            return having_win_pos(board, bot_sign)[0]
        elif having_win_pos(board, p_sign) != []:
            return having_win_pos(board, p_sign)[0]
        else:
            return play_random(board)
        
