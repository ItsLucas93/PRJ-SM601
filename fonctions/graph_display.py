"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Fichier contenant les fonctions d'affichage du graphe.
Version de Python : 3.12
"""

from tabulate import tabulate
from termcolor import colored

import config

def display_graph_relations(graph_dictionnary):
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
    no_successors = set(graph_dictionnary.keys())
    no_predecessors = set()

    cpt_arcs = 0
    for task_id, (duration, predecessors) in graph_dictionnary.items():
        for predecessor in predecessors:
            no_successors.discard(predecessor)
            cpt_arcs += 1

    for task_id, (duration, predecessors) in graph_dictionnary.items():
        if not predecessors:
            no_predecessors.add(task_id)
            cpt_arcs += 1

    cpt_arcs += len(no_successors)
    cpt_sommets = len(graph_dictionnary) + 2

    print("* " + colored("Affichage du graphe :", attrs=["bold", "underline"]) +
          "\n" + str(cpt_sommets) + " sommets"
          "\n" + str(cpt_arcs) + " arcs")

    # Création d'un dictionnaire inversé pour faire apparaître les arcs triés par le numéro de tâche
    graph_dictionnary_flipped = {task_id: (duration, []) for task_id, (duration, predecessors) in graph_dictionnary.items()}
    for task_id, (duration, predecessors) in graph_dictionnary.items():
        for predecessor in predecessors:
            graph_dictionnary_flipped[predecessor][1].append(task_id)

    # Affiche les arcs
    for task_id in no_predecessors:
        if config.notation:
            print("0" + " → " + str(task_id) + " = 0")
        else:
            print("α" + " → " + str(task_id) + " = 0")

    sorted_tasks = sorted(graph_dictionnary_flipped.keys())
    for task_id in sorted_tasks:
        duration, successors = graph_dictionnary_flipped[task_id]
        for successor in successors:
            print(str(task_id) + " → " + str(successor) + " = " + str(graph_dictionnary[task_id][0]))
        if task_id in no_successors:
            if config.notation:
                print(str(task_id) + " → " + str(cpt_sommets - 1) + " = " + str(graph_dictionnary[task_id][0]))
            else:
                print(str(task_id) + " → ω = " + str(graph_dictionnary[task_id][0]))


def display_graph_matrix(graph_matrix, option=""):
    """
    Fonction permettant d'afficher la matrice du graphe.
    """

    if config.notation:
        header = [""] + [colored(str(i), "cyan", attrs=["bold"]) for i in range(len(graph_matrix))]
    else:
        header = [""]
        for i in range(len(graph_matrix)):
            if i == 0:
                header.append(colored("α", "cyan", attrs=["bold"]))
            elif i == len(graph_matrix) - 1:
                header.append(colored("ω", "cyan", attrs=["bold"]))
            else:
                header.append(colored(str(i), "cyan", attrs=["bold"]))

    if config.notation:
        body = [[colored(str(i), "cyan", attrs=["bold"])] + row for i, row in enumerate(graph_matrix)]
    else:
        body = []
        for i, row in enumerate(graph_matrix):
            if i == 0:
                body.append([colored("α", "cyan", attrs=["bold"])] + row)
            elif i == len(graph_matrix) - 1:
                body.append([colored("ω", "cyan", attrs=["bold"])] + row)
            else:
                body.append([colored(str(i), "cyan", attrs=["bold"])] + row)

    if option == "diag":
        for i in range(len(body)):
            for j in range(1, len(body[i])):
                if i == j - 1:
                    if body[i][j] == 0:
                        body[i][j] = colored(body[i][j], "light_green", attrs=["bold"])
                    else:
                        body[i][j] = colored(body[i][j], "light_red", attrs=["bold"])

    print(tabulate(body, headers=header, tablefmt="mixed_outline", numalign="center", stralign="center"))