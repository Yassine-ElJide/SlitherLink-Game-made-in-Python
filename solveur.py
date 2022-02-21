from fonctions import *
from test import *
from graphique import *


def solveur(indices, etat, sommet):
    """
    Fonction récursive responsable de résoudre la grille du jeu
    et prend en paramètre les tableau indices représentant
    la grille et le dictionnaire état et un sommet.

    :param indices: liste de liste
    :param etat: dico
    :param sommet: tuple
    :return value: boolean
    """
    nb_adjacent = segments_traces(etat, sommet)
    if len(nb_adjacent) == 2:  # cas de base
        if cases_satisfait(indices, etat):
            print_etat(etat)
            return True
        return False
    if len(nb_adjacent) > 2:  # cas de base
        return False
    nb_vierge = segments_vierges(etat, sommet)
    for pos in range(len(nb_vierge)):  # tester tous les segments dans nb_vierge
        i, j = nb_vierge[pos]
        if i == sommet:
            extremite = j
        else:
            extremite = i
        if extremite[0] <= len(indices) and extremite[1] <= len(indices):
            if extremite > sommet:   # compare le plus grand des sommets
                tracer_segment(etat, (sommet, extremite))
            else:
                tracer_segment(etat, (extremite, sommet))
            if solveur(indices, etat, extremite):  # cas récursif
                return True
            if extremite > sommet:  # pareil ici, compare le plus grand des sommets
                effacer_segment(etat, (sommet, extremite))
            else:
                effacer_segment(etat, (extremite, sommet))
    return False
