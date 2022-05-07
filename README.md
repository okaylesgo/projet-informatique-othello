# projet d'informatique Othello, Ali et Helder
Ce projet consiste à créer une IA jouant à Othello de la manière la plus optimale et intelligente possible. L'IA que nous avons créée se repose sur 3 fonctions principales:
- la fonction heuristic
- negamaxWithPruningIterativeDeepening
- cachedNegamaxWithPruningLimitedDepth

Avec ces trois fonctions, l'IA arrive à visualiser plusieurs états du jeu selon les coups joués à une profondeur limité par le temps. L'heuristic donne une valeur à chacun de ces états et permet aux deux autres fonctions de prendre le meilleur état à la profondeur atteinte.

L'heuristic possède plusieurs stratègies et donnera une valeur à chacun des états selon les conditions suivantes:
- D'abord, elle vérifie si le jeu n'est pas fini (fonction isGameOver) et renvoi +10000(fonction winner) si c'est le joueur principal(nous l'appelerons Mr. A) qui gagne et -10000 si c'est le joueur adverse qui gagne(Mr.B).Si c'est une égalité, alors elle renverra 0.
- Elle donne +10 si  Mr.A a un coin du plateau et -10 si c'est Mr.B qui l'a.
- Elle augmentera la valeur de l'état si le nombre de coups possibles de Mr.B diminue, de même si le nombre de coups possibles de Mr.A augmente.
- Si le nombre de pions joués sur le plateau est plus bas que 32, elle augmente la valeur de l'état selon le nombre  des 4 cases principales, qui sont déjà jouées au tout début , prises par Mr.A et l'état diminue si c'est Mr.B qui en possède. De plus, l'état augmente si le nombre de pion de Mr.B est plus grand que Mr.A et l'état diminue si c'est l'inverse.
- Si le nombre de pions joués sur le plateau est plus haut que(ou égal à) 32, l'état augmente si le nombre de cotés sont pris par Mr.A mais aussi si le nombre de pions autour de ces cotés sont pris par celui-ci. Bien évidemment, l'état diminuera si Mr.B qui possède tout cela.

Il est important de savoir que nous utilisons des threads pour laisser à notre IA un temps limité le plus grand possible  et ainsi être sûr que après ce temps, l'IA renvoie la dernière valeur obtenue. Nous voulons avoir un temps le plus grand possible pour ainsi avoir une profondeur maximale et donc avoir un état du jeu qui permettra à l'IA de gagner le plus sûr.


C'est trois fonctions ne sont pas les seules utilisées, par exemple, nous avons toutes la partie réseau qui appelle plusieurs fonctions. Notamment, la fonction listen qui écoute le serveur et  lui envoie une réponse selon sa requête.
