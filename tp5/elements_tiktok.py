from abc import ABC, abstractmethod


class ElementViral(ABC):

    @abstractmethod
    def score_viral(self) -> int:
        pass


class Musique(ElementViral):

    def __init__(self, titre: str, nb_ecoutes: int) -> None:
        self.titre = titre
        self.nb_ecoutes = nb_ecoutes

    def score_viral(self) -> int:
        return int(self.nb_ecoutes / 10_000)


class Filtre(ElementViral):

    def __init__(self, nom: str, nb_utilisations: int) -> None:
        self.nom = nom
        self.nb_utilisations = nb_utilisations

    def score_viral(self) -> int:
        return int(self.nb_utilisations / 50_000)


FILTRE_RALENTI = Filtre("Ralenti", 50000000)
FILTRE_ETOILES = Filtre("Étoiles", 500000)
FILTRE_FESTIF = Filtre("Festif", 1000000)

MUSIQUE_CHRISTMAS = Musique("All I Want for Christmas is You", 934220516)
MUSIQUE_BEZOS_I = Musique("Bezos I", 95610379)
MUSIQUE_SEPTEMBER = Musique("September", 941627159)
