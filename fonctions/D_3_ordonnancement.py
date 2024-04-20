"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Ce fichier est le fichier qui contient les fonctions d'ordonnancement du graphe.
Version de Python : 3.12
"""
from tabulate import tabulate
from termcolor import colored
import D_3_config as config

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
    date_per_predecessor_list, earliest_start_dates_list = earliest_dates(value_matrix)
    str_tab_3 = display_earliest_start_dates_per_predecessor(date_per_predecessor_list, predecessors_list, str_tab_2)
    str_tab_4, earliest_start_dates_list_line = display_earliest_start_dates(date_per_predecessor_list, earliest_start_dates_list, predecessors_list, str_tab_3)

    successors_list, str_tab_5 = display_successor(adjacency_matrix, str_tab)
    date_per_successors_list, latest_dates_list = latest_dates(ranks, value_matrix, earliest_start_dates_list, successors_list)
    str_tab_6 = display_latest_dates_per_successor(date_per_successors_list, successors_list, str_tab_5)
    str_tab_7, latest_dates_list_line = display_latest_finish_dates(date_per_successors_list, latest_dates_list, successors_list, str_tab_6)

    total_margins = total_margin(earliest_start_dates_list, latest_dates_list)
    critical_paths = find_critical_paths(adjacency_matrix, total_margins)
    str_tab_8 = display_margin_table(total_margins, earliest_start_dates_list_line, latest_dates_list_line, str_tab)

    critical_paths_str, i = display_critical_paths(critical_paths)

    # Affichage des résultats
    print("Rangs", ranks)
    print("Prédecesseurs", predecessors_list)
    print("Dates par prédécesseur", date_per_predecessor_list)
    print("Dates au plus-tôt", earliest_start_dates_list)
    print("Successeurs", successors_list)
    print("Dates par successeur", date_per_successors_list)
    print("Dates au plus-tard", latest_dates_list)
    print("Marges totales", total_margins)
    print("Chemin critique", critical_paths)

    # Tri du tableau par tri insertion
    # TODO: Trier le tableau en fonction du rang

    str_tab = sort_table_by_rank(str_tab, ranks)
    str_tab_2 = sort_table_by_rank(str_tab_2, ranks)
    str_tab_3 = sort_table_by_rank(str_tab_3, ranks)
    str_tab_4 = sort_table_by_rank(str_tab_4, ranks)
    str_tab_5 = sort_table_by_rank(str_tab_5, ranks)
    str_tab_6 = sort_table_by_rank(str_tab_6, ranks)
    str_tab_7 = sort_table_by_rank(str_tab_7, ranks)
    str_tab_8 = sort_table_by_rank(str_tab_8, ranks)

    # Affichage
    print("* " + colored("Rangs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tôt - Prédécesseurs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_2, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tôt - Dates par Prédécesseur :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_3, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tôt :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_4, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tard - Successeurs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_5, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tard - Dates par Successeurs:", attrs=["bold", "underline"]))
    print(tabulate(str_tab_6, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Dates au plus-tard :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_7, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    print("* " + colored("Marges totales & Chemins critiques :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_8, tablefmt="mixed_grid", numalign="center", stralign="center"))
    # Affichage des chemins critiques
    print("Nous sommes en présence de " + colored(str(i), "cyan", attrs=["bold"]) + " chemin(s) critique(s) :")
    print(critical_paths_str)
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
                    str_predecessor = "α"
            elif len(adjacency_matrix) - 1 in predecessor:
                if not config.notation:
                    str_predecessor = "ω"
            line3.append(colored(str_predecessor, attrs=["bold"]))
        predecessors.append(predecessor)

    str_copy = [line for line in str_tab]
    str_copy.append(line3)
    return predecessors, str_copy


def display_successor(adjacency_matrix, str_tab):
    """
    Fonction permettant d'afficher les successeurs dans le tableau
    """
    successors = []
    line3 = ["Successeurs"]
    for i in range(len(adjacency_matrix)):
        successor = []
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] != 0:
                successor.append(j)

        if not successor:
            line3.append(colored("--", attrs=["bold"]))
        else:
            str_successor = ""
            for s in successor:
                str_successor += str(s) + ", "
            str_successor = str_successor[:-2]

            if 0 in successor:
                # Construction du String
                if not config.notation:
                    str_successor = "α"
            elif len(adjacency_matrix) - 1 in successor:
                if not config.notation:
                    str_successor = "ω"
            line3.append(colored(str_successor, attrs=["bold"]))
        successors.append(successor)

    str_copy = [line for line in str_tab]
    str_copy.append(line3)
    return successors, str_copy


def earliest_dates(duration_matrix):
    date_per_predecessor = [0 for i in range(len(duration_matrix))]
    earliest_start_dates = [0 for i in range(len(duration_matrix))]

    duration_matrix = [[duration_matrix[i][j] for j in range(len(duration_matrix))] for i in range(len(duration_matrix))]
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


def latest_dates(tasks_ranks, duration_matrix, earliest_start_dates, successors_list):
    num_tasks = len(duration_matrix)
    latest_finish_dates = [float('inf')] * num_tasks
    date_per_successor = [[] for _ in range(num_tasks)]

    # Initialiser la date au plus tard pour le point de sortie (typiquement ω)
    latest_finish_dates[-1] = earliest_start_dates[-1]
    date_per_successor[-1] = [earliest_start_dates[-1]]

    # Créer une liste des tâches triées par rang en ordre décroissant
    tasks_sorted_by_rank = sorted(range(num_tasks), key=lambda x: tasks_ranks[x], reverse=True)

    # Deep copy
    successors_list = [[successor for successor in successors_list[i]] for i in range(num_tasks)]
    duration_matrix = [[duration_matrix[i][j] for j in range(num_tasks)] for i in range(num_tasks)]

    # Parcourir les tâches en respectant l'ordre de rang décroissant
    for task in tasks_sorted_by_rank:
        if successors_list[task]:
            list_of_dates = []
            for idx, successor in enumerate(successors_list[task]):
                if 0 <= successor < num_tasks and duration_matrix[task][successor] is not None:
                    calculated_date = latest_finish_dates[successor] - duration_matrix[task][successor]
                    list_of_dates.append(calculated_date)
                    date_per_successor[task].append(calculated_date)
                else:
                    # Maintenir l'alignement de l'index
                    date_per_successor[task].append(float('inf'))

            if list_of_dates:
                latest_finish_dates[task] = min(list_of_dates)
            else:
                latest_finish_dates[task] = earliest_start_dates[task]
        else:
            # Si aucune successeur n'est présent, la date au plus tard est égale à la date au plus tôt
            latest_finish_dates[task] = earliest_start_dates[task]

    return date_per_successor, latest_finish_dates


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


def display_latest_dates_per_successor(date_per_successor_list, successors_list, str_tab):
    """
    Afficher les dates de fin au plus tard par successeur.
    """
    # https://stackoverflow.com/questions/24391892/printing-subscript-in-python
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # string.translate(SUB)

    line4 = ["Dates par successeur"]
    for i in range(len(date_per_successor_list)):
        if date_per_successor_list[i] and successors_list[i] != []:
            str_dates = ""
            for date in range(len(date_per_successor_list[i])):
                str_dates += str(date_per_successor_list[i][date]) + str(successors_list[i][date]).translate(SUB) + ", "
            str_dates = str_dates[:-2]
            line4.append(colored(str_dates, attrs=["bold"]))
        elif date_per_successor_list[i] and successors_list[i] == []:
            line4.append(colored(str(date_per_successor_list[i][0]), attrs=["bold"]))
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
    return str_tab_copy, line5


def display_latest_finish_dates(date_per_successor_list, latest_finish_dates_list, successors_list, str_tab):
    """
    Afficher les dates de fin au plus tard.
    """
    # https://stackoverflow.com/questions/24391892/printing-subscript-in-python
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # string.translate(SUB)

    line5 = ["Dates au plus-tard"]
    for i in range(len(date_per_successor_list)):
        if date_per_successor_list[i] and successors_list[i] != []:
            str_dates = str(min(date_per_successor_list[i])) + str(successors_list[i][date_per_successor_list[i].index(min(date_per_successor_list[i]))]).translate(SUB)
            line5.append(colored(str_dates, attrs=["bold"]))
        elif date_per_successor_list[i] and successors_list[i] == []:
            line5.append(colored(str(date_per_successor_list[i][0]), attrs=["bold"]))
        else:
            line5.append(colored("0", attrs=["bold"]))

    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(line5)
    return str_tab_copy, line5


def sort_table_by_rank(str_tab, ranks):
    """
    Fonction permettant de trier le tableau par rang.
    """
    # Créer une liste d'indices triés basés sur les rangs
    sorted_indices = sorted(range(len(ranks)), key=lambda x: ranks[x])

    # Réorganiser chaque ligne du tableau selon les indices triés
    sorted_str_tab = []
    for line in str_tab:
        sorted_line = [line[0]]  # Conserver l'en-tête de la colonne
        sorted_line.extend([line[i + 1] for i in sorted_indices])
        sorted_str_tab.append(sorted_line)

    return sorted_str_tab


def total_margin(earliest_start_dates, latest_finish_dates):
    """
    Calculer les marges totales.
    """
    return [latest_finish_dates[i] - earliest_start_dates[i] for i in range(len(earliest_start_dates))]


def find_critical_paths(adjacency_matrix, margins):
    """
    Trouver tous les chemins critiques dans le graphe.
    Un chemin critique est défini comme un chemin où toutes les tâches ont une marge de zéro.
    """
    start_node = 0  # Habituellement, alpha est le point de départ dans le graphe d'ordonnancement
    end_node = len(adjacency_matrix) - 1  # Omega est le point final

    # Initialiser la liste des chemins critiques
    critical_paths = []

    # Fonction récursive pour explorer les chemins
    def dfs(current_node, path):
        # Ajouter le noeud actuel au chemin
        path.append(current_node)

        # Si le noeud actuel est le noeud de fin et que tous les noeuds dans le chemin sont critiques
        if current_node == end_node:
            # Vérifier si tous les noeuds dans le chemin ont une marge de zéro
            if all(margins[node] == 0 for node in path):
                critical_paths.append(path.copy())
        else:
            # Continuer à explorer les successeurs qui ont également une marge de zéro
            for successor in range(len(adjacency_matrix[current_node])):
                if adjacency_matrix[current_node][successor] > 0 and margins[successor] == 0:
                    dfs(successor, path)

        # Retirer le noeud actuel du chemin avant de revenir en arrière
        path.pop()

    # Commencer l'exploration à partir du noeud de départ
    dfs(start_node, [])

    return critical_paths


def display_margin_table(total_margins, earliest_start_dates_list_line, latest_dates_list_line, str_tab):
    """
    Afficher les marges totales.
    """
    line6 = ["Marges totales"]
    earliest_start_dates_list_line = [line for line in earliest_start_dates_list_line]
    latest_dates_list_line = [line for line in latest_dates_list_line]

    for i in range(len(total_margins)):
        if total_margins[i] == 0:
            line6.append(colored(str(total_margins[i]), "red", attrs=["bold"]))
            earliest_start_dates_list_line[i + 1] = colored(str(earliest_start_dates_list_line[i + 1]), "red", attrs=["bold"])
            latest_dates_list_line[i + 1] = colored(str(latest_dates_list_line[i + 1]), "red", attrs=["bold"])
        else:
            line6.append(colored(str(total_margins[i]), attrs=["bold"]))

    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(earliest_start_dates_list_line)
    str_tab_copy.append(latest_dates_list_line)
    str_tab_copy.append(line6)

    return str_tab_copy


def display_critical_paths(critical_paths):
    temp_str = ""
    i = 0
    for path in critical_paths:
        i += 1
        critical_path = str(i) + ".\t"
        for task in path:
            if not config.notation:
                if task == critical_paths[0][0]:
                    critical_path += "α" + " -> "
                elif task == critical_paths[0][-1]:
                    critical_path += "ω" + " -> "
                else:
                    critical_path += str(task) + " -> "
            else:
                critical_path += str(task) + " -> "
        critical_path = critical_path[:-4]
        temp_str += critical_path + "\n"
    return temp_str, i
