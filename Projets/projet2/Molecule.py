# -*- coding: utf-8 -*-
# Nom_du_fichier: Molecule.py
# Cree le       : 6 Octobre 2021
# Cree par      : Erreur-404
# Version num   : 1
# Modifie le    : 6 Octobre 2021

from random import randint, randrange


def creerMolecule(x, y, dx, dy, rayon):
    '''
    La fonction reçoit la position (x, y) de la molécule, ça vitesse (dx, dy) 
    et son rayon. La fonction renvoie un dictionnaire.

        Paramètres:
            x[1x1]: position en x de la molécule.
            y[1x1]: position en y de la molécule.
            dx[1x1]: vitesse de déplacement en x de la molécule.
            dy[1x1]: vitesse de déplacement en y de la molécule.
            rayon[1x1]: rayon de la molécule.
        
        Renvoie:
            molecule[1x1]: un dictionnaire de type molécule
    '''
    return {'x': x, 'y': y, 'dx': dx, 'dy': dy, 'rayon': rayon}


def moleculesSeTouche(mol_1, mol_2):
    '''
        La fonction renvoie vrai si les deux molécules se touchent faux sinon.

        Paramètres:
            mol_1[1x1]: dictionnaire de type molécule.
            mol_2[1x1]: dictionnaire de type molécule.

        Renvoie:
            Boolean
    '''
    # Verifies that the parameters are molecule dictionaries
    for keys in ('x', 'y', 'dx', 'dy', 'rayon'):
        if keys not in mol_1 or keys not in mol_2:
            print('Error. Wrong dictionary.')
            return None

    d = (((mol_1['x'] - mol_2['x'])**2) + ((mol_1['y'] - mol_2['y'])**2)) ** 0.5
    return d <= mol_1['rayon'] + mol_2['rayon']


def deplacerMolecule(mol):
    '''
    Déplace la molécule

        Paramètres:
            mol[1x1]: dictionnaire de type molécule.
        
        Renvoie:
            mol[1x1]: dictionnaire de type molécule.
    '''
    mol['x'] += mol['dx']
    mol['y'] += mol['dy']
    return mol


#####################################################
# Donner
#####################################################
def ajusteDirApresCollision(mol_1, mol_2):
    deltaX = mol_2['x'] - mol_1['x']
    dVx = 0

    if (deltaX == 0.0):
        dVy = mol_2['y'] - mol_1['y']
    else:
        r = (mol_2['y'] - mol_1['y']) / deltaX
        dVx = (mol_2['dx'] - mol_1['dx'] + (mol_2['dy'] - mol_1['dy']) * r) / (1 + r * r)
        dVy = r * dVx

    mol_1['dx'] += dVx
    mol_1['dy'] += dVy
    mol_2['dx'] -= dVx
    mol_2['dy'] -= dVy

    return mol_1, mol_2


def creerListMolecules(hauteur, xmin, xmax, nbMolecules):
    '''
    Crée une liste de molécules.
    
        Paramètres:
            hauteur[1x1] : hauteur du réservoir
            xmin[1x1] : position x minimale
            xmax[1x1] : position x maximale
            nbMolecules[1x1] : nombre de molécules a créé
        
        Renvoie:
            molecules[1xnbMolecules]: liste qui contient les molécules générées aléatoirement
    '''
    molecules = []
    for molecule in range(nbMolecules):
        rayon = randrange(10, 30, 2)
        x = randint(xmin + rayon, xmax - rayon)
        y = randint(rayon, hauteur - rayon)
        dx = randint(1, 5)
        dy = randint(1, 5)
        molecules.append(creerMolecule(x, y, dx, dy, rayon))
    return molecules


def inverseDirMolecule(mol, paroiG, paroiD, hauteur):
    '''
    Inverse la direction de la molécule si elle frappe une paroi

        Paramètres:
            mol[1x1] : dictionnaire de type molécule
            paroiG[1x1] : paroi gauche
            paroiD[1x1] : paroi droite
            hauteur[1x1] : hauteur du réservoir
        
        Renvoie:
            mol[1x1]: dictionnaire de type molécule
    '''
    # Verifies that the parameters are molecule dictionaries
    for keys in ('x', 'y', 'dx', 'dy', 'rayon'):
        if keys not in mol:
            print('Error. Wrong dictionary.')
            return None

    if mol['x'] - mol['rayon'] <= paroiG:
        mol['x'] = paroiG + mol['rayon']
        mol['dx'] *= -1     # Inverse la direction de la vitesse


    if mol['x'] + mol['rayon'] >= paroiD:
        mol['x'] = paroiD - mol['rayon']
        mol['dx'] *= -1


    if mol['y'] + mol['rayon'] >= hauteur:
        mol['y'] = hauteur - mol['rayon']
        mol['dy'] *= -1


    if mol['y'] - mol['rayon'] <= 0:
        mol['y'] = mol['rayon']
        mol['dy'] *= -1



    return mol

if __name__ == '__main__':
    # Test creerMolecule
    x, y, dx, dy, rayon = 5, 2, -3, 4, 5
    mol = creerMolecule(x, y, dx, dy, rayon)
    text = "La position de la molecule est ({}, {}), sa vitesse est ({}, {}) "
    text += "et son rayon est {}"
    
    print(text.format(mol['x'], mol['y'], mol['dx'], mol['dy'], mol['rayon']))

    # Test moleculesSeTouche
    
    mol_1  = creerMolecule(x, y, dx, dy, rayon)
    mol_2  = mol_1
    result = moleculesSeTouche(mol_1, mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
       
    mol_2  = creerMolecule(x, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon/4)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+2*rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    # Test deplacerMolecule
    
    old_text = "Avant le deplacement \n\t" + text
    print(old_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
    
    mol = deplacerMolecule(mol)
    new_text = "Apres le deplacement \n\t" + text
    print(new_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
