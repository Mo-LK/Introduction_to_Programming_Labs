import json
from typing import List, Union

from animal import Animal
from elements_tiktok import Musique, Filtre


class TikTok:

    def __init__(self, titre : str) -> None:
        self.titre = titre
        self.__animaux = []
        self.musique = None
        self.filtre = None

    def ajouter_animal(self, animal: Animal) -> 'TikTok':
        # Ajoute l'animal à la liste et retourne le TikTok mis à jour
        self.__animaux.append(animal)
        return self

    def __lt__(self, autre_tiktok: 'TikTok') -> bool:
        # Surcharge l'opérateur < entre deux objets de type TikToks
        return self.vues < autre_tiktok.vues

    def __str__(self) -> str:
        # Retourne une chaine de caractère semblable à :
        #  TITRE (NOMBRE_DE_VUES vues)
        return f'{self.titre} ({self.vues} vues)'

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    @property
    def vues(self) -> int:
        # Retourne le nombre de vues du TikTok
        return self.musique.score_viral() + self.filtre.score_viral() \
                + len(self.__animaux) * sum([a.score_viral() for a in self.__animaux])

    def to_json(self):
        # Ne pas modifier
        return json.dumps({
            'titre': self.titre,
            'vues': self.vues,
            'musique': self.musique.titre,
            'filtre': self.filtre.nom,
            'animaux': [
                {
                    'nom': animal.nom,
                    'espèce': type(animal).__name__,
                    'accessoires': [
                        {
                            'nom': accessoire.nom,
                            'type': str(accessoire.type_accessoire)
                        } for accessoire in animal.liste_accessoires
                    ]
                } for animal in self.__animaux
            ]
        }, ensure_ascii=False)


class CompteTikTok:

    def __init__(self, identifiant : str) -> None:
        self.identifiant = identifiant
        self.__tiktoks = []

    def __len__(self) -> int:
        # Surcharge l'opérateur len pour que len(COMPTE_TIKTOK) retourne le nombre de tiktok du compte
        return len(self.__tiktoks)

    def __iadd__(self, tiktok: TikTok) -> 'CompteTikTok':
        # Surcharge l'opérateur += pour permettre d'ajouter un TikTok à la liste du compte
        self.__tiktoks.append(tiktok)
        return self

    @property
    def vues(self) -> int:
        # Retourne le nombre de vues cumulatives du compte c'est à dire la somme des vues des différents TikToks
        return sum([tiktok.vues for tiktok in self.__tiktoks])

    def tiktoks_plus_populaires(self) -> List[TikTok]:
        # Retourne une liste triée des TikToks du compte en ordre décroissant de vues
        return sorted(self.__tiktoks, reverse=True)
