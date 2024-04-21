# PRJ-SM601
Projet SM601 - Théorie des Graphes, Promotion 2026 (Année 2024)

## Description du projet

L'objectif de ce projet est de générer des graphes à partir de fichiers textes. 
Ces fichiers textes contiennent des informations sur les sommets et les arêtes du graphe.
Le programme doit lire ces fichiers, afficher ses informations à travers de matrices, et effectuer des opérations d'ordonnancement (dates au plus-tôt, dates au plus-tard, marges totales, chemins critiques).

## Structure du projet

Les données sont stockés dans le dossier `./testfiles/` nommées `table x.txt` où `x` est le numéro du graphe.
Les traces d'exécution sont stockés dans le dossier `./logs/` nommées `table x.txt` où `x` est le numéro du graphe.

### Structure du projet : 
```bash
./
├── LICENSE
├── README.md
├── D_3_main.py
├── D_3_config.py
├── filemanager
│      └── D_3_filemanager.py
├── fonctions
│      ├── D_3_graph_display.py
│      ├── D_3_ordonnancement.py
│      └── D_3_validators.py
├── logs
│      └── testfiles
│          ├── table 1.txt
│          [...]
│          └── table 16.txt
└── testfiles
    ├── table 1.txt
    [...]
    └── table 16.txt
```

### Exemple d'exécution :

```markdown
----------------------------------------------------------
Entrez le numéro du fichier à traiter : 16
----------------------------------------------------------
* Affichage du graphe :
12 sommets
16 arcs
α → 1 = 0
1 → 2 = 7
1 → 4 = 7
2 → 3 = 3
3 → 5 = 1
3 → 6 = 1
3 → 7 = 1
4 → 5 = 8
4 → 6 = 8
4 → 7 = 8
5 → 10 = 2
6 → 8 = 1
7 → 10 = 1
8 → 9 = 3
9 → 10 = 2
10 → ω = 1
Appuyez sur une touche pour continuer...
----------------------------------------------------------
* Matrice de valeurs :
┍━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━━┯━━━━━┑
│    │  α  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │  10  │  ω  │
┝━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━━┿━━━━━┥
│ α  │     │  0  │     │     │     │     │     │     │     │     │      │     │
│ 1  │     │     │  7  │     │  7  │     │     │     │     │     │      │     │
│ 2  │     │     │     │  3  │     │     │     │     │     │     │      │     │
│ 3  │     │     │     │     │     │  1  │  1  │  1  │     │     │      │     │
│ 4  │     │     │     │     │     │  8  │  8  │  8  │     │     │      │     │
│ 5  │     │     │     │     │     │     │     │     │     │     │  2   │     │
│ 6  │     │     │     │     │     │     │     │     │  1  │     │      │     │
│ 7  │     │     │     │     │     │     │     │     │     │     │  1   │     │
│ 8  │     │     │     │     │     │     │     │     │     │  3  │      │     │
│ 9  │     │     │     │     │     │     │     │     │     │     │  2   │     │
│ 10 │     │     │     │     │     │     │     │     │     │     │      │  1  │
│ ω  │     │     │     │     │     │     │     │     │     │     │      │     │
┕━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━━┷━━━━━┙
Appuyez sur une touche pour continuer...
* Matrice d'adjacence :
┍━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━━┯━━━━━┑
│    │  α  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │  10  │  ω  │
┝━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━━┿━━━━━┥
│ α  │  0  │  1  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0   │  0  │
│ 1  │  0  │  0  │  1  │  0  │  1  │  0  │  0  │  0  │  0  │  0  │  0   │  0  │
│ 2  │  0  │  0  │  0  │  1  │  0  │  0  │  0  │  0  │  0  │  0  │  0   │  0  │
│ 3  │  0  │  0  │  0  │  0  │  0  │  1  │  1  │  1  │  0  │  0  │  0   │  0  │
│ 4  │  0  │  0  │  0  │  0  │  0  │  1  │  1  │  1  │  0  │  0  │  0   │  0  │
│ 5  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1   │  0  │
│ 6  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1  │  0  │  0   │  0  │
│ 7  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1   │  0  │
│ 8  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1  │  0   │  0  │
│ 9  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1   │  0  │
│ 10 │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0   │  1  │
│ ω  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0   │  0  │
┕━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━━┷━━━━━┙
* Matrice transitive :
┍━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━┯━━━━━━┯━━━━━┑
│    │  α  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │  10  │  ω  │
┝━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━┿━━━━━━┿━━━━━┥
│ α  │  0  │  1  │  1  │  1  │  1  │  1  │  1  │  1  │  1  │  1  │  1   │  1  │
│ 1  │  0  │  0  │  1  │  1  │  1  │  1  │  1  │  1  │  1  │  1  │  1   │  1  │
│ 2  │  0  │  0  │  0  │  1  │  0  │  1  │  1  │  1  │  1  │  1  │  1   │  1  │
│ 3  │  0  │  0  │  0  │  0  │  0  │  1  │  1  │  1  │  1  │  1  │  1   │  1  │
│ 4  │  0  │  0  │  0  │  0  │  0  │  1  │  1  │  1  │  1  │  1  │  1   │  1  │
│ 5  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1   │  1  │
│ 6  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1  │  1  │  1   │  1  │
│ 7  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1   │  1  │
│ 8  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1  │  1   │  1  │
│ 9  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  1   │  1  │
│ 10 │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0   │  1  │
│ ω  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0  │  0   │  0  │
┕━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━┷━━━━━━┷━━━━━┙
Le graphe possède un seul point d'entrée : α
Le graphe possède un seul point de sortie : ω
Le graphe ne possède pas de circuit.
Le graphe ne possède pas d'arêtes négatives.
Le graphe est un graphe d'ordonnancement.
----------------------------------------------------------
Souhaitez-vous continuer ? (y/n)...
```

## Exécuter le programme

Le projet a été codé sur la version 3.12 de Python.
Il est demandé à l'utilisateur d'installer la version 3.12 de [Python](https://www.python.org/downloads/).

Pour vérifier la version de Python installée sur votre machine :
```bash
python3 --version
```

Avant de lancer votre programme, des modules tiers doivent être installés : `tabulate`, `termcolor`. Pour installer ces modules :
```bash
pip3 install tabulate termcolor
```

Pour lancer le programme, exécutez le fichier `D_3_main.py` (Soit par la commande sur votre terminal, soit dans un IDE type [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/download)) :
```bash
python3 D_3_main.py
```

## Auteurs du projet

Ce projet est proposé par [Helen KASSEL](https://eng.efrei.fr/department-of-mathematics/), coordinatrice du module SM601 - Théorie des Graphes à l'[Efrei Paris Panthéon Assas Université](https://www.efrei.fr/).

Groupe de projet (D-3) constitué de :
* BAUDET Antoine
* HOUEE Adrien
* SABBEH Chokri
* Lucas KOCOGLU