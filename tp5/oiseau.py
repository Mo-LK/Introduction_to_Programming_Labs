from abc import ABC
from typing import List

from animal import Animal


class Oiseau(Animal, ABC):

    def __init__(self, nom : str, nb_pattes : int, chante : bool) -> None:
        super().__init__(nom, nb_pattes)
        self.chante = chante

    def __str__(self) -> str:
        if self.chante:
            return f'Le {type(self).__name__} {self.nom} chante.'
        else:
            return f'Le {type(self).__name__} {self.nom} ne chante pas.'

    def crier(self) -> str:
        if self.chante:
            return 'Ba de ya, say that you remember. Ba de ya, dancing in September.'
        else:
            return 'cuicui'


class Cockatiel(Oiseau):

    def __init__(self, nom, nb_pattes):
        super().__init__(nom, nb_pattes, chante=True)
