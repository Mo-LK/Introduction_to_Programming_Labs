import math

from constantes import MASSE_VOLUMIQUE_CARBURANT, CHAMP_GRAVITATIONNEL


class Piece:
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float) -> None:
        self.nom = nom
        self.hauteur = hauteur  # En m
        self.masse = masse  # En kg
        self.prix = prix  # En $CAN

    def __str__(self) -> str:
        return f"{self.nom}, hauteur={self.hauteur}m, masse={self.masse}kg, prix={self.prix}$"


class Capsule(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, places: int) -> None:
        super().__init__(nom, hauteur, masse, prix)

        self.places = places  # En personnes

    def __str__(self) -> str:
        return f"Capsule: {super().__str__()}, places={self.places} personne(s)"


class Reservoir(Piece):
    def __init__(self, nom: str, hauteur: float, masse_vide: float, prix: float, capacite: float) -> None:
        super().__init__(nom, hauteur, masse_vide, prix)

        self.capacite = capacite  # En litres

    def __str__(self) -> str:
        return f"Réservoir: {super().__str__()}, capacité={self.capacite}L"

    @property
    def masse_rempli(self) -> float:
        '''
        Retourne la masse du réservoir rempli de carburant.

            Paramètres
                self (Reservoir) : Une référence au réservoir duquel la masse remplie doit être calculée
            
            Valeur de retour
                Type : float
                Description : La masse du réservoir rempli de carburant
        '''
        # Calcule la masse du réservoir rempli.
        return self.capacite * MASSE_VOLUMIQUE_CARBURANT + self.masse


class Moteur(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, impulsion_specifique: int) -> None:
        super().__init__(nom, hauteur, masse, prix)

        self.impulsion_specifique = impulsion_specifique  # En secondes

    def __str__(self) -> str:
        return f"Moteur: {super().__str__()}, impulsion spécifique={self.impulsion_specifique}s"


class Fusee:
    """
    La classe représentant une fusée simple.

    Une fusée a comme attributs publics:
    * Un nom

    Une fusée a comme attributs privés:
    * Une capsule
    * Un réservoir
    * Un moteur
    """
    
    def __init__(self, nom: str, capsule: Capsule, reservoir: Reservoir, moteur: Moteur) -> None:
        '''
        Constructeur de la fusée.

            Paramètres
                nom (str) : Le nom de la fusée
                capsule (Capsule) : La capsule à assembler dans votre fusée
                reservoir (Reservoir) : Le réservoir à assembler dans votre fusée
                moteur (Moteur) : Le moteur à assembler dans votre fusée
            
            Valeur de retour
                Aucune
        '''
        self.nom = nom
        self.__capsule = capsule
        self.__reservoir = reservoir
        self.__moteur = moteur

    def __str__(self) -> str:
        '''
        Retourne la représentation en str d'un objet Fusee.

            Paramètres
                self (Fusee) : Une référence à la fusée à représenter en str
        
            Valeur de retour
                Type : str
                Description : La représentation en str de l'objet Fusee.
        '''
        # Permet l'affichage de la fusée
        return f'Fusée:\n\tNom: {self.nom}\n\tHauteur totale: {self.hauteur}m\n\t' \
                + f'Masse totale (remplie): {self.masse}kg\n\tPrix total: {self.prix}$\n' \
                + f'Pièces:\n\t{self.__capsule.__str__()}\n\t{self.__reservoir.__str__()}\n\t' \
                + f'{self.__moteur.__str__()}'

    @property
    def masse(self) -> float:
        '''
        Retourne la masse totale d'un objet Fusee.

            Paramètres
                self (Fusee) : Une référence à la fusée
        
            Valeur de retour
                Type : float
                Description : La masse totale de l'objet Fusee
        '''
        # Calcule la masse totale de la fusée (incluant le carburant)
        return self.__reservoir.masse_rempli + self.__moteur.masse + self.__capsule.masse

    @property
    def hauteur(self) -> float:
        '''
        Retourne la hauteur totale d'un objet Fusee.

            Paramètres
                self (Fusee) : Une référence à la fusée
            
            Valeur de retour
                Type : float
                Description : La hauteur totale de l'objet Fusee
        '''
        # Calcule la hauteur totale de la fusée
        return self.__reservoir.hauteur + self.__capsule.hauteur + self.__moteur.hauteur

    @property
    def prix(self) -> float:
        '''
        Retourne le prix total d'un objet Fusee.

            Paramètres
                self (Fusee) : Une référence à la fusée
        
            Valeur de retour
                Type : float
                Description : Le prix total de l'objet Fusee
        '''
        # Calcule le prix total de la fusée
        return self.__reservoir.prix + self.__capsule.prix + self.__moteur.prix

    def calculer_deltav(self) -> float:
        '''
        Retourne le deltaV d'un objet Fusee
            
            Paramètres
                self (Fusee) : Une référence à la fusée
            
            Valeur de retour
                Type : float
                Description : Le deltaV de l'objet Fusee
        '''
        # À partir de la masse, du moteur et du réservoir,
        #  calcule le deltaV disponible de la fusée dans l'atmosphère
        Isp = self.__moteur.impulsion_specifique
        m_rempli = self.masse
        m_vide = self.__capsule.masse + self.__moteur.masse + self.__reservoir.masse
        log = math.log(m_rempli / m_vide)
        return Isp * CHAMP_GRAVITATIONNEL * log


if __name__ == '__main__':
    # Reservoir.masse_rempli
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    masse_rempli = reservoir.masse_rempli
    print(f"Une fois rempli, {reservoir.nom} a une masse de {masse_rempli} kg")
    print()

    # Fusee constructeur
    capsule = Capsule("Exigüe", 1.0, 750, 1300.0, 1)
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20.0, 2)
    moteur = Moteur("Pantera Arctic Cat Triple 800", 4, 2000, 14000.0, 199)
    fusee = Fusee("Romano Fafard", capsule, reservoir, moteur)

    # Fusee.masse
    print(f"La masse de la fusée {fusee.nom} est {fusee.masse}kg")
    print()

    # Fusee.hauteur
    print(f"La hauteur de la fusée {fusee.nom} est {fusee.hauteur}m")
    print()

    # Fusee.prix
    print(f"Le prix de la fusée {fusee.nom} est {fusee.prix}$")
    print()

    # Fusee.__str__
    print(f"fusee est de type {type(fusee)}")
    print()
