import fltk
from fonctions import *

taille = 100
rayon = 5

marge = taille / 2


# fonctions graphiques
def menu():
    """
    Fonction responsable du menu du jeu et nous renvoie
    le fichier que l'utlisateur a choisi.

    :return value: str
    """
    jouer = True
    fltk.cree_fenetre(600, 650)
    fltk.rectangle(100, 50, 500, 150,
                   couleur='black', remplissage='', epaisseur=1, tag='')
    fltk.rectangle(100, 200, 500, 300,
                   couleur='black', remplissage='', epaisseur=1, tag='')
    fltk.rectangle(100, 350, 500, 450,
                   couleur='black', remplissage='', epaisseur=1, tag='')
    fltk.rectangle(100, 500, 500, 600,
                   couleur='black', remplissage='', epaisseur=1, tag='')
    fltk.rectangle(550, 600, 600, 650,
                   couleur='black', remplissage='red', epaisseur=1, tag='')
    fltk.texte(200, 70, "grille-triviale", taille=40)
    fltk.texte(200, 220, "grille-vide", taille=40)
    fltk.texte(200, 370, "grille1", taille=40)
    fltk.texte(200, 520, "grille2", taille=40)

    fltk.texte(550, 600, "Quitter", taille=10, couleur='white')
    fichier = 'grille-vide.txt'
    fltk.mise_a_jour()
    while jouer:

        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        print(tev)
        if tev == 'Quitte':
            jouer = False
            print(oui)
            break
        x, y = fltk.attend_clic_gauche()
        if x > 100 and x < 500 and y > 50 and y < 150:
            fichier = 'grille-triviale.txt'
            break
        if x > 100 and x < 500 and y > 200 and y < 300:
            fichier = 'grille-vide.txt'
            break
        if x > 100 and x < 500 and y > 350 and y < 450:
            fichier = 'grille1.txt'
            break
        if x > 100 and x < 500 and y > 500 and y < 600:
            fichier = 'grille2.txt'
            break
        if x > 550 and x < 600 and y > 600 and y < 650:
            fermer = False
            fltk.ferme_fenetre()
            return None
            break
    fltk.ferme_fenetre()
    return fichier


def ready():
    """
    Fonction permettant d'afficher un message de début de jeu.
    Le message s'efface quand on clique sur la fenêtre.
    """
    jouer = True
    fltk.cree_fenetre(600, 650)
    fltk.texte(50, 100, "Tapez sur une touche pour commencer !",
               taille=20, couleur='red')
    fltk.mise_a_jour()
    fltk.attend_clic_gauche()
    fltk.ferme_fenetre()


def fin():
    """
    Fonction qui lorsque les deux conditions de victoires sont réunis,
    dessine un message de victoire en haut à gauche de l'écran.
    """
    fltk.texte(0, 0, "C'est gagné !", taille=20)
    fltk.mise_a_jour()


def print_points(indices, r):
    """
    Fonction permettant d'afficher les sommets (points) dans
    la grille du jeu.

    :param indices: liste de liste
    :param r: int (rayon des cercles)
    """
    horizon = len(indices[0])
    vertical = len(indices)
    for h in range(horizon + 1):
        for v in range(vertical + 1):
            fltk.cercle(h * taille+marge, v * taille+marge, r,
                        remplissage="black")


def print_etat(liste):
    """
    Fonction permettant d'afficher graphiquement l'état de la grille
    en créant un cercle si le segment est interdit et une ligne sinon.

    :param liste: liste
    """
    for data in liste:
        if est_trace(liste, data):  # est_trace
            (x1, y1), (x2, y2) = data
            x1a, y1a, x2a, y2a = x1 * taille+marge, y1 * taille+marge, x2 * taille+marge, y2 * taille+marge
            fltk.ligne(x1a, y1a, x2a, y2a)
        if est_interdit(liste, data):  # est_interdit
            (x1, y1), (x2, y2) = data
            x1a, y1a, x2a, y2a = x1 * taille+marge, y1 * taille+marge, x2*taille+marge, y2 * taille+marge
            fltk.cercle(x1a/2+x2a/2, y1a/2+y2a/2, 5, remplissage="red")


def print_indices(indices, tailleq, etat):
    """
    Fonction permettant d'afficher les valeurs indices dans la grille,
    si la valeur est None on affiche rien sinon on met le chiffre
    dans sa place correspandante.

    :param indices: liste de liste
    :param tailleq: int (taille du texte)
    :param etat: dico
    """
    for x in range(len(indices[0])):
        for y in range(len(indices)):
            if indices[x][y] is not None:
                if statut_case(indices, etat, (x, y)) == 0:
                    fltk.texte(y*taille+taille-10, x*taille+taille-10,
                               indices[x][y], taille=tailleq, couleur='blue')
                elif statut_case(indices, etat, (x, y)) == -1:
                    fltk.texte(y*taille+taille-10, x*taille+taille-10,
                               indices[x][y], taille=tailleq, couleur='red')

                else:
                    fltk.texte(y*taille+taille-10, x*taille+taille-10,
                               indices[x][y], taille=tailleq, couleur='black')
