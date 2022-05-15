# projet d'informatique Othello, Ali et Helder
## Comment lancer mon IA
-Lancer le programme lancement.py: si vous ne mettez rien dans le terminal lors du lancement du programme, le port de l'IA sera aléatoire et son nom sera:'ptitbot' accompagné de son port.
Si vous voulez choisir le port de votre IA ainsi que son nom , il suffit de lancer le programme lancement.py dans le terminal accompagné :
- En premier,du port que voulez. 
- En deuxième, de son nom.
Exemple: python lancement.py 2222 ALIHELDER 

## Description
Ce projet consiste à créer une IA jouant à Othello de la manière la plus optimale et intelligente possible. L'IA que nous avons créée se repose sur 3 fonctions principales:
- la fonction heuristic
- negamaxWithPruningIterativeDeepening
- cachedNegamaxWithPruningLimitedDepth

Avec ces trois fonctions, l'IA arrive à visualiser plusieurs états du jeu selon les coups joués à une profondeur limité par le temps. L'heuristic donne une valeur à chacun de ces états et permet aux deux autres fonctions de prendre le meilleur état à la profondeur atteinte.

L'heuristic possède plusieurs stratègies et donnera une valeur à chacun des états selon les conditions suivantes:
- D'abord, elle vérifie si le jeu n'est pas fini (fonction isGameOver) et renvoie +10000(fonction winner) si c'est le joueur principal(nous l'appelerons Mr. A) qui gagne et -10000 si c'est le joueur adverse qui gagne(Mr.B).Si c'est une égalité, alors elle renverra 0.
- Elle donne +10 si  Mr.A a un coin du plateau et -10 si c'est Mr.B qui l'a.
- Elle augmentera la valeur de l'état si le nombre de coups possibles de Mr.B diminue, de même si le nombre de coups possibles de Mr.A augmente.
- Si le nombre de pions joués sur le plateau est plus bas que 32, elle augmente la valeur de l'état selon le nombre  des 4 cases principales, qui sont déjà jouées au tout début , prises par Mr.A et l'état diminue selon le nombre de ces cases prises  par Mr.B . De plus, l'état augmente si le nombre de pion de Mr.B est plus grand que Mr.A et l'état diminue si c'est l'inverse.
- Si le nombre de pions joués sur le plateau est plus haut que(ou égal à) 32, l'état augmente si le nombre de cotés pris par Mr.A augmente mais aussi si le nombre de pions autour de ces cotés  pris par celui-ci augmente . Bien évidemment, l'état diminuera si c'est Mr.B qui possède tout cela.

Il est important de savoir que nous utilisons des threads pour laisser à notre IA un temps limité le plus grand possible  et ainsi être sûr que après ce temps, l'IA renvoie la dernière valeur obtenue. Nous voulons avoir un temps le plus grand possible pour ainsi avoir une profondeur maximale selon le temps donné et donc avoir un état du jeu qui permettra à l'IA d'avoir le maximum de chances de gagner.
