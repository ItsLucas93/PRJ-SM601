"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Ce fichier est le fichier qui contient les fonctions d'ordonnancement du graphe.
Version de Python : 3.12
"""
from tabulate import tabulate
from termcolor import colored
import config

"""
4. Calculer les rangs de tous les sommets du graphe.
5. Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges.
Pour le calcul du calendrier au plus tard, considérez que la date au plus tard de fin de projet
est égale à sa date au plus tôt.
6. Calculer le(s) chemin(s) critique(s) et les afficher
"""

def ordonnencement_graph(adjacency_matrix, value_matrix):
    """
    Fonction d'ordonnancement du graphe.
    """
    ranks = rank_calculator(adjacency_matrix)
    str_tab = display_rank_matrix(ranks, value_matrix)
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))
    str_tab = display_predecessor(adjacency_matrix, str_tab)
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))


def rank_calculator(adjacency_matrix):
    """
    Calculer les rangs de tous les sommets du graphe.
    """
    ranks = [0 for i in range(len(adjacency_matrix))]

    task_id = [i for i in range(len(adjacency_matrix))]
    d_minus = [0 for i in range(len(adjacency_matrix))]
    d_plus = [0 for i in range(len(adjacency_matrix))]

    for i in range(len(adjacency_matrix)):
        d_plus[i] = sum([adjacency_matrix[i][j] for j in range(len(adjacency_matrix))])

    for i in range(len(adjacency_matrix)):
        d_minus[i] = sum([adjacency_matrix[j][i] for j in range(len(adjacency_matrix))])

    # print("d_minus: ", d_minus)
    # print("d_plus: ", d_plus)

    ranks = [-1 for i in range(len(adjacency_matrix))]
    S = {i for i in range(len(adjacency_matrix)) if d_minus[i] == 0}
    k = 0

    while S:
        S_k_plus_1 = set()
        for i in S:
            ranks[i] = k
            for j in range(len(adjacency_matrix)):
                if adjacency_matrix[i][j] > 0:
                    d_minus[j] -= 1
                    if d_minus[j] == 0:
                        S_k_plus_1.add(j)
                # print(str(d_minus) + ' | ' + str(j) + ' \t ' + str(S) + ' \t ' + str(S_k_plus_1) + ' \t ' + str(
                # ranks))
        S = S_k_plus_1
        k += 1

    return ranks


def display_rank_matrix(ranks, matrix):
    """
    Fonction permettant d'afficher la matrice des rangs.
    """
    print("* " + colored("Rangs :", attrs=["bold", "underline"]))
    line1 = ["Rang"] + [colored(str(i), "cyan", attrs=["bold"]) for i in ranks]
    line2 = ["Tâche et sa longueur"]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is not None or i == len(matrix) - 1:
                if i == 0:
                    if not config.notation:
                        line2.append(colored("α", "cyan", attrs=["bold"]) + "(" + str(matrix[i][j]) + ")")
                    else:
                        line2.append(colored(str(i), "cyan", attrs=["bold"]) + "(" + str(matrix[i][j]) + ")")
                elif i == len(matrix) - 1:
                    if not config.notation:
                        line2.append(colored("ω", "cyan", attrs=["bold"]))
                    else:
                        line2.append(colored(str(i), "cyan", attrs=["bold"]))
                else:
                    line2.append(colored(str(i), "cyan", attrs=["bold"]) + "(" + str(matrix[i][j]) + ")")
                break
    else:
        pass
    print(tabulate([line1, line2], tablefmt="mixed_grid", numalign="center", stralign="center"))
    return [line1, line2]


def display_predecessor(adjacency_matrix, str_tab):
    """
    Fonction permettant d'afficher les prédécesseurs dans le tableau
    """
    print("* " + colored("Dates au plus-tôt - Prédécesseurs :", attrs=["bold", "underline"]))
    line3 = ["Prédécesseurs"]
    for i in range(len(adjacency_matrix)):
        predecessor = []
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[j][i] != 0:
                predecessor.append(j)

        if not predecessor:
            line3.append(colored("--", attrs=["bold"]))
        else:
            str_predecessor = ""
            for p in predecessor:
                str_predecessor += str(p) + ", "
            str_predecessor = str_predecessor[:-2]

            if 0 in predecessor:
                # Construction du String
                if not config.notation:
                    str_predecessor = "α" + str_predecessor[1:]
            elif len(adjacency_matrix) - 1 in predecessor:
                if not config.notation:
                    str_predecessor = str_predecessor[:-1] + "ω"
            line3.append(colored(str_predecessor, attrs=["bold"]))

    str_tab.append(line3)
    print(tabulate(str_tab, tablefmt="mixed_grid", numalign="center", stralign="center"))
    return str_tab
