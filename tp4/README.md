# TP4: Bibliothèques scientifiques et graphiques | Tests et outils de correction

- [Directives particulières](#directives-particuli%C3%A8res)
- [Objectifs](#objectifs)
- [Partie 1: Exploration de la base de données](#partie-1-Lire-et-construire-la-base-de-donn%C3%A9es)
- [Partie 2: Affichage graphique des données](#partie-2-analyse-des-donn%C3%A9es)
- [Partie 3: Rédaction des tests](#partie-3-rédactions-des-tests)

:alarm_clock: [Date de remise le dimanche 14 novembre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20210406T2359&p0=165&font=cursive)

## Directives particulières
* Un fichier TP4.ipynb sera utilisé;
* Il suffit de faire un 'pip install jupyter' puis de rajouter jupyter sur pycharm afin de l'ouvrir, les jupyter notebook sont intéressants pour leur affichage rapide et vous familiariserons avec un outil communément utilisé; Afin de l'utiliser directement sur pycharm, il faut avoir la version pro, vous pouvez l'installer via votre courriel de Polytechnique en cliquant [ici](https://www.jetbrains.com/shop/eform/students). Pour ceux avec visual studio code, la version gratuite offre déjà le plugin jupyter que vous pouvez installer gratuitement.
* N'oubliez pas également d'installer les librairies manquantes (seaborn, numpy et pandas) via anaconda ou directement via pycharm; 
* Pas de librairies externes autres que celles déjà importées.

## Objectifs
Le TP4 se concentre sur l'utilisation de librairies scientifiques et graphiques. Plus précisément, vous aurez à vous familiariser avec numpy et pandas, des librairies essentielles en python en plus de visualiser certaines données avec matplotlib et seaborn. Exceptionnellement, les étapes à suivre pour les parties 1 et 2 seront expliquées entièrement dans le jupyter notebook nommé TP4.ipynb. Pour ce qui est de la partie 3 sur la rédaction de tests, un élément important lors de la réalisation de projet en programmation, les instructions sont ci-dessous.

## Partie 3: Rédactions des tests
Il est primordial de tester extensivement le code écrit. Toutefois, cette pratique est souvent mise de côté par manque de temps ou d'envie. Elle demeure néanmoins une bonne habitude à entreprendre pour vos futurs projets en tant qu'ingénieur en informatique/logiciel.

Pour votre première rédaction de tests, vous allez vous inspirer de codes déjà rédigés auparavant lors du TP1. Les codes en question sont les suivants. Ils sont aussi disponibles dans le fichier *fonctions_a_tester.py*.

```python
# Fonction fizzBuzz 
def fizz_buzz(nombre: int) -> str:
    result = str(nombre)

    if nombre % 3 == 0 and nombre % 5 == 0:
        result = "fizzbuzz"
    elif nombre % 3 == 0:
        result = "fizz"
    elif nombre % 5 == 0:
        result = "buzz"

    return result

#Fonction CalculerPosition
def resoudre_equation(a: int, b: int, c: int) -> Union[None, float, Tuple[float, float]]:
    delta = b ** 2 - 4 * a * c

    na_pas_de_solution = delta < 0

    if na_pas_de_solution:
        return None

    a_une_seule_solution = delta == 0

    if a_une_seule_solution:
        racine_1 = (-b + math.sqrt(delta)) / (2 * a)
        return racine_1

    a_deux_solutions = delta > 0

    if a_deux_solutions:
        racine_1 = (-b + math.sqrt(delta)) / (2 * a)
        racine_2 = (-b - math.sqrt(delta)) / (2 * a)
        return racine_1, racine_2
```

Le fichier *tests.py* est celui que vous devez compléter afin de réaliser les tests en question et vous assurez que les fonctions fizz_buzz() et resoudre_equation() implémentées ci-haut sont belles et bien fonctionnelles. Pour ce faire, il vous suffit de compléter quelques cas de tests pour ces deux fonctions. N'oubliez pas que vous pouvez toujours reconsulter les nombreux fichiers de test_assignment que vous possédez des anciens TP et projets.

## Barème

| Question |  Points  |  
|----------|----------|
| 1.1      | 2        | 
| 1.2      | 4        | 
| 2.1      | 1        | 
| 2.2      | 4        | 
| 3        | 3        | 
| 4        | 4        | 
| Partie 3 | 2        | 



