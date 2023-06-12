import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # fait les calculs intermediaires.
    vitesseInitiale /= 3.6      # en m/s
    vitesseFinale /= 3.6        # en m/s
    acceleration = (vitesseFinale - vitesseInitiale) / duree

    # calcule la position finale
    positionFinale = positionInitiale + (vitesseInitiale * duree + 0.5 * acceleration * duree ** 2)

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
