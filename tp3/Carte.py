# -*- coding: utf-8 -*-

import math

def est_dictionnaire_sommet(sommet):
    '''
    Indique si le dictionnaire est un dictionnaire de sommet

        Paramètre:
            sommet[1x1 dictionnaire]: Le sommet à tester

        Renvoie:
            bool: True si le dictionnaire est un dictionnaire de sommmet
    '''

    keys = ('no', 'x', 'y', 'altitude')
    if len(sommet) != len(keys):
        return False
    for key in keys:
        if key not in sommet:
            return False
    return True


def estVoisin(sommet1, sommet2):
    '''
    Valide que deux sommets sont voisins.
    
        Paramètres:
            sommet1[1x1 dictionnaire]: Le premier sommet.
            sommet2[1x1 dictionnaire]: Le deuxième sommet.
    
        Renvoie:
            distance[1x1]: Vrai si les sommets sont voisins.
    '''

    if not est_dictionnaire_sommet(sommet1) or not \
        est_dictionnaire_sommet(sommet2):
        print('Dictionnary is not a summit dictionary')
        return None

    x1, x2 = sommet1['x'], sommet2['x']
    y1, y2 = sommet1['y'], sommet2['y']

    return  abs(x1 - x2) == 0 and abs(y1 - y2) == 1 or \
            abs(x1 - x2) == 1 and abs(y1 - y2) == 0 or \
            abs(x1 - x2) == 1 and abs(y1 - y2) == 1


def distanceEuclidienne(sommet1, sommet2):
    '''
    Calcule la distance euclidienne entre deux sommets.
    
        Paramètres:
            sommet1[1x1 dictionnaire]: Le premier sommet.
            sommet2[1x1 dictionnaire]: Le deuxième sommet.

        Renvoie:
            distance[1x1]:La distance euclidienne entre les deux sommets.
    '''
    if not est_dictionnaire_sommet(sommet1) or not \
        est_dictionnaire_sommet(sommet2):
        print('Dictionnary is not a summit dictionary')
        return None

    return math.sqrt((sommet1['x'] - sommet2['x']) ** 2 + (sommet1['y'] - sommet2['y']) ** 2)


def distance3D(sommet1, sommet2):
    '''
    Calcule la distance 3D entre deux sommets.
    
        Paramètres:
            sommet1[1x1 dictionnaire]: Le premier sommet.
            sommet2[1x1 dictionnaire]: Le deuxième sommet.
        
        Renvoie:
            distance[1x1]:La distance 3D entre les deux sommets.
    '''
    if not est_dictionnaire_sommet(sommet1) or not \
            est_dictionnaire_sommet(sommet2):
        print('Dictionnary is not a summit dictionary')
        return None
    
    altitude1, altitude2 = sommet1['altitude'], sommet2['altitude']
    distance_sommets = distanceEuclidienne(sommet1, sommet2)

    return math.sqrt(distance_sommets ** 2 + (altitude1 - altitude2) ** 2)


def matriceAdjacence(sommets):
    '''
    Retourne la matrice d’adjacence à partir d’un tableau de sommets.
    
        Paramètres:
            sommets[1x1 dictionnaire]: Tableau de sommets.
    
        Renvoie:
            Matrice[nxn]: la somme des poids entre le sommets de départ et l'arrivé
    '''

    if not est_dictionnaire_sommet(sommets):
        print('Dictionnary is not a summit dictionary')
        return None

    #1) determiner le nombre de sommet de sommets
    nombre_de_sommets = len(sommets['no'])

    #2) creer une liste de liste de -1 de nombre de sommet
    liste_vide = [-1 for i in range(nombre_de_sommets)]
    matrice = [liste_vide[:] for i in range(nombre_de_sommets)]

    #3) determiner la matrice d'adjacence des sommets
    for i in range(nombre_de_sommets):
        sommet1 = {'no': sommets['no'][i], 'x': sommets['x'][i], \
                'y': sommets['y'][i], 'altitude': sommets['altitude'][i]}
        for j in range(nombre_de_sommets):
            sommet2 = {'no': sommets['no'][j], 'x': sommets['x'][j], \
                'y': sommets['y'][j], 'altitude': sommets['altitude'][j]}
            if i == j:
                continue
            elif estVoisin(sommet1, sommet2):
                matrice[i][j] = distance3D(sommet1, sommet2)
    return matrice
              


def carteEnSommets(carte_topo):
    '''
    Converti les altitudes de la carte en tableau de sommets.
    
        Paramètres:
            carteTopographique[mxn]: Carte topographique des altitudes.
    
        Renvoie:
            sommets[1x1 dictionnaire]: dictionnaire des sommets de la carte
    '''
    
    # Valide que la carte topographique est de deux dimensions et de valeurs non négatives.
    # et compte le nombre de sommets
    nombre_de_sommets = 0
    if isinstance(carte_topo, list):
        for i in range(len(carte_topo)):
            if isinstance(carte_topo[i], list):
                for j in range(len(carte_topo[i])):
                    if  not isinstance(carte_topo[i][j], int) and not \
                        isinstance(carte_topo[i][j], float):
                        print('Error. Map might contain more than 2 dimensions')
                        return None
                    elif carte_topo[i][j] < 0:
                        print('Map contains negative values. Abort')
                        return None
                    else:
                        nombre_de_sommets += 1

    sommets = {}
    sommets['no'] = [i for i in range(nombre_de_sommets)]
    sommets['x'] = [i % len(carte_topo) for i in range(nombre_de_sommets)]
    sommets['y'] = [i // len(carte_topo) for i in range(nombre_de_sommets)]
    sommets['altitude'] = [carte_topo[i][j] for i in range(len(carte_topo)) for j in range(len(carte_topo[i]))]

    return sommets


if __name__ == '__main__':
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 2, 'x': 1, 'y': 1, 'altitude': 12}
    txt = "les deux noeuds sont ils voisin? {}"
    print(txt.format(estVoisin(sommet1, sommet2)))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 3, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "les deux noeuds sont ils voisin? {}"
    print(txt.format(estVoisin(sommet1, sommet2)))
    
    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "la distance euclidienne entre les deux sommets est: {:.2f}"
    print(txt.format(distanceEuclidienne(sommet1, sommet2)))

    sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
    sommet2 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
    txt = "la distance 3D entre les deux sommets est: {:.2f}"
    print(txt.format(distance3D(sommet1, sommet2)))
    
    carte_topo = [[12, 13], [23, 21]]
    sommets = carteEnSommets(carte_topo)
    print("Le dictionnaire des sommets est: \n\t",sommets)
    
    matrice_ad= matriceAdjacence(sommets)
    txt = "la matrice d'adjacense est: \n\t"
    for i in matrice_ad:
        for j in i:
            txt += "{:.3f}\t".format(j)
        txt += "\n\t"
    print(txt)
