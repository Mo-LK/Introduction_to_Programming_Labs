<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Polytechnique_Montr%C3%A9al_logo.jpg" />
</p>

# TP3: Fonctions, lecture et écriture de fichiers
- [Directives particulières](#directives)
- [Énoncé de travail](#enonce)
- [Concepts](#concepts)
  - [L’algorithme de Dijkstra](#djikstra)  
  - [Représentation de graphe sous forme de matrice adjacente](#representation)
  - [Calcul de plus court chemin dans une carte topographique](#calcul)
- [Modules à implémenter](#module)
  - [Module algo](#algo) 
  - [Module carte](#carte)
  - [Module fichier](#fichier)
  - [Module interface](#interface)
  - [Module principale](#principale)
- [Barème](#bareme)
- [Annexe: Guide et normes de codage](#annexe)

:alarm_clock: [Date de remise le Dimanche 31 Octobre 23h59][0]

## Directives particulières <a name="directives"></a>
* Respecter [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Noms de variables et fonctions adéquats (concis, compréhensibles);  
* Pas de librairies externes autres que celles déjà importées;  
* Dans chaque programme, vous pouvez ajouter d’autres fonctions à celles décrites dans l’énoncé pour améliorer la lisibilité.

## 1. Énoncé de travail <a name="enonce"></a>
<p align='justify'> Dans le cadre de ce laboratoire, vous devrez réaliser un programme qui permet de trouver le plus court chemin dans un graphe. Il existe plusieurs algorithmes qui permettent de déterminer le plus court chemin dans un graphe. Dans le cadre de ce laboratoire, nous avons choisi d’implémenter l’algorithme de Dijkstra. </p>

Le travail demandé consiste à :
* Implémenter l’Algorithme de Dijkstra (un pseudo-code est fourni dans la section 2.1).
* Programmer les fonctionnalités nécessaires pour valider les données.
* Programmer un menu principal qui permet à l’usager de choisir parmi les fonctionnalités suivantes :
  1. <p align='justify'>Trouver le plus court chemin dans un graphe saisi par l’utilisateur. L’utilisateur doit saisir la matrice d’adjacente (le nombre des nœuds et les poids des arcs) ainsi que le nœud de départ et le nœud d’arrivée.</p>
  2.  <p align='justify'>Trouver le plus court chemin dans un graphe généré aléatoirement : l’utilisateur saisit le nombre le nœud, ensuite la matrice et généré avec des poids d’arcs aléatoires. La matrice d’adjacente est affichée et l’utilisateur est invité à saisir le nœud de départ et le nœud d’arrivée.</p>
  3.  <p align='justify'>Trouver le plus court chemin dans une carte topographique. Votre programme doit être capable de lire un fichier d’un modèle numérique de terrain. Ensuite, transformer le  modèle en une matrice d’adjacente et l’afficher. L’utilisateur choisit par la suite le nœud de départ et le nœud d’arrivée. Votre programme doit afficher la distance du plus court chemin et afficher le chemin. </p>

Dans ce qui suit, nous expliquons les différents concepts.

## 2. Concepts <a name="concepts"></a>
<p align='justify'> Un graphe est un ensemble de points appelés *nœuds* et de segments appelés *arcs*. Ces arcs peuvent être pondérés en termes de *poids* pour représenter le coût ou la distance entre les nœuds. Un graphe peut servir à représenter un réseau informatique, un réseau de transport, une carte topographique (voir figure 1).</p>



<p align="center"> 
  <img src="Img/Fig_01.PNG"> 
    <br>
    <em><b>Fig. 1 : Exemple de graphe pondéré.</b></em>
</p>

<p align='justify'> On définit un chemin dans un graphe pondéré comme une suite de nœuds reliés deux à deux par des arcs et le poids d’un chemin comme la somme des poids des arcs de cette suite (voir figure 2).</p>

<p align="center">
  <img src="Img/Fig_02.PNG" alt> 
    <br>
    <em><b>Fig. 2 : Chemin 1,3,6,5 de poids total égal à 20.</b></em>
</p>

<p align='justify'> L’algorithme de Dijkstra permet de résoudre le problème suivant : étant donné un graphe pondéré, un nœud de départ et un nœud d’arrivée, trouver le chemin le plus court allant du nœud départ au nœud d’arrivée.</p>

### 2.1. L’algorithme de Dijkstra <a name="djikstra"></a>
<p align='justify'> On donne ci-dessous l’algorithme de Dijkstra en *pseudo-code* permettant de déterminer la distance mini- male d’un nœud de départ à un nœud d’arrivée.</p>

<p align="center">
  <img src="Img/Algo_01.PNG" alt>
</p>

<p align='justify'> Les figures de 3 à 8 montrent l’application de l’algorithme de Dijkstra sur le graphe de la figure 1 pour trouver le plus court chemin pour aller du nœud de départ <b>1</b> au nœud d’arrivée <b>5</b> et montrent le contenu des différents tableaux utilisés dans l’algorithme à chaque itération. Les nœuds en <b>gris</b> sont les nœuds déjà visités et le nœud en <b>rouge</b> est le nœud en cours de visite qui sera ajoutée aux nœuds visités. </p>
  
<p align='justify'>Le tableau ”<b>distanceMin</b>” initialisé à des −1 qui seront remplacés par des distances au fur et aux mesures par que l’algorithme avance. À la fin de l’exécution de l’algorithme, ce tableau contient les distances minimales qui séparent chaque nœud au nœud de départ - entre autres le nœud d’arrivée. </p>
  
<p align='justify'>De même le tableau des prédécesseurs est initialisé à des −1 qui seront remplacés par le prédécesseur de chaque nœud dans le plus court chemin qui le sépare du nœud de départ.</p>

<p align="center">
  <img src="Img/Fig_03.PNG" alt>
    <br>
    <em><b>Fig. 3 : Initialisation.</b></em>
</p>

<p align='justify'>  Le premier nœud à visiter est le nœud de départ (1) (voir figure 4), on calcule les distances des voisins et on met à jour les tableaux. Le nœud (1) est par la suite ajouté à l’ensemble des nœuds visités.</p>

<p align="center">
  <img src="Img/Fig_04.PNG" alt>
    <br>
    <em><b>Fig. 4 : Visite du nœud 1.</b></em>
</p>

<p align='justify'>  Le nœud non visité qui a la distance la plus petite dans le tableau *Distancement* est le nœud (2). Par la suite, il devient le nœud suivant à visiter (figure 5). Et ainsi de suite (voir les figures 6 et 7).</p>

<p align="center">
  <img src="Img/Fig_05.PNG" alt>
    <br>
    <em><b>Fig. 5 : Visite du nœud 2.</b></em>
</p>

<p align="center">
  <img src="Img/Fig_06.PNG" alt>
    <br>
    <em><b>Fig. 6 : Visite du nœud 3</b></em>
</p>

<p align="center">
  <img src="Img/Fig_07.PNG" alt>
    <br>
    <em><b>Fig. 7 : Visite du nœud 6.</b></em>
</p>

<p align='justify'> Le nœud suivant à visiter après le nœud (6) est le nœud (5) qui est le nœud d’arrivée. À ce stade, l’algorithme s’arrête. Pour trouver le plus court chemin entre le nœud de départ et le nœud d’arrivée, on utilise le tableau des prédécesseurs. On prend le prédécesseur du nœud d’arrivée, dans notre exemple le prédécesseur du nœud d’arrivée (5) est le nœud (6), le prédécesseur du nœud (6) est le nœud (3), ainsi de suite jusqu’à atteindre le nœud de départ (1). Le plus court chemin entre le nœud (1) et (5) est (1) => (3) => (6) => (5) ayant comme distance la somme des poids des arcs qui vaut 20.</p>

<p align="center">
  <img src="Img/Fig_08.PNG" alt>
    <br>
    <em><b>Fig. 8 : Le plus court chemin pour aller de 1 à 5 est 1,3,6,5 le poids total est 20.</b></em>
</p>


### 2.2.Représentation de graphe sous forme de matrice adjacente <a name="representation"></a> 
<p align='justify'>On peut considérer que le graphe comporte N nœuds numérotés de 1 à N, et représenter ses arcs par un tableau de nombres de deux dimensions N x N, de sorte que si l’élément [i, j] du tableau vaut −1, il n’existe pas d’arc allant du nœud i au nœud j, et s’il est positif, il existe un tel arc et sa longueur est donnée par ce nombre.</p>

<p align='justify'> Ce tableau de deux dimensions forme la matrice d’adjacente qui représente le graphe ; c’est une matrice symétrique. La figure 9 représente la transformation du graphe de l’exemple précédent en une matrice d’adjacente.</p>


<p align="center">
  <img src="Img/Tab_01.PNG" alt>
    <br>
    <em><b>Fig. 9 : Transformation du graphe de la figure 1 en une matrice d’adjacente.</b></em>
</p>


### 2.3. Calcul de plus court chemin dans une carte topographique <a name="calcul"></a>
<p align='justify'>Une carte topographique est une carte à échelle réduite représentant le relief déterminé par les altitudes (l’altimétrie et les aménagements humains) d’une région géographique de manière précise et détaillée sur un plan horizontal. Les données d’altitude d’une carte topographique sont utilisées pour construire un modèle numérique de terrain (MNT) qui représente les élévations dans chaque point cartésien du terrain. Le MNT est une représentation numérique d’une carte topographique).</p>

La figure 10 montre un exemple de modèle MNT sous forme de matrice de deux dimensions, tel que :
* Chaque case représente un sommet de la carte.
* La ligne horizontale représente les abscisses cartésiennes (x) de chaque sommet.
* La ligne verticale représente les ordonnées cartésiennes (y) de chaque sommet.
* La valeur au centre de chaque case représente l’altitude.
* La valeur en bas à droite le numéro de chaque sommet.


<p align="center">
  <img src="Img/Fig_09.PNG" alt>
    <br>
    <em><b>Fig. 10 : un modèle numérique de terrain sous forme d’une matrice et son illustration en surface en termes d’altitudes et de coordonnées cartésiennes. La valeur au centre de chaque cellule de la matrice représente l’altitude et la valeur en bas à droite le numéro de chaque sommet.</b></em>
</p>


La distance plate entre deux sommets ![][1] et ![][2] de la carte est calculée en utilisant la distance euclidienne 2D, selon la formule suivante :

<p align="center">
  <img src=https://latex.codecogs.com/svg.latex?distanceEuclidienne\left(%20{{S_i},{S_j}}%20\right)%20=%20\sqrt%20{{{\left(%20{{X_i}%20-%20{X_j}}%20\right)}^2}%20+%20{{\left(%20{{Y_i}%20-%20{Y_j}}%20\right)}^2}}%20>
</p>

<p align='justify'> Cette distance ne représente pas la distance réelle parce qu’elle ne considère pas l’altitude. En effet la distance réelle est une distance à 3 dimensions qui augmente de valeur avec l’altitude (voir figure 11). 
  
La distance 3D entre deux sommets voisins ![][3]  et ![][4]  ayants comme altitudes respectives ![][5] et ![][6]  est:</p>
<p align="center">
  <img src= https://latex.codecogs.com/svg.latex?distance3D\left(%20{{S_i},{S_j}}%20\right)%20=%20\sqrt%20{distanceEuclidienne{{\left(%20{{S_i},{S_j}}%20\right)}^2}%20+%20{{\left(%20{altitud{e_i}%20-%20altitud{e_j}}%20\right)}^2}}
</p>


<p align="center">
  <img src="Img/Fig_10.PNG" alt>
    <br>
    <em><b>Fig. 11 : La distance entre deux sommets avec deux altitudes différentes.</b></em>
</p>


Deux sommets ![][1] et ![][2] sont voisin s’ils sont adjacents dans la carte c’est-à-dire :

<p align="center">
  <img src= https://latex.codecogs.com/svg.latex?\begin{array}{l}\left(%20{{X_i}%20-%20{X_j}}%20\right)%20=%200%20\;%20et%20\;%20\left(%20{{Y_i}%20-%20{Y_j}}%20\right)%20=%201%20\;%20ou\\%20\left(%20{{X_i}%20-%20{X_j}}%20\right)%20=%201%20\;%20et%20\;%20\left(%20{{Y_i}%20-%20{Y_j}}%20\right)%20=%200%20\;%20ou\\%20\left(%20{{X_i}%20-%20{X_j}}%20\right)%20=%201%20\;%20et%20\;%20\left(%20{{Y_i}%20-%20{Y_j}}%20\right)%20=%201%20\end{array}
</p>
  
<p align='justify'> L’un des objectifs de ce travail est de calculer le plus court chemin entre les sommets d’une carte topographique. Pour ce faire, il faut (transformer le modèle MNT en une matrice d’adjacente), en suivant ces étapes:</p>

  * <p align='justify'> Les sommets de la carte topographique formeront les nœuds du graphe. Donc, si le nombre des sommets de la matrice est égale à <b>n</b> alors la dimension de la matrice d’adjacente <b>M</b>  est égale à <b>n x n</b> ;</p>
  * La distance entre deux sommets voisins constitue le poids des arcs du graphe. Donc, ![][7] si i et j sont des sommets voisins dans la carte et ![][8] dans le cas contraire.

Par exemple, la carte de la figure 10 est transformée en une matrice d’adjacente M de dimensions <b>30 x 30</b> et ![][9] mais ![][10] est égal à -1 car les sommets 1 et 25 ne sont pas des sommets voisins.

## 3. Modules à implémenter <a name="module"></a>

La figure 12 représente l'arbre des appels de fonctions à implémenter.

<p align="center">
  <img src="Img/Imp_01.png" alt>
    <br>
    <em><b>Fig. 12 :Arbre des appels de fonctions.</b></em>
</p>

### 3.1. Module algo:<a name="algo"></a> 

<dl>
  <dt>3.1.1. indiceMinimum(vec):</dt>
  <dd><p align='justify'>Trouve l’indice et la valeur minimum dans un vecteur. La fonction ne doit pas considérer les cases avec une valeur de -1. Si toutes les cases sont à -1, 	on retourne le minimum -1 et l’indice -1.
  </p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b> vec[1xn]</b>: Vecteur des valeurs à parcourir.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>indice[1x1]</b>: l’indice de la case minimum.</li>
			<li><b>minim[1x1]</b>: la valeur minimum du vecteur.</li>
  	</ul></ol>
		<dd><p align='justify'><code> <b>Note:</b> Valide que vec est une liste de valeurs numériques plus grandes ou égales à -1s.</code></p></dd>

</dl>	

<dd><b>Exemple:</b></dd>

```python
vec     = [-1, 4, 6, -1, -1, 3, 5]
indice, minimum = indiceMinimum(vec)
txt = "la valeur minimale du vecteur est {} à la position {}"
print(txt.format(minimum, indice))
```

    la valeur minimale du vecteur et 3 à la position 5
-------------------------------------------------------------------------------------------------------------------------------------------------------


<dl>
  <dt> 3.1.2. noeudMinimalNonVisitesDeNoeud(matrice, nœud, noeudsVisites):</dt>
  <dd><p align='justify'>Cherche le nœud non visité ayant le poids minimum autour d’un nœud spécifique. Recherche seulement les liens au nœud initial. Retourne le nœud minimum. 	et son poids.
  </p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>Matrice[mxn]</b>: Matrice d’adjacence.</li>
			<li><b>noeud[1x1]</b>: Le nœud autour duquel on veut chercher le nœud non visité minimum.</li>
			<li><b>noeudsVisites[1xn]</b>: La liste des nœuds visités.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>nœuds[1x1]</b>: Noeud voisin avec la distance minimum.</li>
			<li><b>poids[1x1]</b>: Poids du nœud voisin avec la distance minimum.</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note:</b> Valide que la matrice est carrée et que les valeurs sont plus grandes ou égales à -1. Valide que le nœud est un entier positif 			scalaire. Valide que les nœuds visités est un vecteur de nombres entiers positifs. Valide que le nœud fait partie des nœuds visités.</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
noeud   = 1
noeudsVisites = [1]
indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeudsVisites)
txt = "le poids minimum du noeud non visité est {} à la position {}"
print(txt.format(minimum, indice))
```

    le poids minimum du noeud non visités est 12 à la position 2

-------------------------------------------------------------------------------------------------------------------------------------------------------


<dl>
  <dt>3.1.3. noeudMinimalNonVisites(matrice, noeudsVisites):</dt>
  <dd><p align='justify'> Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins. Retourne le nœud visité et le nœud non-visité ayant le poids minimum.
  </p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>Matrice[mxn]</b>:  Matrice d’adjacence.</li>
			<li><b>noeudsVisites[1xn]</b>: VLa liste des nœuds visités.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>depart[1x1]</b>: le nœud visité.</li>
			<li><b>arrive[1x1]</b>: le nœuds ayant le plus petit poids avec le nœud de départ.</li>
  	</ul></ol>
		<dd><p align='justify'><code> <b>Note:</b> Valide que la matrice est carrée et que les valeurs sont plus grandes ou égales à -1. Valide que les nœuds visités est un 
		vecteur de nombres entiers positifs..</code></p></dd>
</dl>	


<dd><b>Exemple:</b></dd>

```python
matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
noeudsVisites = [1, 2, 3]
depart, arrive = noeudMinimalNonVisites(matrice, noeudsVisites)
txt = "Le noeud de départ est le noeud {} et le noeud 'non-visité' ayant le plus \n petit poids de avec le noeud de départ est le noeud {}"
print(txt.format(depart, arrive))
```

    Le noeud de départ est le noeud 1 et le noeud 'non-visié' ayant le plus \n petit poids de avec le noeud de départ est le noeud 0
-------------------------------------------------------------------------------------------------------------------------------------------------------


<dl>
  <dt>3.1.4. noeudsVoisins(matrice, nœud):</dt>
  <dd><p align='justify'>Cherche les nœuds voisins et leur poids par rapport à un nœud initial. Les nœuds voisins ont un poids différent de -1 dans la matrice d’adjacence.</p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>Matrice[mxn]</b>: Matrice d’adjacence.</li>
			<li><b>nœud[1x1]</b>: Indice du nœud auquel on veut trouver les voisins.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>noeuds[1xn]</b>: Vecteur des nœuds voisins.</li>
			<li><b>poids[1xn]</b>: Vecteur des poids des nœuds voisins.</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note:</b> Valide que la matrice est carrée et de valeurs plus grande ou égale à -1. Valide que le nœud initial est une entier positif scalaire. </code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
noeud = 1
noeuds, poids = noeudsVoisins(matrice, noeud)
txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
print(txt.format(noeuds, poids, noeud))
```

    les noeuds voisin sont [0, 2, 3] et leur poids [20, 12, 17] rapport à un noeud 1

-------------------------------------------------------------------------------------------------------------------------------------------------------
<dl>
  <dt>3.1.5. dijkstra (matrice, depart, arrive):</dt>
  <dd><p align='justify'>Calcule le plus court chemin entre un nœud de départ et un nœud d’arrivée. Retourne la distance (poids total entre le chemin entre deux nœuds) entre le 
		nœud de départ et le nœud d’arrivée. Retourne aussi le vecteur de prédécesseur qui indique le nœud précédent pour se rendre au nœud de départ.</p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>Matrice[mxn]</b>: Matrice d’adjacence.</li>
			<li><b>depart[1x1]</b>: Le nœud de départ.</li>
			<li><b>arrive[1x1]</b>: Le nœud d’arrivé.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>distance[1x1]</b>: la somme des poids entre le nœud de départ et l’arrivé.</li>
			<li><b>predecesseur[1xn]</b>: vecteur des nœuds précédent pour se rendre au départ.</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note:</b> Valider que la matrice est carrée et que ses valeurs sont plus grandes ou égales à -1. Valider que le départ et l’arrivée sont 	des entiers positifs scalaires.</code></p></dd>
	<dd><p align='justify'><code> <b>Avertissement:</b> Faite référence à l’explication de l’algorithme de Dijkstra pour implémenter cette fonction.</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
depart  = 0
arrive  = 3
indice, prédécesseurs = dijkstra(matrice, depart, arrive)
txt = "la distance la plus cours entre un noeud de départ {} et un noeud d’arrivée {} est {} avec les prédécesseurs {}"
print(txt.format(depart, arrive, indice, prédécesseurs))
```

    la distance la plus cours entre un noeud de départ 0 et un noeud d’arrivée 3 est 37 avec les prédécesseurs [-1, 0, 1, 1]
    

-------------------------------------------------------------------------------------------------------------------------------------------------------
### 3.2. Module carte:<a name="carte"></a>

<dl>
  <dt>3.2.1. distanceEuclidienne(sommet1, sommet2):</dt>
  <dd><p align='justify'>Calcule la distance euclidienne entre deux sommets avec l’équation suivante:</p></dd>
<p align="center">
  <img src=https://latex.codecogs.com/svg.latex?distanceEuclidienne\left(%20{{S_i},{S_j}}%20\right)%20=%20\sqrt%20{{{\left(%20{{X_i}%20-%20{X_j}}%20\right)}^2}%20+%20{{\left(%20{{Y_i}%20-%20{Y_j}}%20\right)}^2}}%20>
</p>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>sommet1[1x1 dictionnaire]</b>: Le premier sommet.</li>
			<li><b>sommet2[1x1 dictionnaire]</b>: Le deuxième sommet.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>distance[1x1]</b>:La distance euclidienne entre les deux sommets.</li>
  	</ul></ol>
<dd><p align='justify'><code> <b>Note:</b>  Valide que les deux sommets sont des dictionnaires de sommet. </code></p></dd>
</dl>	


<dd><b>Exemple:</b></dd>

```python
sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
sommet2 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
txt = "la distance euclidienne entre les deux sommets est: {:.2f}"
print(txt.format(distanceEuclidienne(sommet1, sommet2)))
```

    la distance euclidienne entre les deux sommets est: 2.24
    
-------------------------------------------------------------------------------------------------------------------------------------------------------

<dl>
  <dt>3.2.2. distance3D(sommet1, sommet2):</dt>
  <dd><p align='justify'>Calcule la distance 3D entre deux sommets avec l’équation suivante:</p></dd>
	<p align="center">
  <img src= https://latex.codecogs.com/svg.latex?distance3D\left(%20{{S_i},{S_j}}%20\right)%20=%20\sqrt%20{distanceEuclidienne{{\left(%20{{S_i},{S_j}}%20\right)}^2}%20+%20{{\left(%20{altitud{e_i}%20-%20altitud{e_j}}%20\right)}^2}}
</p>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>sommet1[1x1 dictionnaire]</b>: Le premier sommet.</li>
			<li><b>sommet2[1x1 dictionnaire]</b>: Le deuxième sommet.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>distance[1x1]</b>:La distance 3D entre les deux sommets.</li>
  	</ul></ol>
<dd><p align='justify'><code> <b>Note:</b> Valide que les deux sommets sont des dictionnaires de sommet.</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
sommet2 = {'no': 1, 'x': 2, 'y': 2, 'altitude': 12}
txt = "la distance 3D entre les deux sommets est: {:.2f}"
print(txt.format(distance3D(sommet1, sommet2)))
```

    la distance 3D entre les deux sommets est: 8.31
    
-------------------------------------------------------------------------------------------------------------------------------------------------------
<dl>
  <dt>3.2.3. estVoisin(sommet1,  sommet2):</dt>
  <dd><p align='justify'>Valide que deux sommets sont voisins d’après leur emplacement en x et y sur la carte topographique. Les sommets sont voisins si:</p></dd>
	<p align="center">
  <img src= https://latex.codecogs.com/svg.latex?\begin{array}{l}\left(%20{{X_i}%20-%20{X_j}}%20\right)%20=%200%20\;%20et%20\;%20\left(%20{{Y_i}%20-%20{Y_j}}%20\right)%20=%201%20\;%20ou\\%20\left(%20{{X_i}%20-%20{X_j}}%20\right)%20=%201%20\;%20et%20\;%20\left(%20{{Y_i}%20-%20{Y_j}}%20\right)%20=%200%20\;%20ou\\%20\left(%20{{X_i}%20-%20{X_j}}%20\right)%20=%201%20\;%20et%20\;%20\left(%20{{Y_i}%20-%20{Y_j}}%20\right)%20=%201%20\end{array}
</p>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>sommet1[1x1 dictionnaire]</b>: Le premier sommet.</li>
			<li><b>sommet2[1x1 dictionnaire]</b>: Le deuxième sommet.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>distance[1x1]</b>: Vrai si les sommets sont voisins. Les sommets sont voisins si leurs valeurs en x ou en y sont à maximum 1 de distance.</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note: Valide que le  sommet est un dictionnaire de sommet.</b> </code></p></dd>
</dl>	

<dd><b>Exemple 1:</b></dd> 

```python
sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
sommet2 = {'no': 2, 'x': 1, 'y': 1, 'altitude': 12}
txt = "les deux noeuds sont ils voisin? {}"
print(txt.format(estVoisin(sommet1, sommet2)))
```

    les deux noeuds sont ils voisin? True
    
<dd><b>Exemple 2:</b></dd>

```python
sommet1 = {'no': 1, 'x': 0, 'y': 1, 'altitude': 4}
sommet2 = {'no': 3, 'x': 2, 'y': 2, 'altitude': 12}
txt = "les deux noeuds sont ils voisin? {}"
print(txt.format(estVoisin(sommet1, sommet2)))
```

    les deux noeuds sont ils voisin? False


	
-------------------------------------------------------------------------------------------------------------------------------------------------------
<dl>
  <dt>3.2.4. carteEnSommets(carteTopographique):</dt>
  <dd><p align='justify'>Converti les altitudes de la carte en tableau de sommets. Les sommets sont des dictionnaire avec les cles suivantes:</p></dd>
	<ol><ul>
		<li><b>no:</b> Numéro du sommet</li>
		<li><b>x:</b> Coordonnée X</li>
		<li><b>y:</b> Coordonnée Y</li>
		<li><b>altitude:</b> Altitude au sommet</li>
  	</ul></ol>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>carteTopographique[mxn]</b>: Carte topographique des altitudes.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>sommets[1x1 dictionnaire]</b>: dictionnaire des sommets de la carte</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note:</b> Valide que la carte topographique est de deux dimensions et de valeurs non négatives.</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
carteTopographique = [[12, 13], [23, 21]]
sommets = carteEnSommets(carteTopographique)
print("Le dictionnaire des sommets est: \n\t",sommets)
```

    Le dictionnaire des sommets est: 
    	 {'no': [0, 1, 2, 3], 'x': [0, 1, 0, 1], 'y': [0, 0, 1, 1], 'altitude': [12, 13, 23, 21]}
	 
-------------------------------------------------------------------------------------------------------------------------------------------------------
<dl>
  <dt>3.2.5. matriceAdjacence(sommets):</dt>
  <dd><p align='justify'>Retourne la matrice d’adjacence à partir d’un tableau de sommets. Construis la matrice en regardant chaque voisin possible dans la liste de sommets. Les cases sans lien sont assignées à -1. Consulté la section sur la carte topographique pour plus d’information sur l’implémentation.</p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>sommets[1x1 dictionnaire]</b>: Matrice d’adjacence des sommets.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>Matrice[nxn]</b>: la somme des poids entre le nœud de départ et l’arrivé.</li>
  	</ul></ol>
<dd><p align='justify'><code> <b>Note:</b> Valide que le  sommet est un dictionnaire de sommet</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
carteTopographique = [[12, 13], [23, 21]]
sommets = carteEnSommets(carteTopographique)
matAd = matriceAdjacence(sommets)
txt = "la matrice d'adjacense est: \n\t"
for i in matAd:
    for j in i:
        txt += "{:.3f}\t".format(j)
    txt += "\n\t"
print(txt)
```

    la matrice d'adjacense est: 
    	-1.000	1.414	11.045	9.110	
    	1.414	-1.000	10.100	8.062	
    	11.045	10.100	-1.000	2.236	
    	9.110	8.062	2.236	-1.000	
### 3.3. Module fichier:<a name="fichier"></a> 
-------------------------------------------------------------------------------------------------------------------------------------------------------
<dl>
  <dt>3.3.1. lireCarte(nomFichier):</dt>
  <dd><p align='justify'>Lit le fichier à partir du nom de fichier reçu en paramètre. Retourne la carte topographique lu dans le fichier.</p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>nomFichier[1xn char]</b>: Nom du fichier à lire.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>matrice[mxn]</b>: matrice des altitudes lut dans la carte topographique.</li>
  	</ul></ol>
<dd><p align='justify'><code> <b>Note:</b> Valide que le nom du fichier est une chaine de caractère.</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
nomFichier = 'carte.txt'
carte = lireCarte(nomFichier)
print("la carte lu est:")
for ligne in carte:
    print("\t", ligne)
```

    la carte lu est:
    	 [930, 927, 925, 926, 929]
    	 [928, 923, 920, 923, 927]
    	 [930, 926, 919, 925, 928]
    	 [927, 920, 917, 922, 929]
    	 [925, 919, 914, 920, 924]
    	 [924, 918, 913, 917, 919]

-------------------------------------------------------------------------------------------------------------------------------------------------------
<dl>
  <dt>3.3.2. chargeMatriceDeCarte(nomFichier):</dt>
  <dd><p align='justify'>Reçoit un nom de fichier et retourne la matrice d’adjacence correspondant au fichier lut. Pour se faire, la fonction va:</p></dd>
	<ol><ul>
			<li> Lire la carte.</li>
			<li> Convertir la carte en sommets.</li>
			<li> Convertir les sommets en matrice d’adjacence.</li>
  	</ul></ol>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>nomFichier[1xn char]</b>: Nom du fichier à lire.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>matrice[mxn]</b>: matrice d’adjacence trouver à partir du fichier lu.</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note:</b> Valide que le nom du fichier est une chaine de caractère</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
nomFichier = 'mini_carte.txt'
carte = chargeMatriceDeCarte(nomFichier)

txt = "matrice d'adjacense de la carte lu est: \n\t"
for i in carte:
    for j in i:
        txt += "{:.3f}\t".format(j)
    txt += "\n\t"
print(txt)
```

    matrice d'adjacense de la carte lu est: 
    	-1.000	3.162	5.099	1.732	
    	3.162	-1.000	2.449	4.123	
    	5.099	2.449	-1.000	6.083	
    	1.732	4.123	6.083	-1.000	
	
-------------------------------------------------------------------------------------------------------------------------------------------------------
### 3.4. Module interface<a name="interface"></a> 

<dl>
  <dt>3.4.1. saisirMatrice():</dt>
  <dd><p align='justify'>Saisit une matrice d’adjacence au clavier. Saisis le nombre de noeuds et le nombre de poids à avoir. Pour chaque poids, saisit les deux noeuds de chaque extrémité et saisit ensuite le poids.</p></dd>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>matrice[mxn]</b>: matrice d’adjacence saisit au clavier.</li>
			<li><b>predecesseur[1xn]</b>: vecteur des nœuds précédent pour se rendre au départ.</li>
  	</ul></ol>
</dl>	

```python
matrice = aisirMatrice()
```

    Donner le nombre de noeuds dans la matrice: 3
    Donner le nombre de poids dans la matrice: 2
    
    	 Saisir le poids  0
    		 Donner le noeud dextrémité 1: 0
    		 Donner le noeud dextrémité 2: 1
    		 Saisir le poids: 10
    
    	 Saisir le poids  1
    		 Donner le noeud dextrémité 1: 2
    		 Donner le noeud dextrémité 2: 1
    		 Saisir le poids: 5
	
    matrice =  [[-1, 10, -1], [10, -1, 5], [-1, 5, -1]]

    
-------------------------------------------------------------------------------------------------------------------------------------------------------
<dl>
  <dt>3.4.2. genereMatriceAleatoire(nNoeuds):</dt>
  <dd><p align='justify'>Génère une matrice d’adjacence de manière aléatoire. Le poids maximum entre les noeuds est de 99. La matrice d’adjacence généré doit avoir en moyenne la moitié des noeuds reliés l’un envers l’autre avec un poids. Par exemple, si on génère un tableau avec 20 noeuds, chaque noeud devrait avoir en moyenne 10 poids entre d’autres noeuds. Les noeuds non reliés auront un poids de -1.</p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>nNoeuds[1x1]</b>:  Le nombre de noeuds a généré dans la matrice.</li>
  	</ul></ol>
	<dd><b>Renvoie:</b></dd>
		<ol><ul>
			<li><b>matrice[nNoeudsxnNoeuds]</b>: matrice d’adjacence généré de manière aléatoire.</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note:</b> Valide que le nombre de noeuds est un entier scalaire positif.</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
nNoeuds = 5
matAlea = genereMatriceAleatoire(nNoeuds)
txt = "la matrice aléatoire est: \n\t"
for i in matAlea:
    for j in i:
        txt += "{}\t".format(j)
    txt += "\n\t"
print(txt)
```

    la matrice aléatoire est: 
    	22	-1	36	40	42	
    	-1	-1	-1	46	68	
    	36	-1	18	79	44	
    	40	46	79	28	-1	
    	42	68	44	-1	93	
	
-------------------------------------------------------------------------------------------------------------------------------------------------------


<dl>
  <dt>3.4.3. afficheChemin(predecesseurs, depart, arrive):</dt>
  <dd><p align='justify'>Affiche le chemin entre un nœud de départ et d’arrivé à partir du tableau de prédécesseurs.</p></dd>
  <dd><b>Paramètres:</b></dd>
		<ol><ul>
			<li><b>predecesseurs[1xn]</b>: vecteur des prédécesseurs.</li>
			<li><b>depart[1x1]</b>: Le nœud de départ du chemin.</li>
			<li><b>arrive[1x1]</b>: Le nœud d’arrivé du chemin.</li>
  	</ul></ol>
	<dd><p align='justify'><code> <b>Note:</b> Valide les prédécesseurs est un vecteur d’entier plus grand ou égal à -1 et différent de zéro. Valide que le nœud de départ et d’arrivée sont des scalaires entiers positifs.</code></p></dd>
</dl>	

<dd><b>Exemple:</b></dd>

```python
predecesseurs = [-1, 0, 0, 2, 5, 2]
depart = 0
arrive = 4
afficheChemin(predecesseurs, depart, arrive)
```

    Le chemin à parcourir est :
    	 DÉBUT : 0  ==> 2  ==> 5  ==>  4 : FIN 
	 
-------------------------------------------------------------------------------------------------------------------------------------------------------	
### 3.5. Module principal <a name="principale"></a> 

<dl>
  <dt>3.5.1. meilleurCheminDijkstra():</dt>
  <dd><p align='justify'>Programme principal de l’algorithme de Dijkstra. Donne 3 options à l’utilisateur:</p></dd>
	<ol><ul>
			<li>Saisir une matrice manuellement.</li>
			<li>Généré aléatoirement une matrice d’adjacence.</li>
			<li>Lire une carte topographique pour construire la matrice.</li>
  	</ul></ol>
</dl>	


## 4. Barème /20 <a name="bareme"></a>

|**Nom des fonctions**|**Nombre de points attribuer**|
| :- | :- |
|*indiceMinimum*|1|
|*noeudMinimalNonVisitesDeNoeud*|1|
|*noeudMinimalNonVisites*|1|
|*noeudsVoisins*|1|
|*dijkstra*|2|
|*estVoisin*|0.5|
|*distanceEuclidienne*|0.5|
|*distance3D*|1|
|*matriceAdjacence*|1.5|
|*carteEnSommets*|1.5|
|*lireCarte*|1.5|
|*chargeMatriceDeCarte*|1.5|
|*saisirMatrice*|1.5|
|*genereMatriceAleatoire*|1.5|
|*afficheChemin*|1.5|
|*meilleurCheminDijkstra*|1.5|

## Annexe: Guide et normes de codage <a name="annexe"></a>
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. 
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)


[0]: https://www.timeanddate.com/countdown/generic?iso=20211031T235959&p0=165&msg=Date+limite+remise+TP03+INF1007&font=cursive
[1]: https://latex.codecogs.com/svg.latex?{S_i}\left(%20{{X_i},{Y_i}}%20\right)
[2]: https://latex.codecogs.com/svg.latex?{S_j}\left(%20{{X_j},{Y_j}}%20\right)
[3]: https://latex.codecogs.com/svg.latex?{S_i}
[4]: https://latex.codecogs.com/svg.latex?{S_j}
[5]: https://latex.codecogs.com/svg.latex?{altitude_i}
[6]: https://latex.codecogs.com/svg.latex?{altitude_j}
[7]: https://latex.codecogs.com/svg.latex?M(i,j)%20=%20distance(i,j)
[8]: https://latex.codecogs.com/svg.latex?M(i,j)%20=%20-1
[9]: https://latex.codecogs.com/svg.latex?M(1,2)%20=%20distance(1,2)
[10]: https://latex.codecogs.com/svg.latex?M(1,25)
