# TP2

#### :alarm_clock: [Date de remise le dimanche 10 octobre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20211010T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif
Ce TP poursuit votre apprentissage de l'algorithmie avec le langage de programmation Python.
Plus particulièrement l'utilisation de structure de contrôles et de structure de données.  
Celui-ci est composé de 4 exercices, pour lesquels vous devez compléter le code avec l'indicateur `TODO`.
Les exercices sont tous indépendants, l'exercice 4 est composé de 3 parties.

## Consignes à respecter
Tout d'abord, assurez-vous d'avoir lu le fichier [instructions.md](instructions.md) et d'avoir téléchargé les exercices1-4.py que vous devrez compléter.  
Pour ce TP, vous ne pouvez pas importer d'autres librairies que celles qui sont déjà importées dans les fichiers.

## Exercice 1 (3 points):
Dans cet exercice, vous devez écrire un programme qui combine deux dictionnaires dans un 3e dictionnaire en gardant la valeur maximale des clés communes.  
**Exemple :**
```python
dic_1 = {'a': 5, 'b': 2, 'c':9}
dic_2 = {'a': 1, 'b': 8, 'd':17}
dic_3 = {'a': 5, 'b': 8, 'd': 17, 'c': 9}
```

## Exercice 2 (3 points):
Lors de la manipulation de liste il est commun de vouloir trier les valeurs qui la compose.
Pour ce faire nous allons implémenter un algorithme de tri appelé tri à bulle. Il s'agit d'un algorithme peu efficace, mais facile à implémenter.  
**Le pseudo-code de l'algorithme est le suivant :**
```
tri_à_bulles(Tableau T)
   pour i allant de (taille de T)-1 à 1
       pour j allant de 0 à i-1
           si T[j+1] < T[j]
               on inverse les valeurs
```
**Une animation qui représente le fonctionnement de l'algorithme :**  
<img align="center" src="img/Sorting_bubblesort_anim.gif"/>  
Nous ferons un tri par ordre croissant ce qui donnera : 
```python
val = [5,8,1,9,6,2,4,3,7,5]
sorted_val = [1,2,3,4,5,5,6,7,8,9]
```
**ATTENTION** Un *pseudo-code* est une façon de décrire un algorithme qui ne prend pas en compte les spécificités du language.
Mais dans le cas présent les tableaux sont quand même considérés comme commençant à 0.

## Exercice 3 (4 points):
Nous voulons réaliser un programme estimant la valeur du nombre π. Pour cela, nous utilisons la formule suivante :  
<img align="center" src="img/formule_pi.png"/>  
Cette formule permet une estimation précise de π pour un nombre d’itérations n suffisamment grand.
Vous devez compléter la fonction `compute_pi(p)` où p est la précision que l'on veut.  
Dès que l'écart entre 2 valeurs successives est inférieur à la précision on s'arrête.
Le programme met normalement moins d'une seconde à s'exécuter. 

## Exercice 4 :
Le but de cet exercice est de programmer un petit jeu de labyrinthe dans lequel on guide le joueur jusqu'à la sortie. Le joueur peut se déplacer dans toutes les directions mais il ne peut pas sortir du labyrinthe ou passer à travers les murs, ce n'est pas un fantôme.    
Toutes les fonctions vous sont fournies, il vous faut seulement compléter les diverses parties identifiées par un `TODO`.  
Le labyrinthe que l'on va représenter est le suivant :  
<img align="center" src="img/grille.png"/>  
Cependant comme nous allons afficher le labyrinthe dans le terminal, notre affichage est simplifié et ressemblera à cela :  
<img align="center" src="img/terminal.png"/>  
- O : le joueur
- X : la sortie
- W : un mur
- _ : une case libre

**ATTENTION** Pour la correction une autre définition du labyrinthe sera utilisée, donc votre code devra pouvoir s'adapter.

### Partie 1 : Génaration du labyrinthe (3 points)
Il vous faut compléter la fonction `init_maze` pour ce faire nous avons :
- la dimension du labyrinthe
- la position du joueur
- la position de la sortie
- une liste de position de mur 

Il faut également compléter le début du `main` pour définir la position du joueur comme étant le coin en haut à gauche et la sortie comme étant en bas à droite.
Voir l'image ci-dessus.

### Partie 2 : Vérification d'un mouvement (3 points)
Dans cette partie on va compléter la fonction `validate_move`, pour cette fonction nous avons *maze* qui correspond au labyrinthe générer à la question d'avant et *new_player_pos*.
qui correspond à une nouvelle position que le joueur serait sur le point de prendre.  
L'objectif ici est de compléter la fonction pour que l'on renvoie *True* si *new_player_pos* est valide, c'est à dire dans le labyrinthe et pas sur un mur. 
Sinon on renverra *False*.

### Partie 3 : Faire un mouvement (4 points)
Dans cette dernière partie nous allons compléter la fonction `move`, Dans un premier temps à l'aide d'un dictionnaire
il faut convertir l'entré *input* en sa direction correspondante. On s'attend à avoir :
- w -> up
- a -> left 
- s -> down
- d -> right

Il faut ensuite vérifier si l'entrée est valide, puis en fonction de la direction générer une nouvelle position potentielle pour le joueur.  
Enfin si le mouvement est valide on change la position du joueur dans le labyrinthe.
