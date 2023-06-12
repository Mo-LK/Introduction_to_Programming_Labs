# -*- coding: utf-8 -*-

from Carte import carteEnSommets, matriceAdjacence

def lireCarte(nom_fichier):
    '''
    Lit le fichier à partir du nom de fichier reçu en paramètre.
    
        Paramètres:
            nomFichier[1xn char]: Nom du fichier à lire.
        
        Renvoie:
            matrice[mxn]: matrice des altitudes lut dans la carte topographique.
    '''
    if isinstance(nom_fichier, str):
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            data = fichier.readlines()
        matrice = []
        for index, line in enumerate(data):
            matrice.append([])
            line = line.rstrip()
            numbers = [int(i) for i in line.split(',')]
            for number in numbers:
                matrice[index].append(number)
    else:
        print('Error. Filename is not a string')
        return None
    return matrice

def chargeMatriceDeCarte(nom_fichier):
    '''
    Reçoit un nom de fichier et retourne la matrice d’adjacence correspondant au fichier lut. 
        
        Paramètres:
            nomFichier[1xn char]: Nom du fichier à lire.
        
        Renvoie:
            matrice[mxn]: matrice d’adjacence trouver à partir du fichier lu.
    '''
    #1) lire la carte
    if isinstance(nom_fichier, str):
        matrice = lireCarte(nom_fichier)
    else:
        print('Error. Filename is not a string')
        return None
    #2) transformer la carte lu en sommet
    sommets = carteEnSommets(matrice)    

    #3) determiner la matrice d’adjacence
    matrice = matriceAdjacence(sommets)
    return matrice


if __name__ == '__main__':
    nom_fichier = 'carte.txt'
    carte = lireCarte(nom_fichier)
    print("la carte lu est:")
    for ligne in carte:
        print("\t", ligne)
        
        nom_fichier = 'mini_carte.txt'
    carte = chargeMatriceDeCarte(nom_fichier)
    
    txt = "matrice d'adjacense de la carte lu est: \n\t"
    for i in carte:
        for j in i:
            txt += "{:.3f}\t".format(j)
        txt += "\n\t"
    print(txt)
    