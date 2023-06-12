from abc import ABC
from enum import Enum
from typing import List

from animal import Animal


class LongueurPoils(Enum):
    RASES = 0
    COURTS = 1
    LONGS = 2

    def __str__(self):
        return self.name


class Mammifere(Animal, ABC):

    def __init__(self, nom, nb_pattes, longueur_poils) -> None:
        super().__init__(nom, nb_pattes)
        self.longueur_poils = longueur_poils

    def __str__(self) -> str:
        return f'Le {type(self).__name__} {self.nom} a {self.nb_pattes} pattes '\
                + f'et des poils {self.longueur_poils}.'


class Chat(Mammifere):

    def __init__(self, nom, longueur_poils, couleur, nb_pattes=4):
        super().__init__(nom, nb_pattes, longueur_poils)
        self.couleur = couleur

    def crier(self) -> str:
        return 'Miaou'
