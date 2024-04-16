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
    predecessors_list, str_tab_2 = display_predecessor(adjacency_matrix, str_tab)
    date_per_predecessor_list, earliest_start_dates_list = earliest_start_dates(value_matrix)
    str_tab_3 = display_earliest_start_dates_per_predecessor(date_per_predecessor_list, predecessors_list, str_tab_2)
    str_tab_4 = display_earliest_start_dates(date_per_predecessor_list, earliest_start_dates_list, predecessors_list, str_tab_3)

    # Tri du tableau par tri insertion
    str_tab = sort_table_by_rank(str_tab)
    str_tab_2 = sort_table_by_rank(str_tab_2)
    str_tab_3 = sort_table_by_rank(str_tab_3)
    str_tab_4 = sort_table_by_rank(str_tab_4)

    print(ranks)

    # Affichage
    print("* " + colored("Rangs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tôt - Prédécesseurs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_2, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tôt - Par Prédécesseur :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_3, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tôt :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_4, tablefmt="mixed_grid", numalign="center", stralign="center"))
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

    return [line1, line2]


def display_predecessor(adjacency_matrix, str_tab):
    """
    Fonction permettant d'afficher les prédécesseurs dans le tableau
    """
    predecessors = []
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
        predecessors.append(predecessor)

    str_copy = [line for line in str_tab]
    str_copy.append(line3)
    return predecessors, str_copy


def earliest_start_dates(duration_matrix):
    date_per_predecessor = [0 for i in range(len(duration_matrix))]
    earliest_start_dates = [0 for i in range(len(duration_matrix))]
    for i in range(len(duration_matrix)):
        for j in range(len(duration_matrix)):
            if duration_matrix[i][j] is None:
                duration_matrix[i][j] = 0

    # Parcourir chaque tâche (en excluant 'alpha' qui est l'indice 0)
    for task in range(1, len(duration_matrix)):
        # Trouver les prédécesseurs et calculer les dates de fin au plus tôt pour chaque tâche
        predecessors_finish_times = [
            earliest_start_dates[predecessor] + duration_matrix[predecessor][task]
            for predecessor in range(len(duration_matrix)) if duration_matrix[predecessor][task] > 0
        ]

        # print(predecessors_finish_times)
        # Si la tâche a des prédécesseurs, la date de début au plus tôt est la plus grande date de fin de ses prédécesseurs
        if predecessors_finish_times:
            earliest_start_dates[task] = max(predecessors_finish_times)
        date_per_predecessor[task] = predecessors_finish_times

    return date_per_predecessor, earliest_start_dates


def display_earliest_start_dates_per_predecessor(date_per_predecessor_list, predecessors_list, str_tab):
    """
    Afficher les dates de début au plus tôt par prédécesseur.
    """
    # https://stackoverflow.com/questions/24391892/printing-subscript-in-python
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # string.translate(SUB)

    line4 = ["Dates par prédécesseur"]
    for i in range(len(date_per_predecessor_list)):
        if date_per_predecessor_list[i]:
            str_dates = ""
            for date in range(len(date_per_predecessor_list[i])):
                str_dates += str(date_per_predecessor_list[i][date]) + str(predecessors_list[i][date]).translate(SUB) + ", "
            str_dates = str_dates[:-2]
            line4.append(colored(str_dates, attrs=["bold"]))
        else:
            line4.append(colored("0", attrs=["bold"]))

    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(line4)
    return str_tab_copy


def display_earliest_start_dates(date_per_predecessor_list, earliest_start_dates_list, predecessors_list, str_tab):
    """
    Afficher les dates de début au plus tôt.
    """
    # https://stackoverflow.com/questions/24391892/printing-subscript-in-python
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # string.translate(SUB)

    line5 = ["Dates au plus-tôt"]
    for i in range(len(date_per_predecessor_list)):
        if date_per_predecessor_list[i]:
            str_dates = str(max(date_per_predecessor_list[i])) + str(predecessors_list[i][date_per_predecessor_list[i].index(max(date_per_predecessor_list[i]))]).translate(SUB)
            line5.append(colored(str_dates, attrs=["bold"]))
        else:
            line5.append(colored("0", attrs=["bold"]))

    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(line5)
    return str_tab_copy


def sort_table_by_rank(str_tab):
    """
    Fonction permettant de trier le tableau par rang.
    Algorithmes de tri : Tri bubble
    """
    for i in range(2, len(str_tab)):
        flag = 0
        for j in range(1, len(str_tab)):
            if str_tab[0][j] > str_tab[0][j+1]:
                tmp = str_tab[0][j]
                str_tab[0][j] = str_tab[0][j+1]
                str_tab[0][j+1] = tmp
                flag = 1
                for k in range(1, len(str_tab)):
                    tmp = str_tab[k][j]
                    str_tab[k][j] = str_tab[k][j+1]
                    str_tab[k][j+1] = tmp

        if flag == 0:
            break

    return str_tab