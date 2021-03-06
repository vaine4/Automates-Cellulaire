# -*- coding: utf-8 -*-

################################################################################################################################################################

from random import random                     # Import de la fonction randint du module Random pour ajouter de la probabilité à la propagation du feu

################################################################################################################################################################

def propagationFeu(nbCellLignes, x, y, foret, p): # Algorithme gérant la propagation du feu
    clicX, clicY = x, y # On récupère les coordonnées de la cellule par rapport à la double-liste forêt
    listeForet = list(foret)
    listeCellEnFeu = []   # Liste retournée par la fonction, elle contient les coordonnées dans la double-liste forêt des cellules où le feu va se propager
    xMin, xMax, yMin, yMax = 0, 0, 0, 0 # Coordonnées des cellules sur lesquelles on va tester si le feu se propage de (xMin à xMax; yMin à yMax)

    if(clicX == 0):         # On test la position de la cellule en feu sur la grille (cellule sur laquelle l'utilisateur a cliqué)
        xMin = clicX
        xMax = clicX+1

    elif(clicX == nbCellLignes-1):
        xMin = clicX-1
        xMax = clicX

    else:
        xMin = clicX-1
        xMax = clicX+1

    if(clicY == 0):
        yMin = clicY
        yMax = clicY+1

    elif(clicY == nbCellLignes-1):
        yMin = clicY-1
        yMax = clicY

    else:
        yMin = clicY-1
        yMax = clicY+1      # Fin du test de la position de la cellule en feu sur la grille

    for j in range(yMin, yMax+1):
        for i in range(xMin, xMax+1):

            if(i != clicX or j != clicY): # Si la cellule à tester est la cellule déjà en feu, on ne fait rien
                if(listeForet[j][i] == "1" and random() < p): # Si la cellule voisine est un arbre, alors on l'ajoute dans la liste des cellules à incendier
                    listeCellEnFeu.append(i)
                    listeCellEnFeu.append(j)
                    listeForet[j][i] = "3"   # Comme la cellule est un arbre qui va prendre feu, alors on le met à l'état 3, soit arbres en feu

    return list(listeCellEnFeu), list(listeForet)   # On retourne la liste des cellules en feu et la liste forêt