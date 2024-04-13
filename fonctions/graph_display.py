from tabulate import tabulate
from termcolor import colored

def display_graph(graph):
    """
    Affichage du graphe comme un jeu de triplets, par exemple:

    * Création du graphe d’ordonnancement :
    7 sommets
    9 arcs
    0 -> 1 = 0
    0 -> 2 = 0
    1 -> 3 = 1
    1 -> 4 = 1
    2 -> 4 = 2
    2 -> 5 = 2
    3 -> 6 = 3
    4 -> 5 = 4
    5 -> 6 = 5
    """
    pass

def display_graph_matrix(matrix):
    """
    Fonction permettant d'afficher la matrice du graphe.
    """
    # header = [""] + [colored(str(i), "cyan", attrs=["bold"]) for i in range(len(matrix))]
    header = [""]
    for i in range(len(matrix)):
        if i == 0:
            header.append(colored("α", "cyan", attrs=["bold"]))
        elif i == len(matrix) - 1:
            header.append(colored("ω", "cyan", attrs=["bold"]))
        else:
            header.append(colored(str(i), "cyan", attrs=["bold"]))

    # body = [[colored(str(i), "cyan", attrs=["bold"])] + row for i, row in enumerate(matrix)]
    body = []
    for i, row in enumerate(matrix):
        if i == 0:
            body.append([colored("α", "cyan", attrs=["bold"])] + row)
        elif i == len(matrix) - 1:
            body.append([colored("ω", "cyan", attrs=["bold"])] + row)
        else:
            body.append([colored(str(i), "cyan", attrs=["bold"])] + row)

    print(tabulate(body, headers=header, tablefmt="mixed_outline", numalign="center", stralign="center"))