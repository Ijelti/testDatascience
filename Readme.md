



## L’objectif
Le projet fait l’analyse d’un fichier log pour retirer des informations nécessaires afin de segmenter les utilisateurs.

## Les outils 
Python, bibliothèque CSV

## Description de la méthode
L’algorithme du projet est basé sur la logique de la méthode 'MapReduce', il sert à mapper les types d’action pour chaque utilisateur, puis calculer le nombre d’actions ainsi que le segment de chaque utilisateur. Il contient trois fichiers. Les deux premiers fichiers  sont pour la partie du 'MapReduce'. Et le troisième fichier présente la fonction 'main' de notre projet. 

### Etape1: L’importation du fichier log
Comme première étape, j’ai utilisé la bibliothèque de python 'CSV' pour importer et lire le fichier log, puis j’ai récupérer les deux champs ( Iduser et TypeAction). Enfin, et pour mapper les données, j’ai créé un dictionnaire de données dont la clé est le 'Iduser'  et le 'TypeAction' comme valeur.  

### Etape2: Calcul des points et du segment 
La deuxième étape consiste à l’automatisation de la méthode de calcul des points pour chaque type d’action, puis la définition du segment pour chaque utilisateur tout en vérifiant l’intervalle dont lequel la somme des points appartient. Il s’agit de deux fonctions : la fonction 'intervallePoints' qui prend en paramètre le type d’action et la fonction 'intervalleSegment' qui prend en paramètre la somme des points.

### Etape3: segmentation des utilisateurs
La méthode 'segmentUser' présente la partie de la réduction de notre projet. Elle prend en paramètre notre dictionnaire de données puis elle applique les méthodes de calcul des points et du segment sur chaque utilisateur, et en même temps elle calcul leur nombre d’action.
Le output est un dictionnaire qui contient le 'iduser' comme clé et une liste du segment et le nombre des actions comme valeur.

### Etape4 : liaison entre les iduser et leurs emails 
Dans cette étape,  j’ai importé le fichier Database.csv qui contient les emails ainsi le iduser puis je les ai organisé en un dictionnaire de données. À ce stade on a deux dictionnaires de données qui ont la même clé, donc j’ai liée entre les deux tout en comparant les clés et écrire leurs valeurs dans un fichier csv avec un délimiteur « ; ».
Il s’agit de la fonction  'writterCsv' qui prend en paramètres les deux dictionnaires de données et le chemin du fichier de sortie. 

### Etape5 : Affichage
La dernière étape consiste à  la réalisation de la fonction 'main' qui regroupe l’ensemble des fonctions de notre projet. Et qui prend trois arguments d’entrée (respectivement les chemins de fichier log, Database et le fichier de sortie).
  

