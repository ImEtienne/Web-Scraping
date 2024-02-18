## Description du projet :
- Objectif : Programmer un bot pour le jeu "A Song of Link and Wire" se déroulant sur le wiki Game of Thrones.

### Fonctionnalités implémentées :
- Développement d'un programme répondant au problème spécifié, prenant en entrée deux pages du wiki et renvoyant un chemin de liens hypertexte entre ces deux pages, ou None s'il n'y a pas de chemin.
- Écriture de fonctions pour lister les liens hypertexte d'une page donnée, ainsi que pour construire et sauvegarder le graphe du wiki dans un fichier local.
- Implémentation de parcours de graphe (parcours en largeur et algorithme de Dijkstra) pour trouver le chemin le plus court entre deux pages, en tenant compte des poids des liens hypertexte basés sur la longueur des pages et le nombre de voyelles.

### Algorithme :
- Recherche d'un chemin entre deux pages du wiki en utilisant un parcours en largeur pour trouver un chemin valide entre les pages source et cible, puis en utilisant l'algorithme de Dijkstra pour trouver le chemin de poids minimal en tenant compte des poids spécifiés basés sur la longueur des pages et le nombre de voyelles.

