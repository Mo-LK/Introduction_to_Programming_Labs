import math


def resoudreEquation(a, b, c):
    # Calcule le discriminant et assigne la valeur dans la variable "delta"
    delta = ((b ** 2) - (4 * a * c))

    # Déterminee la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
    naPasDeSolution = (delta < 0)

    if naPasDeSolution:
        # ces ligne de code seront executé si il y'a aucune racine
        # affiche sur l'écran "Aucune racine"
        print('Aucune racine')
        # ne pas modifier
        return None

    # Détermine la condition (bool) qui correspond à une unique solution de l'équation et met la valeur dans "aUneSeuleSolution"
    aUneSeuleSolution = (delta == 0)

    if aUneSeuleSolution:
        # ces ligne de code seront executé si il y'a une seule racine
        # affiche sur l'écran "Une seule racine"
        print('Une seule racine')
        # assigne a la variable x1 la valeur de la racine
        x1 = delta
        # ne pas modifier
        return x1

    # Détermine la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    aDeuxSolutions = (delta > 0)

    if aDeuxSolutions:
        # affiche sur l'écran "Deux racines"
        print('Deux racines')
        # calcule la premiere racine, assigner la à "x1"
        x1 = (-b + math.sqrt(delta)) / (2 * a)

        # calcule la deuxieme racine, assigner la a "x2"
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        # ne pas modifier cette ligne
        return x1, x2


if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

    print(resoudreEquation(a, b, c))
