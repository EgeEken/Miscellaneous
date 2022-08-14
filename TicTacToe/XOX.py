def plateau_vide():
    '''Renvoie un plateu de jeu vide pour le tictactoe de taille 3x3'''
    return [[' ' for s in range(3)] for i in range(3)]
    #return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

empty = plateau_vide()

def videt(plat, i, j):
    '''Decide si la case de coordonnees (i, j) du plateau est vide ou pas'''
    return plat[int(abs(j-2))][i] == ' '

def jouex(plat,i,j):
    '''joue x sur (i, j)'''
    plat[int(abs(j-2))][i] = 'X'
    
def joueo(plat,i,j):
    '''joue o sur (i, j)'''
    plat[int(abs(j-2))][i] = 'O'

def dessine_plateau(plat):
    '''Renvoie une chaine de caractere correspondant a un affichage du plateau de tic-tac-toe'''
    #res = ''
    line = ''
    print('/−−−\\')
    for i in plat:
        for j in range(3):
            line = line + i[j]
        print('|' + line + '|')
        #res = res + line
        line = ''
    print('\−−−/')
    #return res
    if not pleint(plat):
        return 'Your turn'
    else:
        return 'It\'s a draw'

def gagnet(plat, s):
    '''Precondition: s == 'X' or s == 'O'
    Dit si s a gagne ou pas'''
    w = [s, s, s]
    return w in [plat[0], plat[1], plat[2],
                [plat[i][0] for i in range(3)], [plat[i][1] for i in range(3)], [plat[i][2] for i in range(3)],
                [plat[i][i] for i in range(3)], [plat[i][int(abs(i-2))] for i in range(3)]]

def pleint(plat):
    '''Dit si plat contient des boites plein'''
    for i in range(3):
        for j in range(3):
            if plat[i][j] == ' ':
                return False
    return True

def boites_pleint(plat):
    '''Retourne une liste des coordonnees de tous les boites pleins'''
    res = []
    for i in range(3):
        for j in range(3):
            if videt(plat, i, j):
                res.append((i, j))
    return res

def undo(plat,i,j):
    '''supprime sur (i, j)'''
    plat[int(abs(j-2))][i] = ' '

import random

def tourt(plat, i, j):
    '''Joue un tour de tictactoe sur plat avec l'ordinateur qui joue par hazard chaque fois'''
    if videt(plat, i, j):
        if gagnet(plat, 'O'):
            print('L\'ordinateur a deja gagne')
            return 'commence avec une plateau qui n\'est pas fini'
        jouex(plat, i, j)
        options = boites_pleint(plat)
        ordmove = options[int(random.random() * len(options))]
        x, y = ordmove
        if not pleint(plat) and not gagnet(plat, 'O') and not gagnet(plat, 'X'):
            print('L\'ordinateur joue en (' + str(x) + ', ' + str(y) + ').')
            joueo(plat, x, y)
            print(dessine_plateau(plat))
            if gagnet(plat, 'O'):
                print('L\'ordinateur gagne')
        else:
            print(dessine_plateau(plat))
            if gagnet(plat, 'X'):
                print('Tu gagnes')
            else:
                print('Le coup est une egalite')
    else:
        print('Cette case est occupée')

def xcount(plat):
    '''retourne le nombre de x sur plat'''
    res = 0
    for i in plat:
        for j in i:
            if j == 'X':
                res += 1
    return res

def ocount(plat):
    '''retourne le nombre de o sur plat'''
    res = 0
    for i in plat:
        for j in i:
            if j == 'O':
                res += 1
    return res

def quijoue(plat):
    '''dit si c'est le tour de x ou o'''
    if xcount(plat) == ocount(plat):
        return 'X'
    else:
        return 'O'

def gagnexo(plat):
    '''dit si quelqu'un a gagne ou pas'''
    return gagnet(plat, 'X') or gagnet(plat, 'O')

def checkcorners(plat):
    '''Retourne une liste qui contient les coins disponibles et strategiquement viables''' 
    corners = [(2,2), (0,2), (0,0), (2,0)]
    available = set()
    for corner in corners:
        xc, yc = corner
        if videt(plat, xc, yc):
            available.add(corner)
    e = [' ', ' ', ' ']
    if xcount(plat) > 1:
        if plat[0] == e:
            available.remove((2,2))
            available.remove((0,2))
            return list(available)
        elif plat[2] == e:
            available.remove((0,0))
            available.remove((2,0))
            return list(available)
        elif [plat[i][0] for i in range(3)] == e:
            available.remove((0,2))
            available.remove((0,0))
            return list(available)
        elif [plat[i][2] for i in range(3)] == e:
            available.remove((2,0))
            available.remove((2,2))
            return list(available)
    return list(available)

