from tabulate import tabulate
from termcolor import colored

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

    print("* Création du graphe d’ordonnancement : "
          "\n" + str(cpt_sommets) + " sommets"
          "\n" + str(cpt_arcs) + " arcs")

    # Création d'un dictionnaire inversé pour faire apparaître les arcs triés par le numéro de tâche
    graph_dictionnary_flipped = {task_id: (duration, []) for task_id, (duration, predecessors) in graph_dictionnary.items()}
    for task_id, (duration, predecessors) in graph_dictionnary.items():
        for predecessor in predecessors:
            graph_dictionnary_flipped[predecessor][1].append(task_id)

    # Affiche les arcs
    for task_id in no_predecessors:
        print("α" + " -> " + str(task_id) + " = 0")

    sorted_tasks = sorted(graph_dictionnary_flipped.keys())
    for task_id in sorted_tasks:
        duration, successors = graph_dictionnary_flipped[task_id]
        for successor in successors:
            print(str(task_id) + " -> " + str(successor) + " = " + str(graph_dictionnary[successor][0]))
        if task_id in no_successors:
            print(str(task_id) + " -> ω = " + str(graph_dictionnary[task_id][0]))


def display_graph_matrix(graph_matrix):
    """
    Fonction permettant d'afficher la matrice du graphe.
    """
    # header = [""] + [colored(str(i), "cyan", attrs=["bold"]) for i in range(len(graph_matrix))]
    header = [""]
    for i in range(len(graph_matrix)):
        if i == 0:
            header.append(colored("α", "cyan", attrs=["bold"]))
        elif i == len(graph_matrix) - 1:
            header.append(colored("ω", "cyan", attrs=["bold"]))
        else:
            header.append(colored(str(i), "cyan", attrs=["bold"]))

    # body = [[colored(str(i), "cyan", attrs=["bold"])] + row for i, row in enumerate(graph_matrix)]
    body = []
    for i, row in enumerate(graph_matrix):
        if i == 0:
            body.append([colored("α", "cyan", attrs=["bold"])] + row)
        elif i == len(graph_matrix) - 1:
            body.append([colored("ω", "cyan", attrs=["bold"])] + row)
        else:
            body.append([colored(str(i), "cyan", attrs=["bold"])] + row)

    print(tabulate(body, headers=header, tablefmt="mixed_outline", numalign="center", stralign="center"))