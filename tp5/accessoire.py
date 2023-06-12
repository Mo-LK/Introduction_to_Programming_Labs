from enum import Enum

from elements_tiktok import ElementViral


class TypeAccessoire(Enum):
    CHAPEAU = 1.5
    CHAUSSURES = 1.2
    BIJOU = 0.8
    VETEMENT = 1

    def __str__(self):
        return self.name


class Accessoire(ElementViral):

    def __init__(self, nom : str, niveau_mignonnerie : int, type_accessoire : TypeAccessoire) -> None:
        self.nom = nom
        self.niveau_mignonnerie = niveau_mignonnerie
        self.type_accessoire = type_accessoire

    def __str__(self) -> str:
        return  f'type : {self.type_accessoire}, nom : {self.nom}, '\
                + f'niveau de mignonnerie : {self.niveau_mignonnerie}'

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    def score_viral(self) -> int:
        return int(self.niveau_mignonnerie * self.type_accessoire.value * 10_000)
