from typing import List

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from constantes import DELTA_V_MINIMUM_PAR_CORPS_CELESTE, CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS
from fichiers_pieces import charger_capsules_df, charger_moteurs_df, charger_reservoirs_df
from fusee import Fusee, Capsule, Reservoir, Moteur


def creer_capsules(capsules_df: pd.DataFrame) -> List[Capsule]:
    '''
    Crée une liste d'objets Capsule à partir d'un dataframe.

        Paramètres
            capsules_df : Un dataframe contenant des informations sur des capsules
        
        Valeur de retour
            Type : List[Capsule]
            Description : Une liste d'objets de type Capsule
    '''
    capsules = list()
    for index in capsules_df.index:
        rangee = capsules_df.iloc[index]
        nom = rangee['nom']
        hauteur = rangee['hauteur']
        masse = rangee['masse']
        prix = rangee['prix']
        places = rangee['places']
        capsules.append(Capsule(nom, hauteur, masse, prix, places))
    return capsules
    


def creer_moteurs(moteurs_df: pd.DataFrame) -> List[Moteur]:
    '''
    Crée une liste d'objets Moteur à partir d'un dataframe.
        
        Paramètres
            moteurs_df : Un dataframe contenant des informations sur des moteurs
        
        Valeur de retour
            Type : List[Moteur]
            Description : Une liste d'objets de type Moteur
    '''
    # Transforme le dataframe des moteurs en liste d'objets de type Moteur
    moteurs = list()
    moteurs_df = moteurs_df.reset_index(drop=True)
    for index in moteurs_df.index:
        rangee = moteurs_df.iloc[index]
        nom = rangee['nom']
        hauteur = rangee['hauteur']
        masse = rangee['masse']
        prix = rangee['prix']
        impulsion_specifique = rangee['impulsion specifique']
        moteurs.append(Moteur(nom, hauteur, masse, prix, impulsion_specifique))
    return moteurs


def creer_reservoirs(reservoirs_df: pd.DataFrame) -> List[Reservoir]:
    '''
    Crée une liste d'objets Reservoir à partir d'un dataframe.

        Paramètres
            reservoirs_df : Un dataframe contenant des informations sur des réservoirs
        
        Valeur de retour
            Type : List[Reservoir]
            Description : Une liste d'objets de type Reservoir
    '''
    # Transforme le dataframe des reservoir en liste d'objets de type Reservoir
    reservoirs = list()
    for index in reservoirs_df.index:
        rangee = reservoirs_df.iloc[index]
        nom = rangee['nom']
        hauteur = rangee['hauteur']
        masse = rangee['masse']
        prix = rangee['prix']
        capacite = rangee['capacite']
        reservoirs.append(Reservoir(nom, hauteur, masse, prix, capacite))
    return reservoirs



def corps_celestes_accessibles(fusee: Fusee) -> List[str]:
    '''
    Retourne la liste des corps célestes accessibles par la fusée.
    
        Paramètres
            fusee : La fusée en question
        
        Valeur de retour
            Type : List[str]
            Description : Une liste des corps célestes accessibles par la fusée
    '''
    # Retourne la liste des corps célestes accessibles par la fusée.
    deltaV_fusee = fusee.calculer_deltav()
    return [corps_celestes for corps_celestes in DELTA_V_MINIMUM_PAR_CORPS_CELESTE \
        if DELTA_V_MINIMUM_PAR_CORPS_CELESTE[corps_celestes] < deltaV_fusee]


def comparer_fusee(fusee_1: Fusee, fusee_2: Fusee) -> None:
    '''
    Affiche un graphique de comparaison entre deux fusées.
        
        Paramètres
            fusee_1 : La première fusée à comparer
            fusee_2 : La deuxième fusée à comparer
        
        Valeur de retour
            Aucune
    '''
    # Crée un grouped barplot comparant les fusées passées en paramètre en fonction des trois métriques suivantes:
    #  * Masse / Coût
    #  * DeltaV / Coût
    #  * DeltaV / Masse

    # Calcule les ratios
    deltaV_masse_1 = fusee_1.calculer_deltav() / fusee_1.masse
    deltaV_masse_2 = fusee_2.calculer_deltav() / fusee_2.masse
    deltaV_prix_1 = fusee_1.calculer_deltav() / fusee_1.prix
    deltaV_prix_2 = fusee_2.calculer_deltav() / fusee_2.prix
    hauteur_masse_1 = fusee_1.hauteur / fusee_1.masse
    hauteur_masse_2 = fusee_2.hauteur / fusee_2.masse

    # Génère un dataframe avec trois colonnes; fusée, résultats des différents ratios et type_ratio
    d = {'fusée': [fusee_1.nom, fusee_1.nom, fusee_1.nom,
            fusee_2.nom, fusee_2.nom, fusee_2.nom], 
        'Ratios': [deltaV_masse_1, deltaV_prix_1, hauteur_masse_1, 
            deltaV_masse_2, deltaV_prix_2, hauteur_masse_2], 
        'type_ratio': ['deltaV/masse', 'deltaV/prix', 'hauteur/masse', 
            'deltaV/masse', 'deltaV/prix', 'hauteur/masse']}
    df = pd.DataFrame(d)
    sns.catplot(data=df, x='fusée', y='Ratios', hue='type_ratio', kind='bar')
    plt.show()


if __name__ == '__main__':
    # creer_capsules
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    capsules = creer_capsules(capsules_df)
    for capsule in capsules:
        print(capsule)
    print()

    # creer_moteurs
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)
    moteurs = creer_moteurs(moteurs_df)
    for moteur in moteurs:
        print(moteur)
    print()

    # creer_reservoirs
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    reservoirs = creer_reservoirs(reservoirs_df)
    for reservoir in reservoirs:
        print(reservoir)
    print()

    # corps_celestes_accessibles
    capsule = Capsule("PasDBonSens", 1.5, 840.0, 600.0, 1)
    reservoir_1 = Reservoir("Piscine", 25.0, 9000.0, 13000.00, 6480.0)
    moteur = Moteur("La Puissance", 12.0, 15000.0, 39000.00, 295)
    fusee_1 = Fusee("Romano Fafard", capsule, reservoir_1, moteur)

    deltaV = fusee_1.calculer_deltav()
    corps_celestes = corps_celestes_accessibles(fusee_1)
    print(f"La fusée {fusee_1.nom} peut aller, avec {deltaV:.2f} de deltaV, jusqu'à: {corps_celestes}")
    print()

    # comparer_fusee
    reservoir_2 = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    fusee_2 = Fusee("Romano Fafard Lite", capsule, reservoir_2, moteur)
    comparer_fusee(fusee_1, fusee_2)
