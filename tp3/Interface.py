# -*- coding: utf-8 -*-

import random

def moyenneMatrice(matrice):
    '''
    Retourne la moyenne de poids entre les noeuds d'une matrice

        Paramètres:
            matrice[nxn]: matrice d'adjacence
        
        Renvoie:
            moyenne[1x1]: la moyenne de poids entre les noeuds 
    '''
    moyenne = 0
    for line in matrice:
        for elem in line:
            if elem != -1:
                moyenne += 1
    moyenne /= len(matrice)
    return moyenne


def ajusterPoids(matrice, nombre_de_noeuds, operation='ajouter',):
    '''
    Ajoute un poids entre deux noeuds précédemment non reliés d'une matrice d'adjacence

        Paramètres:
            matrice[nxn]: matrice d'adjacence
            operation[string]: l'operation à appliquer
        
        Renvoie:
            matrice[nxn]: matrice d'adjacence
    '''
    if operation == 'ajouter':
        while True:
            noeud_1 = random.randint(0, nombre_de_noeuds - 1)
            noeud_2 = random.randint(0, nombre_de_noeuds - 1)
            if noeud_1 != noeud_2 and matrice[noeud_1][noeud_2] == -1:
                break
        poids = random.randint(1, 99)
        matrice[noeud_1][noeud_2] = matrice[noeud_2][noeud_1] = poids
    elif operation == 'enlever':
        while True:
            noeud_1 = random.randint(0, nombre_de_noeuds - 1)
            noeud_2 = random.randint(0, nombre_de_noeuds - 1)
            if noeud_1 != noeud_2 and matrice[noeud_1][noeud_2] != -1:
                break
        matrice[noeud_1][noeud_2] = matrice[noeud_2][noeud_1] = -1

    return matrice


def saisirMatrice():
    noeud = int(input("Donner le nombre de noeuds dans la matrice: "))
    poids = int(input('Donner le nombre de poids dans la matrice: '))
    matrice = [[-1] * noeud for i in range(noeud)]
    for i in range(poids):
        print("\n\tSaisir le poids", i)
        extremite_1 = int(input("\t\tDonner le noeud d'extremité 1: "))
        extremite_2 = int(input("\t\tDonner le noeud d'extremité 2: "))
        poids_0 = int(input('\t\tSaisir le poids: '))
        matrice[extremite_1][extremite_2] = poids_0
        matrice[extremite_2][extremite_1] = poids_0
    return matrice


def genereMatriceAleatoire(nb_noeuds):
    if nb_noeuds > 0 and isinstance(nb_noeuds, int):
        matrice = [[-1] * nb_noeuds for i in range(nb_noeuds)]
    else:
        print('Error. Number of nodes is not a positive integer')
        return None

    moyenne_presente = 0
    moyenne_attendue = nb_noeuds // 2
    while moyenne_presente != moyenne_attendue:
        if moyenne_presente < moyenne_attendue:
            matrice = ajusterPoids(matrice, nb_noeuds, 'ajouter')
            moyenne_presente = moyenneMatrice(matrice) 

        elif moyenne_presente > moyenne_attendue:
            matrice = ajusterPoids(matrice, nb_noeuds, 'enlever')
            moyenne_presente = moyenneMatrice(matrice)
    return matrice

def afficheChemin(predecesseurs, depart, arrive):
    for i in predecesseurs:
        if (i == -1 or i >= 0) and depart >= 0 and arrive >= 0 :
            good_values = True
        else:
            good_values = False
            print('Error. Predecessor list contains unsupported values')
            return None
            
    if good_values:
        noeud_courant = arrive
        visite = [noeud_courant]
        while noeud_courant != depart:
            noeud_courant = predecesseurs[noeud_courant]
            visite.insert(0, noeud_courant)

    FOLLOWING_CHAR = "  ==> "
    output = "Le chemin à parcourir est:\n\tDEBUT : "
    for i in range(len(visite)):
        output += str(visite[i])
        if i == len(visite) - 1:
            output += ': FIN \n'
        else:
            output += FOLLOWING_CHAR
    return output

if __name__ == '__main__':
    saisirMatrice()
    
    nb_noeuds = 5
    matAlea = genereMatriceAleatoire(nb_noeuds)
    txt = "la matrice aleatoire est: \n\t"
    for i in matAlea:
        for j in i:
            txt += "{}\t".format(j)
        txt += "\n\t"
    print(txt)
    predecesseurs = [-1, 0, 0, 2, 5, 2]
    depart = 0
    arrive = 4
    print(afficheChemin(predecesseurs, depart, arrive))
