def fizzBuzz(n):
    # Imprime la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    resultat = None
    if n % 3 == 0:
        resultat = 'fizz'
        if n % 5 == 0:
            resultat = 'fizzbuzz'
    elif n % 5 == 0:
        resultat = 'buzz'
    else:
        resultat = n
    return resultat


if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
