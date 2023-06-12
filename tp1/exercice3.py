
def decomposer(secondes):

    # Assigne à la variable "annees" le nombre d'années
    annees = secondes // (60 * 60 * 24 * 365)
    secondes %= 60 * 60 * 24 * 365

    # Assigne à la variable "semaines" le nombre de semaines restantes
    semaines = secondes // (60 * 60 * 24 * 7)
    secondes %= 60 * 60 * 24 * 7

    # Assigne à la variable "jours" le nombre de jours restants
    jours = secondes // (60 * 60 * 24)
    secondes %= 60 * 60 * 24

    # Assigne à la variable "heures" le nombre d'heures restantes
    heures = secondes // (60 * 60)
    secondes %= 60 * 60

    # Assigne à la variable "minute" le nombre de minutes restantes
    minutes = secondes // 60

    # Assigne à la variable "secondes" le nombre de secondes restantes
    secondes %= 60

    # Affiche le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
