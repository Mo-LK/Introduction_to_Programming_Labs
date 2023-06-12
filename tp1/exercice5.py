def pointDeRencontre(v1, v2, distance):
    # fais les calculs intermediaires
    position_initiale1 = 0
    position_initiale2 = distance
    v2 = - v2

    # calcule la position de rencontre
    positionRencontre = ((- v1 * position_initiale2) + (v2 * position_initiale1)) / (v2 - v1)

    return positionRencontre


if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
