from typing import Tuple

from assemblage import creer_capsules, creer_reservoirs, creer_moteurs, corps_celestes_accessibles, comparer_fusee
from constantes import IMPULSION_SPECIFIQUE_MINIMALE, CHEMIN_CAPSULES, CHEMIN_RESERVOIRS, CHEMIN_MOTEURS
from fichiers_pieces import charger_capsules_df, charger_reservoirs_df, charger_moteurs_df, filtrer_moteurs
from fusee import Fusee


def main() -> Tuple[Fusee, Fusee]:
    '''
    Fonction principale du programme.
    
        Paramètres:
            Aucun
        
        Valeur de retour
            Type : Tuple[Fusee, Fusee]
            Description : Un tuple des deux fusées créées par l'utilisateur'''
    
    # Pièces
    # Chargement des pièces
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)

    # Filtre les moteurs avec une impulsion spécifique plus
    #  petite que IMPULSION_SPECIFIQUE_MINIMALE
    moteurs_filtres = filtrer_moteurs(moteurs_df, IMPULSION_SPECIFIQUE_MINIMALE)

    # Affiche les trois dataframes
    print('Capsules :')
    print(capsules_df)
    print('\n\nRéservoirs :')
    print(reservoirs_df)
    print('\n\nMoteurs :')
    print(moteurs_filtres)

    # Assemblage
    # Crée des objets de type Capsule, Reservoir et Moteur
    #  à partir des dataframes
    capsules = creer_capsules(capsules_df)
    reservoirs = creer_reservoirs(reservoirs_df)
    moteurs = creer_moteurs(moteurs_filtres)

    # Crée deux fusées
    fusees = []
    for i in range(2):
        nom_fusee = input("Veuillez entrer le nom de la fusée : ")
        index_capsule = int(input("Veuillez entrer le numéro de la capsule désirée : "))
        index_reservoir = int(input("Veuillez entrer le numéro du réservoir désiré : "))
        index_moteur = int(input("Veuillez entrer le numéro du moteur désiré : "))
        # Crée une fusée à partir des pièces choisies et l'ajoute à la liste fusees
        fusees.append(Fusee(nom_fusee, capsules[index_capsule], 
                            reservoirs[index_reservoir], moteurs[index_moteur]))
        # Affiche la fusée
        print(fusees[-1])

    # Comparaison
    # Affiche les corps célestes accessibles par les deux fusées
    corps_accessibles_fusee_1 = corps_celestes_accessibles(fusees[0])
    corps_accessibles_fusee_2 = corps_celestes_accessibles(fusees[1])
    print(f"Fusée 1 ({fusees[0].nom}) peut aller jusqu'à {','.join(corps_accessibles_fusee_1)}")
    print(f"Fusée 2 ({fusees[1].nom}) peut aller jusqu'à {','.join(corps_accessibles_fusee_2)}")

    # Crée et affiche le graphique de comparaison des deux fusées
    comparer_fusee(fusees[0], fusees[1])
    return fusees[0], fusees[1]


if __name__ == '__main__':
    main()
