# -*- coding: utf-8 -*-
def est_matrice_carree(matrice):
    for line in matrice:
        if len(line) != len(matrice):
            print()
            return False
        for elem in line:
            if elem < -1:
                return False
    return True

def indiceMinimum(vec): 
    '''
    Trouve l’indice et la valeur minimum dans un vecteur.

        Paramètres:
            vec[1xn]: Vecteur des valeurs à parcourir.
        Renvoie:
            indice[1x1]: l’indice de la case minimum.
            minimum[1x1]: la valeur minimum du vecteur.
    '''
    # Vérifie que la boucle ne contient que des valeurs numériques
    # plus grandes ou égales à -1
    vec_verifie = []
    for val in vec:
        if not str(val).isnumeric() or val < -1:
            vec_verifie.append(val)
    if len(vec_verifie) == len(vec):
        return -1, -1

    vec_sans_moins_un = [i for i in vec if i > 0]
    
    minimum = min(vec_sans_moins_un)
    indice = vec.index(minimum)
    return indice, minimum

    
def noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis):
    '''
    Cherche le nœud non visité ayant le poids minimum autour d’un nœud spécifique.

        Paramètres:
            Matrice[mxn]: Matrice d’adjacence.
            noeud[1x1]: Le nœud autour duquel on veut chercher le nœud non visité minimum.
            noeudsVisites[1xn]: La liste des nœuds visités.

        Renvoie:
            nœuds[1x1]: Noeud voisin avec la distance minimum.
            poids[1x1]: Poids du nœud voisin avec la distance minimum.
    '''
    if not est_matrice_carree(matrice):
        print('Error. Not a square matrix, or matrix contains unsupported values')
        return None

    if noeud not in noeuds_vis:
        print('Node not in visited nodes.')
        return None

    #1) extraire la ligne du noeud de la matrice
    # Fait une copie profonde de la matrice
    new_matrice = []
    counter = 0
    for i in matrice:
        new_matrice.append([])
        for j in i:
            new_matrice[counter].append(j)
        counter += 1

    if noeud >= 0 and noeud % 1 == 0:
        ligne = new_matrice[noeud]
    else:
        print('Error. Node is not a scalable positive integer')
        return None

    #2) affecter -1 pour chaque noeud des noeuds_vis de la ligne
    for visite in noeuds_vis:
        if visite >= 0 and visite % 1 == 0:
            ligne[visite] = -1
        else:
            print('Error. Visited nodes list contains non-integer, negative or nul value.')
            return None

    #3) Trouve l’indice et la valeur minimum de la ligne
    noeud, poids = indiceMinimum(ligne)
    return noeud, poids

def noeudMinimalNonVisites(matrice, noeuds_vis):
    '''
    Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins.
    
        Paramètres:
            Matrice[mxn]: Matrice d’adjacence.
            noeudsVisites[1xn]: La liste des nœuds visités.
        Renvoie:
            depart[1x1]: le nœud visité.
            arrive[1x1]: le nœud ayant le plus petit poids avec le nœud de départ.

    '''
    #TODO: Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins
    #TODO: utiliser la fonction noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    if not est_matrice_carree(matrice):
        print('Error. Not a square matrix, or matrix contains unsupported values')
        return None
    
    for noeud in noeuds_vis:
        if noeud < 0 or noeud % 1 != 0:
            print('Error. noeuds_vis contains unsupported values')
            return None

    prochains_noeuds = []
    for noeud in noeuds_vis:
        noeud_arrive, poids = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
        prochains_noeuds.append((noeud, noeud_arrive, poids))

    poids_minimum = min([i[2] for i in prochains_noeuds if i[2] != -1])
    for tuple in prochains_noeuds:
        if tuple[2] == poids_minimum:
            depart, arrive = tuple[0], tuple[1]

    return depart, arrive


def noeudsVoisins(matrice, noeud):
    '''
    Cherche les nœuds voisins et leur poids par rapport à un nœud initial. 
    Les nœuds voisins ont un poids différent de -1 dans la matrice d’adjacence.

        Paramètres:
            Matrice[mxn]: Matrice d’adjacence.
            nœud[1x1]: Indice du nœud auquel on veut trouver les voisins.
        Renvoie:
            noeuds[1xn]: Vecteur des nœuds voisins.
            poids[1xn]: Vecteur des poids des nœuds voisins.
    '''
    if not est_matrice_carree(matrice):
        print('Error. Not a square matrix, or matrix contains unsupported values')
        return None
    if noeud >= 0 and noeud % 1 == 0:
        voisins = matrice[noeud]   
        noeuds = [voisin for voisin in range(len(voisins)) if voisins[voisin] > 0]
        poids = [voisins[voisin] for voisin in range(len(voisins)) if voisins[voisin] > 0]
    return noeuds, poids


def dijkstra(matrice, depart, arrive):
    '''
    Calcule le plus court chemin entre un nœud de départ et un nœud d’arrivée.
        Paramètres:
            Matrice[mxn]: Matrice d’adjacence.
            depart[1x1]: Le nœud de départ.
            arrive[1x1]: Le nœud d’arrivé.
        Renvoie:
            distance[1x1]: la somme des poids entre le nœud de départ et l’arrivé.
            predecesseur[1xn]: vecteur des nœuds précédent pour se rendre au départ.
    '''
    if not est_matrice_carree(matrice):
        print('Error. Not a square matrix, or matrix contains unsupported values')
        return None

    predecesseurs = [-1 for i in matrice]
    distance_min = [-1 for i in matrice]
    distance_min[depart] = 0
    if depart >= 0 and arrive >= 0 and depart % 1 == 0 and arrive % 1 == 0:
        noeud_courant = depart
    else:
        print('Error. Unsupported values.')
        return None
    noeudVisites = [noeud_courant]
    while len(noeudVisites) != len(matrice) and noeud_courant != arrive:
        noeuds_voisins_tuple = noeudsVoisins(matrice, noeud_courant)
        for noeud_voisin, poids in zip(noeuds_voisins_tuple[0], noeuds_voisins_tuple[1]):
            distance = distance_min[noeud_courant] + poids
            if distance < distance_min[noeud_voisin] or distance_min[noeud_voisin] == -1:
                distance_min[noeud_voisin] = distance
                predecesseurs[noeud_voisin] = noeud_courant
        noeud_courant = noeudMinimalNonVisites(matrice, noeudVisites)[1]
        noeudVisites.append(noeud_courant)
    distance = distance_min[arrive]

    return distance, predecesseurs


if __name__ == '__main__':
    vec     = [-1, 4, 6, -1, -1, 3, 5]
    indice, minimum = indiceMinimum(vec)
    txt = "la valeur minimale du vecteur est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))

    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1, 2, 3]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))

    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeudsVisites = [1, 2, 3]
    depart, arrive = noeudMinimalNonVisites(matrice, noeudsVisites)
    txt = "Le noeud de départ est le noeud {} et le noeud 'non-visité' ayant le plus \n petit poids de avec le noeud de départ est le noeud {}"
    print(txt.format(depart, arrive))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 1
    noeudsVoisins(matrice, noeud)
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 3
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    depart  = 0
    arrive  = 3
    indice, prédécesseurs = dijkstra(matrice, depart, arrive)
    txt = "la distance la plus cours entre un noeud de départ {} et un noeud d’arrivée {} est {} avec les prédécesseurs {}"
    print(txt.format(depart, arrive, indice, prédécesseurs))
        