def AItourt(plat, i, j):
    '''Joue un tour de tictactoe contre un ordinateur imbattable'''
    if videt(plat, i, j) and not gagnexo(plat) and not pleint(plat):
        if gagnet(plat, 'O'):
            print('L\'ordinateur a deja gagne')
            return 'commence avec une plateau qui n\'est pas fini'
        a = 0
        jouex(plat, i, j)
        if gagnet(plat, 'X'):
            print(' ')
            dessine_plateau(plat)
            print(' ')
            return 'Tu gagnes'
        elif pleint(plat):
            print(' ')
            dessine_plateau(plat)
            print(' ')
            return 'Le coup est une egalite'
        options = boites_pleint(plat)
        for move in options:
            if a == 0:
                x, y = move
                joueo(plat, x, y)
                if gagnet(plat, 'O'):
                    print(dessine_plateau(plat))
                    return 'L\'ordinateur gagne'
                    a = 1
                else:
                    undo(plat, x, y)
        if a == 0:
            for move in options:
                x, y = move
                jouex(plat, x, y)
                if gagnet(plat, 'X') and a == 0:
                    undo(plat, x, y)
                    joueo(plat, x, y)
                    print(' ')
                    print(dessine_plateau(plat))
                    print(' ')
                    options2 = boites_pleint(plat)
                    if xcount(plat) > 2:
                        for move2 in options2:
                            x2, y2 = move2
                            jouex(plat, x2, y2)
                            if gagnet(plat, 'X'):
                                print('L\'ordinateur voit que vous allez gagner et vous félicite')
                            undo(plat, x2, y2)
                    print('The computer plays (' + str(x) + ', ' + str(y) + ').')
                    a = 2
                else:
                    undo(plat, x, y)
        if a == 0:
            if videt(plat, 1,1):
                joueo(plat, 1,1)
                print('The computer plays (1,1).')
            elif len(checkcorners(plat)) > 0:
                availablecorners = checkcorners(plat)
                cornermove = availablecorners[int(random.random() * len(availablecorners))]
                xc, yc = cornermove 
                joueo(plat, xc,yc)
                print('The computer plays (' + str(xc) + ', ' + str(yc) + ').')
            else:
                ordmove = options[int(random.random() * len(options))]
                x, y = ordmove
                joueo(plat, x, y)
                print('The computer plays (' + str(x) + ', ' + str(y) + ').')
            print(' ')
            dessine_plateau(plat)
            print(' ')
    elif pleint(plat):
        return 'Ce jeu est deja termine'
    elif gagnexo(plat):
        return 'Quelqu\'un a deja gagne ce jeu'
    else:
        return 'Cette case est occupée'
    
def XOX():
    turn = 1
    plat = plateau_vide()
    print(' ')
    dessine_plateau(plat)
    print(' ')
    while not gagnexo(plat) and not pleint(plat):
        print('-------- Turn ' + str(turn) + ' -----------')
        print('Where will you play? (Type "resign" to end the game)')
        i = 3
        while i == 3:
            iin = input('x: ')
            if iin == '':
                print('What?')
            elif iin.isnumeric() and int(iin) in {0, 1, 2}:
                i = int(iin)
            elif iin == 'resign':
                print('You resigned')
                return 'Game over'
            else:
                print('That is not a valid x coord, please pick from 0 to 2')
        j = 3
        while j == 3:
            jin = input('y: ')
            if jin == '':
                print('What?')
            elif jin.isnumeric() and int(jin) in {0, 1, 2}:
                j = int(jin)
            else:
                print('That is not a valid y coord, please pick from 0 to 2')
        if videt(plat, i, j):
            AItourt(plat, i, j)
            turn += 1
        else:
            print('That box is occupied')
    if gagnet(plat, 'O'):
        return 'You lose.'

def startgame():
    print('Press enter to start game')
    a = input()
    print('--------------------------------------------------')
    print(' ')

def endgame():
    print('--------------------------------------------------')
    print(' ')
    print('Press enter to start new game')
    print('Type anything and press enter to exit')
    a = input()
    if a == '':
        print('--------------------------------------------------')
        print(' ')
        XOX()
    else:
        print('Bye')
        
startgame()
XOX()
endgame()
