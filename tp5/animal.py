from abc import abstractmethod, ABC
from typing import List, Tuple, Type

from accessoire import Accessoire, TypeAccessoire
from elements_tiktok import ElementViral


class Animal(ElementViral, ABC):

    def __init__(self, nom : str, nb_pattes : int) -> None:
        self.nom = nom
        self.nb_pattes = nb_pattes
        self.liste_accessoires = []

    def __add__(self, accessoire: Accessoire) -> int:
        return self.score_viral() + accessoire.score_viral()

    def __iadd__(self, accessoire: Accessoire) -> 'Animal':
        if accessoire.type_accessoire == TypeAccessoire.CHAUSSURES and self.nb_pattes == 0:
            print('Vous ne pouvez pas mettre de chaussures à un animal sans pieds')
        else:
            self.liste_accessoires.append(accessoire)
        return self

    @abstractmethod
    def crier(self) -> str:
        pass

    def score_viral(self) -> int:
        return sum([accessoire.score_viral() for accessoire in self.liste_accessoires])

def calcul_meilleur_animal(animaux: List[Animal]) -> Tuple[str, int]:
    meilleur_animal = max(animaux, key=lambda a: a.score_viral())
    return meilleur_animal.nom, meilleur_animal.score_viral()
