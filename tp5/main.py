from typing import Type
from animal import calcul_meilleur_animal
from elements_tiktok import FILTRE_FESTIF, MUSIQUE_SEPTEMBER, MUSIQUE_BEZOS_I, FILTRE_ETOILES, MUSIQUE_CHRISTMAS, \
    FILTRE_RALENTI
from mammifere import Chat, LongueurPoils
from oiseau import Cockatiel
from reptile import Serpent
from accessoire import Accessoire, TypeAccessoire
from tiktok import TikTok, CompteTikTok


def main() -> CompteTikTok:
    # Crée un objet Chat qui s'appelle Wako, avec 4 pattes à poils courts roux
    wako = Chat('Wako', LongueurPoils.COURTS, 'Roux')

    print(wako)


    # Crée un objet Serpent qui s'appelle Bob, qui est diurne et qui n'est pas venimeux
    bob = Serpent("Bob", est_nocturne=False, est_venimeux=False)

    print(bob)


    # Crée un objet Cockatiel qui s'appelle Cookie avec 2 pattes
    cookie = Cockatiel('Cookie', nb_pattes=2)

    print(cookie)


    # Crée un objet Accessoire de type chapeau avec un niveau de mignonnerie de 4
    chapeau = Accessoire('Béret', 4, TypeAccessoire.CHAPEAU)

    # Crée un objet Accessoire de type chaussures avec un niveau de mignonnerie de 6
    chaussures = Accessoire('Mocassins', 6, TypeAccessoire.CHAUSSURES)

    # Ajoute (+=) les chaussures à Wako
    wako += chaussures

    # Ajoute (+=) les chaussures à Bob
    bob += chaussures

    # Ajoute (+=) le chapeau à Bob
    bob += chapeau

    animaux = [wako, bob, cookie]
    # Dans une boucle, fait crier les animaux
    for animal in animaux:
        print(animal.crier())

    # Trouve quel animal est le meilleur
    meilleur_animal, score = calcul_meilleur_animal(animaux)
    print(f"L'animal le plus mignon est {meilleur_animal} avec un score de {score}")

    # Crée un compte TikTok avec l'identifiant "PolyAnimalerie"
    compte = CompteTikTok('PolyAnimalerie')

    # Crée un premier TikTok avec Wako et l'ajoute au compte
    #  Titre: "Wako est prêt pour Noël"
    #  Chanson: All I Want for Christmas is You
    #  Filtre: Ralenti
    tiktok1 = TikTok("Wako est prêt pour Noël")
    tiktok1.musique = MUSIQUE_CHRISTMAS
    tiktok1.filtre = FILTRE_RALENTI
    tiktok1.ajouter_animal(wako)
    compte += tiktok1

    # Crée un deuxième TikTok avec Bob et l'ajoute au compte
    #  Titre: "Bob porte un chapeau"
    #  Chanson: Bezos I
    #  Filtre: Étoiles
    tiktok2 = TikTok("Bob porte un chapeau")
    tiktok2.musique = MUSIQUE_BEZOS_I
    tiktok2.filtre = FILTRE_ETOILES
    tiktok2.ajouter_animal(bob)
    compte += tiktok2

    # Crée un troisième TikTok avec Wako et Cookie et l'ajoute au compte
    #  Titre: "Cookie chante à Wako qui ne veut rien savoir"
    #  Chanson: September
    #  Filtre: Festif
    tiktok3 = TikTok("Cooki chante à Wako qui ne veut rien savoir")
    tiktok3.musique = MUSIQUE_SEPTEMBER
    tiktok3.filtre = FILTRE_FESTIF
    tiktok3.ajouter_animal(wako)
    tiktok3.ajouter_animal(cookie)
    compte += tiktok3

    # Affiche le nombre de vues du troisième TikTok
    vues_tiktok_3 = tiktok3.vues
    print("Le troisième TikTok a", vues_tiktok_3, "vues")

    # Affiche le nombre de TikTok dans le compte
    nombre_tiktok_compte = len(compte)
    print("Le compte TikTok", compte.identifiant, "contient", nombre_tiktok_compte, "TikToks")

    # Affiche le nombre total de vues du compte
    vues_compte = compte.vues
    print("Le compte TikTok", compte.identifiant, "a", vues_compte, "vues")

    # Affiche la liste des TikTok en ordre de vues
    tiktoks_plus_populaires = compte.tiktoks_plus_populaires()
    print(tiktoks_plus_populaires)

    return compte


if __name__ == '__main__':
    compte = main()
    for tiktok in compte.tiktoks_plus_populaires():
        print(tiktok.to_json())
