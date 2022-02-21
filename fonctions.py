nb_trace = 6  # pour la tache 2

largeur = 4
longueur = 4

# tache 1


def seg_adjacent(sommet, max_x, max_y):
    """
    Fonction prenant en paramètre un sommet représenté par un tuple
    et la longueur et la largeur de la grille sur laquelle on travaille.
    Elle renvoie la liste des segment adjacents à ce sommet.

    :param sommet: tuple
    :param max_x: int
    :param max_y: int
    :return value: liste

    >>> seg_adjacent((1,2), 4, 4)
    [((1, 1), (1, 2)), ((1, 2), (1, 3)), ((0, 2), (1, 2)), ((1, 2), (2, 2))]
    """
    lst = []
    x, y = sommet
    if (y - 1) >= 0:
        lst.append(((x, y-1), sommet))
    if (y + 1) < max_y:
        lst.append((sommet, (x, y+1)))
    if (x - 1) >= 0:
        lst.append(((x - 1, y), sommet))
    if (x + 1) < max_x:
        lst.append((sommet, (x + 1, y)))
    return lst


def est_trace(etat, segment):
    """
    Fonction prenant un dictionnaire etat et renvoie si le segment
    passé en argument est tracé ou pas.

    :param etat: dico
    :param segment: couple de sommets
    :return value: boolean

    >>> est_trace({((2, 3), (2, 4)) : 1, ((2, 4), (3, 4)) : -1}, ((2, 4), (3, 4)))
    False
    """
    if segment in etat:
        return etat[segment] == 1
    else:
        return False


def est_interdit(etat, segment):
    """
    Fonction prenant un dictionnaire etat et renvoie si le segment
    passé en argument est interdit ou pas.

    :param etat: dico
    :param segment: couple de sommets
    :return value: boolean

    >>> est_interdit({((2, 3), (2, 4)) : 1, ((2, 4), (3, 4)) : -1}, ((2, 4), (3, 4)))
    True
    """
    x = segment[0]   # la premiere coordonnée du tuple
    y = segment[1]   # la deuxieme
    for elem in etat:  # on parcoure les clés
        if x == elem[0] and y == elem[1]:  # si nos coordonnées correspondent bien au segment
            if etat[elem] == -1:  # et si la valeur de la clé est -1
                return True  # alors elle est interdit donc vrai
    return False


def est_vierge(etat, segment):
    """
    Fonction prenant un dictionnaire etat et renvoie si le segment
    passé en argument est dans le dictionnaire état.

    :param etat: dico
    :param segment: couple de sommets
    :return value: boolean

    >>> est_vierge({((2, 3), (2, 4)) : 1, ((2, 4), (3, 4)) : -1}, ((2, 4), (3, 4)))
    False
    """
    return segment not in etat  # ni trace ni interdit


def tracer_segment(etat, segment):
    """
    Fonction prenant en paramètre un segment et le rend tracé
    dans le dictionnaire état en le donnant la valeur 1.

    :param etat: dico
    :param segment: couple de sommets
    """
    etat[segment] = 1    # ajoute à état le segment tracé


def interdire_segment(etat, segment):
    """
    Fonction prenant en paramètre un segment et le rend interdit
    dans le dictionnaire état en le donnant la valeur -1.

    :param etat: dico
    :param segment: couple de sommets
    """
    etat[segment] = -1


def effacer_segment(etat, segment):
    """
    Fonction permettant de supprimer le segment passé en paramètre du
    dictionnaire état.

    :param etat: dico
    :param segment: couple de sommets
    :return value:
    """
    if segment in etat:
        del etat[segment]  # methode del permettant d'enlever la clé que l'on souhaite
    return None  # cas ou le segment n'est pas dans etat


def trop_proche(xa, ya, var):
    """
    Fonction qui permet de savoir si l'on clique sur une zone rectangulaire
    autour d'un segment.
    Si on est dedans, elle renvoie True sinon False.

    :param xa: float
    :param ya: float
    :param var: float
    :return value: boolean
    """
    par1 = xa - int(xa) < var and xa - int(xa) > -var
    par2 = ya - int(ya) < var and ya - int(ya) > -var
    if par1 and not(par2):
        return True
    elif not(par1) and par2:
        return True
    else:
        return False


def segments_traces(etat, sommet):
    """
    Fonction prenant en paramètre le dictionnaire état
    avec un sommet et nous renvoie la liste des segments
    tracés adjacents à sommet dans etat.

    :param etat: dico
    :param sommet: tuple
    :return value: liste
    """
    lst_segment = []
    i, j = sommet
    if est_trace(etat, ((i, j - 1), (i, j))):
        lst_segment.append(((i, j - 1), (i, j)))
    if est_trace(etat, ((i - 1, j), (i, j))):
        lst_segment.append(((i - 1, j), (i, j)))
    if est_trace(etat, ((i, j), (i, j + 1))):
        lst_segment.append(((i, j), (i, j + 1)))
    if est_trace(etat, ((i, j), (i + 1, j))):
        lst_segment.append(((i, j), (i + 1, j)))
    return lst_segment


def segments_interdits(etat, sommet):
    """
    Fonction prenant en paramètre le dictionnaire état
    avec un sommet et nous renvoie la liste des segments
    interdits adjacents à sommet dans etat.

    :param etat: dico
    :param sommet: tuple
    :return value: liste
    """
    lst_interdits = []
    lst_segments = seg_adjacent(sommet, largeur, longueur)
    for elem in lst_segments:
        if est_interdit(etat, elem):  # on verifie si tous les segments sont interdits
            lst_interdits.append(elem)  # alors on l'ajoute a la liste des segments adjacents
    return lst_interdits


