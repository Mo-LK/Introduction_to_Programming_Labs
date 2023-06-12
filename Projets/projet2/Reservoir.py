# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Cree le      : 6 Octobre 2021
# Cree par     : Erreur-404
# Version num  : 1
# Modifie le   : 6 Octobre 2021

import matplotlib.pyplot as plt
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules
from Molecule import ajusteDirApresCollision, inverseDirMolecule
import time


def creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD):
    '''
    Crée un réservoir et ajoute le nombre de molécules fourni pour chaque côté.

        Paramètres:
            hauteur[1x1] : hauteur du réservoir
            largeur[1x1] : largeur du réservoir
            posPar[1x1] : position de la paroi
            nbMoleculesG[1x1] : nombre de molécules de la partie gauche du réservoir /li>
            nbMoleculesD[1x1] : nombre de molécules de la partie droite du réservoir /li>

        Renvoie:
            reservoir[1x1]: dictionnaire de type réservoir
    '''

    molecules_gauche = creerListMolecules(hauteur, 0, posParoi, nbMoleculesG)
    molecules_droite = creerListMolecules(hauteur, posParoi, largeur, nbMoleculesD)
    list_collisions_gauche = [0 for i in range(nbMoleculesG) for j in range(i + 1, nbMoleculesG)]
    list_collisions_droite = [0 for i in range(nbMoleculesD) for j in range(i + 1, nbMoleculesD)]

    reservoir = {'h': hauteur, 'l': largeur, 'posPar': posParoi, 
                'mG': molecules_gauche, 'mD': molecules_droite, 
                'lCG': list_collisions_gauche, 'lCD': list_collisions_droite}
    return reservoir

  
        
def colision(reservoir):
    '''
    Indique les molécules qui sont en collision

        Paramètre:
            reservoir[1x1]: dictionnaire de type réservoir
        
        Renvoie:
            reservoir[1x1]: dictionnaire de type réservoir
    '''
    
    # Verifies that the parameter is a container dictionary
    for keys in ('h', 'l', 'posPar', 'mG', 'mD', 'lCG', 'lCD'):
        if keys not in reservoir:
            print('Error. Wrong dictionary.')
            return None
    
    index = 0
    molecules_G = reservoir['mG']
    for i in range(len(molecules_G)):
        for j in range(i + 1, len(molecules_G)):
            collision = moleculesSeTouche(molecules_G[i], molecules_G[j])
            if collision:
                molecules_G[i], molecules_G[j] = ajusteDirApresCollision(molecules_G[i], molecules_G[j])
            reservoir['lCG'][index] = int(collision)
            index += 1

    index = 0
    molecules_D = reservoir['mD']
    for i in range(len(molecules_D)):
        for j in range(i + 1, len(molecules_D)):
            collision = moleculesSeTouche(molecules_D[i], molecules_D[j])
            if collision:
                molecules_D[i], molecules_D[j] = ajusteDirApresCollision(molecules_D[i], molecules_D[j])
            reservoir['lCD'][index] = int(collision)
            index += 1
    return reservoir


def inverseDirMolecules(reservoir):
    '''
    Ajuste la direction des molécules qui touchent aux parois (des deux côtés).

        Paramètres:
            reservoir[1x1] : dictionnaire de type réservoir
        Renvoie:
            reservoir[1x1]: dictionnaire de type réservoir
    '''

    # Verifies that the parameter is a container dictionary
    for keys in ('h', 'l', 'posPar', 'mG', 'mD', 'lCG', 'lCD'):
        if keys not in reservoir:
            print('Error. Wrong dictionary.')
            return None

    for molecule in reservoir['mG']:
        inverseDirMolecule(molecule, 0, reservoir['posPar'], reservoir['h'])

    for molecule in reservoir['mD']:
        inverseDirMolecule(molecule, reservoir['posPar'], reservoir['l'], reservoir['h'])
    return reservoir

def getTemperature(reservoir, cote):
    '''
    Calcule la température du réservoir du côté donné

        Paramètres:
            reservoir[1x1] : dictionnaire de type réservoir
            coter[1x1] : le côté du réservoir ("Droite" ou "Gauche")
    
        Renvoie:
            T[1x1] : Température du côté du réservoir
    '''
    
    # Verifies that the parameter is a container dictionary
    for keys in ('h', 'l', 'posPar', 'mG', 'mD', 'lCG', 'lCD'):
        if keys not in reservoir:
            print('Error. Wrong dictionary.')
            return None

    masse = 1
    if cote == 'Droite':
        list_molecules = reservoir['mD']
    elif cote == 'Gauche':
        list_molecules = reservoir['mG']


    energie = 0
    for molecule in list_molecules:
        vitesse = (molecule['dx'] ** 2 + molecule['dy'] ** 2) ** 0.5
        energie += 0.5 * masse * (vitesse ** 2)

    temperature = energie / len(list_molecules)
    return temperature


#####################################################
# Donner
#####################################################
def affichage(reservoir):
    # Verifies that the parameter is a container dictionary
    for keys in ('h', 'l', 'posPar', 'mG', 'mD', 'lCG', 'lCD'):
        if keys not in reservoir:
            print('Error. Wrong dictionary.')
            return None
        
    txt = "Température côté Gauche: {:.2f}C \t\t\t\t\t Température côté Droit: {:.2f}C".expandtabs()   
    plt.figure(figsize=(20,10))
    plt.plot([reservoir['posPar'], reservoir['posPar']], [0, reservoir['h']], 'k-', linewidth=10) 
    plt.axis([-20, reservoir['l'] + 20, -20, reservoir['h'] + 20])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title(txt.format(getTemperature(reservoir, "Gauche"),getTemperature(reservoir, "Droite")),fontsize=23)
    
    for k in [['mG','ro'],['mD','go']]:
        for i in range(len(reservoir[k[0]])):  
            inte = min(max((abs(reservoir[k[0]][i]['dx']) + abs(reservoir[k[0]][i]['dy']))/60,0.2),1)
            plt.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha = inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])
    
    plt.pause(0.01)
    clear_output() 
    

def deplacerMolecules(reservoir):
    '''
    Déplace les molécules d'un réservoir

        Paramètres:
            reservoir[1x1] : dictionnaire de type réservoir
        
        Renvoie:
            reservoir[1x1]: dictionnaire de type réservoir
    '''
    
    # Verifies that the parameter is a container dictionary
    for keys in ('h', 'l', 'posPar', 'mG', 'mD', 'lCG', 'lCD'):
        if keys not in reservoir:
            print('Error. Wrong dictionary.')
            return None

    inverseDirMolecules(reservoir)
    affichage(reservoir)
    colision(reservoir)
    return reservoir

if __name__ == '__main__':
    hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD = 2000,2000,1300,100,50
    reservoir = creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD)
    print(reservoir)
    getTemperature(reservoir, 'Droite')
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir)
