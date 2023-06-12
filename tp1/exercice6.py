import matplotlib.pyplot as plt
import math
import numpy as np


def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)


def trouverModule(nombreComplexe):
    # Calcule le module du nombre complexe et l'assigne dans "module"
    module = math.sqrt(nombreComplexe.real ** 2 + nombreComplexe.imag ** 2)
    return module


def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)

    # Affiche le module et l'angle du nombre complexe (3 decimales de précision)
    print('Module = {:.3f}\nAngle = {:.3f}'.format(module, angle))

    # Calculer le nouveau nombre complexe après rotation, assigne le nouveau nombre complexe à la variable 'resultat'

    resultat = nombreComplexe * (math.cos(math.radians(angle_rotation)) + math.sin(math.radians(angle_rotation)) * 1j)

    nouveauModule = trouverModule(resultat)
    nouvelAngle = trouverAngle(resultat)

    # Affiche le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)
    print('Nouveau module = {:.3f}\nNouvel angle = {:.3f}'.format(nouveauModule, nouvelAngle))
    return resultat


def dessiner(number, label):
    ax = plt.subplot(projection='polar')
    if number != None:
        ax.plot([0, math.radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)


if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
