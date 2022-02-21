from graphique import *
from fonctions import *
from solveur import *
import fltk


indices = []


if __name__ == '__main__':
    ready()
    fichier = menu()
    if fichier is not None:
        lire_fichier(fichier, indices)
        etat = dict()
        fltk.cree_fenetre((len(indices[0])+1)*taille, (len(indices)+1)*taille)
        jouer = True
        while jouer:
            fltk.efface_tout()
            print_points(indices, rayon)
            print_indices(indices, 18, etat)
            print_etat(etat)
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)
            if tev == 'Quitte':
                jouer = False
                break
            if tev == "ClicGauche":
                print("ClicGauche")
                x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                xa, ya = x-marge, y-marge
                xa, ya = xa/taille, ya/taille
                var = 0.2
                if trop_proche(xa, ya, var):
                    if xa-int(xa) < var and xa-int(xa) > -var:
                        segmenttemp = ((int(xa), int(ya)), (int(xa), int(ya)+1))
                    if ya-int(ya) < var and ya-int(ya) > -var:
                        segmenttemp = ((int(xa), int(ya)), (int(xa)+1, int(ya)))
                    ((a, b), (c, d)) = segmenttemp
                    if b <= len(indices) and d <= len(indices) and a <= len(indices) and c <= len(indices):
                        if est_vierge(etat, segmenttemp):  # est_vierge
                            tracer_segment(etat, segmenttemp)  # tracer_segment
                        else:
                            effacer_segment(etat, segmenttemp)  # effacer_segment
                deuxieme_indice(indices, etat)
                affichage(indices, etat)
            if tev == "ClicDroit":
                print("ClicDroit")
                x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
                xa, ya = x-marge, y-marge
                xa, ya = xa/taille, ya/taille
                var = 0.2
                if trop_proche(xa, ya, var):
                    if xa-int(xa) < var and xa-int(xa) > -var:
                        segmenttemp = ((int(xa), int(ya)), (int(xa), int(ya)+1))
                    if ya-int(ya) < var and ya-int(ya) > -var:
                        segmenttemp = ((int(xa), int(ya)), (int(xa)+1, int(ya)))
                    ((a, b), (c, d)) = segmenttemp
                    if b <= len(indices) and d <= len(indices) and a <= len(indices) and c <= len(indices):
                        interdire_segment(etat, segmenttemp)

                affichage(indices, etat)
            if premier_indice(indices, etat) and deuxieme_indice(indices, etat):
                fin()
            if tev == "Touche":
                flag = 0
                for i in range(len(indices)):
                    for j in range(len(indices[0])):
                        if solveur(indices, etat, (i, j)):
                            flag = 1
                            affichage(indices, etat)
                            fin()
                            break
                    if flag == 1:
                        break
            fltk.mise_a_jour()
        fltk.ferme_fenetre()