def segments_vierges(etat, sommet):  # ni trace ni interdit !!!!
    """
    Fonction prenant en paramètre le dictionnaire état
    avec un sommet et nous renvoie la liste des segments
    vierges adjacents à sommet dans etat.

    :param etat: dico
    :param sommet: tuple
    :return value: liste
    """
    lst_vierges = []
    lst_segments = seg_adjacent(sommet, largeur, longueur)
    for elem in lst_segments:
        if est_vierge(etat, elem):  # on verifie si tous les segments sont vierges
            lst_vierges.append(elem)  # alors on l'ajoute a la liste des segments adjacents
    return lst_vierges


def statut_case(indices, etat, case):
    """
    Fonction prenant en paramètre la grille qui est représenté
    par les indices, le dictionnaire état et une case qui est
    représenté par un tuple et nous renvoie le statut
    de la case en renvoyant une valeur 0 si c'est satisfait,
    -1 si on a trop tracé de segments et 1 sinon.

    :param indices: liste de liste
    :param etat: dico
    :param case: tuple
    :return value: int
    """
    i, j = case
    if indices[i][j] is None:
        return 0
    seg_nord = ((j, i), (j+1, i))
    seg_sud = ((j, i + 1), (j+1, i + 1))
    seg_ouest = ((j, i), (j, i + 1))
    seg_est = ((j + 1, i), (j + 1, i + 1))
    case_segments = [seg_nord, seg_sud, seg_ouest, seg_est]
    indice = indices[i][j]  # la valeur de la case
    trace = 0  # compteur pour est tracer
    interdit = 0  # compteur pour est interdit
    for seg in case_segments:   # cette boucle nous permet de connaitre le nombre de segments traces
        if est_trace(etat, seg):
            trace += 1
        if est_interdit(etat, seg):
            interdit += 1
    if indice == trace:  # et donc ici on verifie si indice est satisfait, cad si l'indice correspond au nombre de segments tracés
        return 0
    if indice > trace and (4-interdit-trace >= indice - trace):  # nombre de segment restant superieur à nombre segment tracable
        return 1
    else:
        return -1  # trop tracer donc revenir en arriere



# tache 2


def cases_satisfait(indices, etat):
    """
    Fonction renvoyant True si une case est satisfaite False sinon.

    :param indices: liste de liste
    :param etat: dico
    :return value: boolean
    """
    for i in range(len(indices)):   # double boucle pour parcourir une liste de liste (i et j)
        for j in range(len(indices[0])):
            if statut_case(indices, etat, (i, j)) == 1 or statut_case(indices, etat, (i, j)) == -1:  # tuple i,j car c'est la case parcourue
                return False
    return True


def premier_indice(indices, etat):
    """
    Fonction qui vérifie que chaque case contenant
    un nombre k possède k cotés tracés.

    :param indices: liste de liste
    :param etat: dico
    :return value: boolean
    """
    for x in range(len(indices)):
        for y in range(len(indices)):
            if not(statut_case(indices, etat, (x, y)) == 0):
                return False
    return True


def deuxieme_indice(indices, etat):
    """
    Fonction qui vérifie si l'ensemble des segments tracés forment
    une boucle fermée en renvoyant True si c'est le cas, False sinon.

    :param indices: liste de liste
    :param etat: dico
    :return value: boolean
    """
    compt = 0
    long = None
    for x in etat:
        if etat[x] == 1:
            compt += 1
    for x in etat:
        if etat[x] == 1:
            if longueur_boucle(etat, x) == compt:
                return True
            break
    return False


def longueur_boucle(etat, segment):
    """
    Fonction qui vérifie si le segment appartient à une boucle,
    si le segment n'appartient pas à une boucle, la fonction
    renvoie None sinon elle renvoie la longueur de la boucle.

    :param etat: dico
    :param segment: couple de sommets
    :return value: int
    """
    precedent, courant = segment
    depart = precedent
    nb_seg = 1  # compteur des segments parcourus
    while courant != depart:
        lst_seg = segments_traces(etat, courant)
        if len(lst_seg) == 2:
            [(a, b), (c, d)] = lst_seg
            if a != courant and a != precedent:
                courant, precedent = a, courant
            elif b != courant and b != precedent:
                courant, precedent = b, courant
            elif c != courant and c != precedent:
                courant, precedent = c, courant
            elif d != courant and d != precedent:
                courant, precedent = d, courant
            nb_seg += 1
        else:
            return None
    return nb_seg





def affichage(indices, etat):
    """
    Fonction permettant d'afficher dans la console si on
    est arrivé à satisfaire les indices ou pas à chaque clic.

    :param indices: liste de liste
    :param etat: dico
    """
    print("_" * 10)
    print("premier indice : " + str(premier_indice(indices, etat)))
    print("deuxième indice : " + str(deuxieme_indice(indices, etat)))
    if premier_indice(indices, etat) and deuxieme_indice(indices, etat):
        print("Victoire")
    print("_" * 10)


def lire_fichier(fichier, indice):
    """
    Fonction qui crée la grille de jeu indices, pour cela elle lit
    un fichier et parcourt chaque ligne de ce dernier, si le caractère
    est un chiffre compris entre 0 et 3 ou est un tiret du bas
    alors on l'ajoute dans indice.

    :param : str
    :param indice: liste
    :return value: boolean

    >>> lire_fichier('grille1.txt', [])
    True
    """
    f = open(fichier, 'r')
    for ligne in f:
        lst_temp = []
        for lettre in ligne:
            print(lettre)
            if lettre == '_':
                lst_temp.append(None)
            elif lettre == '0' or lettre == '1' or lettre == '2' or lettre == '3':
                lst_temp.append(int(lettre))
            elif lettre == '\n':
                break
            else:
                f.close()
                return False
        indice.append(lst_temp)
    f.close()
    return True
