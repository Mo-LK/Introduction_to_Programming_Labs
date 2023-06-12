import pandas as pd
from pandas.core.frame import DataFrame

from constantes import CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS, FICHIER_CAPSULE, FICHIERS_RESERVOIRS, \
    FICHIERS_MOTEURS


def ppl_to_dict(chemin_fichier: str) -> dict:
    '''
    Extrait les informations d'un fichier ppl et les renvoie sous la 
    forme d'un dictionnaire

        Paramètre
            chemin_fichier (str) : Une chaine de caractères du chemin vers le fichier ppl
        
        Valeur de retour
            Type : dict
            Description : Dictionnaire des informations du fichier ppl
    '''
    proprietes = dict()
    with open(chemin_fichier, 'r') as fichier:
        for ligne in fichier.readlines():
            ligne = ligne.rstrip()
            if ligne.startswith('#') or len(ligne) == 0:
                continue
            else:
                pos_char_attribution = ligne.find('=')
                key = ligne[:pos_char_attribution]
                value = ligne[pos_char_attribution + 1:]
                try:
                    if '.' in value:
                        proprietes[key] = float(value)
                    else:
                        proprietes[key] = int(value)
                except:
                    proprietes[key] = str(value)
    return proprietes


def charger_capsules_df(chemin_capsules: str) -> pd.DataFrame:
    '''
    Charge les capsules contenues dans le fichier capsules.csv dans un dataframe.
    
        Paramètres
            chemin_capsules (str) : Une chaine de caractères du chemin vers le dossier capsules
    
        Valeur de retour
            Type : pd.DataFrame
            Description : Le Dataframe des capsules avec les bons noms de colonnes
    '''
    # Retourne un dataframe des capsules décrites dans le fichier FICHIER_CAPSULE
    df = pd.DataFrame(pd.read_csv(chemin_capsules + '/' + FICHIER_CAPSULE))
    
    # Renomme les colonnes pour que celles-ci soient plus lisibles
    noms_attendus = ['nom', 'hauteur', 'masse', 'prix', 'places']
    noms_presents = [nom for nom in df.columns]
    nouveaux_noms = {i: j for i, j in zip(noms_presents, noms_attendus)}
    df = df.rename(columns=nouveaux_noms)
    return df


def charger_reservoirs_df(chemin_reservoirs: str) -> pd.DataFrame:
    '''
    Charge les réservoirs contenus dans les fichiers reservoir*.json dans un dataframe.
    
        Paramètres
            chemin_reservoirs (str) : Une chaine de caractères du chemin vers le dossier reservoirs
    
        Valeur de retour
            Type : pd.DataFrame
            Description : Le Dataframe combiné des réservoirs
    '''
    # Retourne un dataframe combiné des réservoirs décrits dans
    #  les fichiers FICHIERS_RESERVOIRS
    df = pd.DataFrame()
    for fichier in FICHIERS_RESERVOIRS:
        fichier = chemin_reservoirs + '/' + fichier
        nouveau_df = pd.DataFrame(pd.read_json(fichier))
        df = df.append(nouveau_df, ignore_index=True)
    return df


def charger_moteurs_df(chemin_moteurs: str) -> pd.DataFrame:
    '''
    Charge les moteurs contenus dans les fichiers moteur*.ppl dans un dataframe.
    
        Paramètres
            chemin_moteurs (str) : Une chaine de caractères du chemin vers le dossier moteurs
        
        Valeur de retour
            Type : pd.DataFrame
            Description : Le Dataframe combiné des moteurs
    '''
    # Retourne un dataframe combiné des moteurs décrits dans
    #  les fichiers FICHIERS_MOTEURS
    informations_fichiers = list()
    for fichier in FICHIERS_MOTEURS:
        fichier = chemin_moteurs + '/' + fichier
        informations_fichiers.append(ppl_to_dict(fichier))
    return pd.DataFrame(informations_fichiers)


def filtrer_moteurs(moteurs_df: pd.DataFrame, impulsion_minimum: int) -> pd.DataFrame:
    '''
    La fonction retourne un dataframe de moteurs filtré où l'impulsion 
    spécifique des éléments contenus est au-dessus d'un certain seuil.
        
        Paramètres
            moteurs_df (pd.DataFrame) : Le dataframe de moteurs à filtrer
            impulsion_minimum (int) : L'impulsion spécifique minimum désirée
            Valeur de retour
    
        Type : pd.DataFrame
            Description : Le Dataframe filtré de moteurs
    '''
    # Retourne un sous-ensemble filtré d'un df de moteurs
    #  où l'impulsion spécifique est au dessus d'un certain seuil
    return moteurs_df[moteurs_df['impulsion specifique'] > impulsion_minimum]


if __name__ == '__main__':
    # charger_capsules_df
    capsules = charger_capsules_df(CHEMIN_CAPSULES)
    print(capsules)
    print()

    # charger_reservoirs_df
    reservoirs = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    print(reservoirs)
    print()

    # charger_moteurs_df
    moteurs = charger_moteurs_df(CHEMIN_MOTEURS)
    print(moteurs)
    print()

    # filtrer_moteurs
    moteurs_filtres = filtrer_moteurs(moteurs, 220)
    print(moteurs_filtres)
