from abc import ABC
from typing import List

from animal import Animal


class Reptile(Animal, ABC):

    def __init__(self, nom : str, nb_pattes : int, est_nocturne : int) -> None:
        super().__init__(nom, nb_pattes)
        self.est_nocturne = est_nocturne

    def __str__(self) -> str:
        if self.est_nocturne:
            return f'Le {type(self).__name__} {self.nom} est nocturne.'
        else:
            return f'Le {type(self).__name__} {self.nom} est diurne.'


class Serpent(Reptile):

    def __init__(self, nom : str, est_nocturne : bool, est_venimeux: bool) -> None:
        super().__init__(nom, 0, est_nocturne)
        self.est_venimeux = est_venimeux

    def __str__(self) -> str:
        if self.est_venimeux:
            return super(Serpent, self).__str__() + " Il est venimeux."
        else:
            return super(Serpent, self).__str__() + " Il n'est pas venimeux."

    def crier(self) -> str:
        return 'sssss'
