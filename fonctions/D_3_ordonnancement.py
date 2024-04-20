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
    * Fonction: ordonnencement_graph
    * ------------------------------
    * Cette fonction effectue tout les étapes de l'ordonnancement du graphe :
    * - Calcul des rangs
    * - Calcul des dates au plus tôt
    * - Calcul des dates au plus tard
    * - Calcul des marges totales
    * - Calcul du/des chemin(s) critique(s)
    * - Affichage des résultats (via les variables str_tab_x)
    * L'affichage reprend le design du pptx fourni en cours (cf. VI. Ordonnancement)
    * :param adjacency_matrix: Matrice d'adjacence du graphe
    * :param value_matrix: Matrice des valeurs du graphe
    """
    # Calcul des rangs
    ranks = rank_calculator(adjacency_matrix)
    str_tab = display_rank_matrix(ranks, value_matrix)

    # Calcul des dates au plus tôt par prédécesseur et des dates au plus tôt
    predecessors_list, str_tab_2 = display_predecessor(adjacency_matrix, str_tab)
    date_per_predecessor_list, earliest_start_dates_list = earliest_dates(value_matrix)

    # Récupération de l'affichage des dates au plus tôt dans le str_tab
    str_tab_3 = display_earliest_start_dates_per_predecessor(date_per_predecessor_list, predecessors_list, str_tab_2)
    str_tab_4, earliest_start_dates_list_line = display_earliest_start_dates(date_per_predecessor_list, predecessors_list, str_tab_3)

    # Calcul des dates au plus tard par successeur et des dates au plus tard
    successors_list, str_tab_5 = display_successor(adjacency_matrix, str_tab)
    date_per_successors_list, latest_dates_list = latest_dates(ranks, value_matrix, earliest_start_dates_list, successors_list)

    # Récupération de l'affichage des dates au plus tard dans le str_tab
    str_tab_6 = display_latest_dates_per_successor(date_per_successors_list, successors_list, str_tab_5)
    str_tab_7, latest_dates_list_line = display_latest_finish_dates(date_per_successors_list, successors_list, str_tab_6)

    # Calcul des marges totales et des chemins critiques
    total_margins = total_margin(earliest_start_dates_list, latest_dates_list)
    critical_paths = find_critical_paths(adjacency_matrix, total_margins)

    # Récupération de l'affichage des marges totales et des chemins critiques dans le str_tab
    str_tab_8 = display_margin_table(total_margins, earliest_start_dates_list_line, latest_dates_list_line, str_tab)
    critical_paths_str, i = display_critical_paths(critical_paths)

    # Tri du tableau par tri insertion, indexé par les rangs
    str_tab = sort_table_by_rank(str_tab, ranks)
    str_tab_2 = sort_table_by_rank(str_tab_2, ranks)
    str_tab_3 = sort_table_by_rank(str_tab_3, ranks)
    str_tab_4 = sort_table_by_rank(str_tab_4, ranks)
    str_tab_5 = sort_table_by_rank(str_tab_5, ranks)
    str_tab_6 = sort_table_by_rank(str_tab_6, ranks)
    str_tab_7 = sort_table_by_rank(str_tab_7, ranks)
    str_tab_8 = sort_table_by_rank(str_tab_8, ranks)

    # Affichage des résultats
    # Rangs
    print("* " + colored("Rangs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    # Dates au plus-tôt - Prédécesseurs
    print("* " + colored("Dates au plus-tôt - Prédécesseurs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_2, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    # Dates au plus-tôt - Dates par Prédécesseur
    print("* " + colored("Dates au plus-tôt - Dates par Prédécesseur :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_3, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    # Dates au plus-tôt
    print("* " + colored("Dates au plus-tôt :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_4, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    # Dates au plus-tard - Successeurs
    print("* " + colored("Dates au plus-tard - Successeurs :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_5, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    # Dates au plus-tard - Dates par Successeurs
    print("* " + colored("Dates au plus-tard - Dates par Successeurs:", attrs=["bold", "underline"]))
    print(tabulate(str_tab_6, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    # Dates au plus-tard
    print("* " + colored("Dates au plus-tard :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_7, tablefmt="mixed_grid", numalign="center", stralign="center"))
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

    # Marges totales & Chemins critiques
    print("* " + colored("Marges totales & Chemins critiques :", attrs=["bold", "underline"]))
    print(tabulate(str_tab_8, tablefmt="mixed_grid", numalign="center", stralign="center"))

    # Affichage des chemins critiques
    print("Nous sommes en présence de " + colored(str(i), "cyan", attrs=["bold"]) + " chemin(s) critique(s) :")
    print(critical_paths_str)
    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

def rank_calculator(adjacency_matrix):
    """
    * Fonction: rank_calculator
    * -------------------------
    * Calcule les rangs de tous les sommets du graphe.
    * Suit une version proche de l'algorithme vue en cours (cf. V. Rang d'un sommet)
    * :param adjacency_matrix: Matrice d'adjacence du graphe
    * :return: Liste des rangs de tous les sommets du graphe
    """
    # Initialisation des variables
    ranks = [-1 for i in range(len(adjacency_matrix))]
    d_minus = [0 for i in range(len(adjacency_matrix))]
    d_plus = [0 for i in range(len(adjacency_matrix))]

    for i in range(len(adjacency_matrix)):
        d_plus[i] = sum([adjacency_matrix[i][j] for j in range(len(adjacency_matrix))])

    for i in range(len(adjacency_matrix)):
        d_minus[i] = sum([adjacency_matrix[j][i] for j in range(len(adjacency_matrix))])

    # print("d_minus: ", d_minus)
    # print("d_plus: ", d_plus)

    # Initialisation de S (ensemble des sommets sans prédécesseurs)
    S = {i for i in range(len(adjacency_matrix)) if d_minus[i] == 0}
    k = 0

    # Algorithme de calcul des rangs (cf. cours V. Rang d'un sommet)
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


def display_rank_matrix(ranks, value_matrix):
    """
    * Fonction: display_rank_matrix
    * -----------------------------
    * Fonction permettant d'afficher la matrice des rangs. (cf. VI. Ordonnancement Page 9)
    * :param ranks: Liste des rangs de tous les sommets du graphe
    * :param value_matrix: Matrice des valeurs du graphe
    * :return: Tableau de la matrice des rangs
    """

    # Construction de la première ligne
    line1 = ["Rang"] + [colored(str(i), "cyan", attrs=["bold"]) for i in ranks]

    # Construction de la deuxième ligne, sous la forme sommet(durée)
    line2 = ["Tâche et sa longueur"]
    for i in range(len(value_matrix)):
        for j in range(len(value_matrix)):
            if value_matrix[i][j] is not None or i == len(value_matrix) - 1:
                if i == 0:
                    if not config.notation:
                        line2.append(colored("α", "cyan", attrs=["bold"]) + "(" + str(value_matrix[i][j]) + ")")
                    else:
                        line2.append(colored(str(i), "cyan", attrs=["bold"]) + "(" + str(value_matrix[i][j]) + ")")
                elif i == len(value_matrix) - 1:
                    if not config.notation:
                        line2.append(colored("ω", "cyan", attrs=["bold"]))
                    else:
                        line2.append(colored(str(i), "cyan", attrs=["bold"]))
                else:
                    line2.append(colored(str(i), "cyan", attrs=["bold"]) + "(" + str(value_matrix[i][j]) + ")")
                break

    return [line1, line2]


def display_predecessor(adjacency_matrix, str_tab):
    """
    * Fonction: display_predecessor
    * -----------------------------
    * Fonction permettant d'afficher les prédécesseurs dans le tableau (cf. VI. Ordonnancement Page 10)
    * :param adjacency_matrix: Matrice d'adjacence du graphe
    * :param str_tab: Tableau de la matrice des rangs
    * :return: Liste des prédécesseurs, String du tableau des prédécesseurs
    """
    # Construction de la liste des prédécesseurs
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

    # Copie du string et ajout de la liste des prédécesseurs dans le tableau
    str_copy = [line for line in str_tab]
    str_copy.append(line3)
    return predecessors, str_copy


def display_successor(adjacency_matrix, str_tab):
    """
    * Fonction: display_successor
    * -----------------------------
    * Fonction permettant d'afficher les successeurs dans le tableau (cf. VI. Ordonnancement Page 12)
    * :param adjacency_matrix: Matrice d'adjacence du graphe
    * :param str_tab: Tableau de la matrice des rangs
    * :return: Liste des successeurs, String du tableau des successeurs
    """
    # Construction de la liste des successeurs
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

    # Copie du string et ajout de la liste des successeurs dans le tableau
    str_copy = [line for line in str_tab]
    str_copy.append(line3)
    return successors, str_copy


def earliest_dates(value_matrix):
    """
    * Fonction: earliest_dates
    * -------------------------
    * Calcule les dates de début au plus tôt pour chaque tâche.
    * :param value_matrix: Matrice de valeurs
    * :return: Liste des dates de début au plus tôt par prédécesseur, Liste des dates de début au plus tôt
    """
    # Initialisation des variables
    date_per_predecessor = [0 for i in range(len(value_matrix))]
    earliest_start_dates = [0 for i in range(len(value_matrix))]

    # Deep copy
    value_matrix = [[value_matrix[i][j] for j in range(len(value_matrix))] for i in range(len(value_matrix))]

    # Remplacer les valeurs 'None' par 0
    for i in range(len(value_matrix)):
        for j in range(len(value_matrix)):
            if value_matrix[i][j] is None:
                value_matrix[i][j] = 0

    # Parcourir chaque tâche (en excluant 'alpha' qui est l'indice 0)
    for task in range(1, len(value_matrix)):
        # Trouver les prédécesseurs et calculer les dates de fin au plus tôt pour chaque tâche
        predecessors_finish_times = [
            earliest_start_dates[predecessor] + value_matrix[predecessor][task]
            for predecessor in range(len(value_matrix)) if value_matrix[predecessor][task] > 0
        ]

        # print(predecessors_finish_times)
        # Si la tâche a des prédécesseurs, la date de début au plus tôt est la plus grande date de fin de ses prédécesseurs
        if predecessors_finish_times:
            earliest_start_dates[task] = max(predecessors_finish_times)
        date_per_predecessor[task] = predecessors_finish_times

    return date_per_predecessor, earliest_start_dates


def latest_dates(ranks, value_matrix, earliest_start_dates, successors_list):
    """
    * Fonction: latest_dates
    * -----------------------
    * Calcule les dates de fin au plus tard pour chaque tâche.
    * :param ranks: Liste des rangs de tous les sommets du graphe
    * :param value_matrix: Matrice de valeurs
    * :param earliest_start_dates: Liste des dates de début au plus tôt
    * :param successors_list: Liste des successeurs
    * :return: Liste des dates de fin au plus tard par successeur, Liste des dates de fin au plus tard
    """
    # Initialisation des variables
    num_tasks = len(value_matrix)
    latest_finish_dates = [float('inf')] * num_tasks
    date_per_successor = [[] for _ in range(num_tasks)]

    # Initialiser la date au plus tard pour le point de sortie (typiquement ω)
    latest_finish_dates[-1] = earliest_start_dates[-1]
    date_per_successor[-1] = [earliest_start_dates[-1]]

    # Création d'une liste des tâches triées par rang en ordre décroissant en conservant l'index
    # Afin de traiter l'algorithme de calcul des dates de fin au plus tard dans l'ordre de rang décroissant
    tasks_sorted_by_rank = sorted(range(num_tasks), key=lambda x: ranks[x], reverse=True)

    # Deep copy des matrices
    successors_list = [[successor for successor in successors_list[i]] for i in range(num_tasks)]
    value_matrix = [[value_matrix[i][j] for j in range(num_tasks)] for i in range(num_tasks)]

    # Parcourir les tâches en respectant l'ordre de rang décroissant
    for task in tasks_sorted_by_rank:
        if successors_list[task]:
            list_of_dates = []
            # Calculer les dates de fin au plus tard pour chaque successeur
            for idx, successor in enumerate(successors_list[task]):
                if 0 <= successor < num_tasks and value_matrix[task][successor] is not None:
                    calculated_date = latest_finish_dates[successor] - value_matrix[task][successor]
                    list_of_dates.append(calculated_date)
                    date_per_successor[task].append(calculated_date)
                else:
                    # Maintenir l'alignement de l'index
                    date_per_successor[task].append(float('inf'))

            # Si la tâche a des successeurs, la date de fin au plus tard est la plus petite date de fin de ses successeurs
            if list_of_dates:
                latest_finish_dates[task] = min(list_of_dates)
            else:
                latest_finish_dates[task] = earliest_start_dates[task]

        # Si aucun successeur n'est présent, la date au plus tard est égale à la date au plus tôt
        else:
            latest_finish_dates[task] = earliest_start_dates[task]

    return date_per_successor, latest_finish_dates


def display_earliest_start_dates_per_predecessor(date_per_predecessor_list, predecessors_list, str_tab):
    """
    * Fonction: display_earliest_start_dates_per_predecessor
    * ------------------------------------------------------
    * Afficher les dates de début au plus tôt par prédécesseur.
    * :param date_per_predecessor_list: Liste des dates de début au plus tôt par prédécesseur
    * :param predecessors_list: Liste des prédécesseurs
    * :param str_tab: String d'affichage du tableau sur lequel la fonction va se rajouter
    * :return: String du tableau mis à jour
    """
    # https://stackoverflow.com/questions/24391892/printing-subscript-in-python
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # string.translate(SUB)

    # Création de la ligne
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

    # Deep copy du tableau et ajout de la ligne
    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(line4)
    return str_tab_copy


def display_latest_dates_per_successor(date_per_successor_list, successors_list, str_tab):
    """
    * Fonction: display_latest_dates_per_successor
    * --------------------------------------------
    * Afficher les dates de fin au plus tard par successeur.
    * :param date_per_successor_list: Liste des dates de fin au plus tard par successeur
    * :param successors_list: Liste des successeurs
    * :param str_tab: String d'affichage du tableau sur lequel la fonction va se rajouter
    * :return: String du tableau mis à jour
    """
    # https://stackoverflow.com/questions/24391892/printing-subscript-in-python
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # string.translate(SUB)

    # Création de la ligne
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

    # Deep copy du tableau et ajout de la ligne
    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(line4)
    return str_tab_copy


def display_earliest_start_dates(date_per_predecessor_list, predecessors_list, str_tab):
    """
    * Fonction: display_earliest_start_dates
    * --------------------------------------
    * Afficher les dates de début au plus tôt.
    * Le choix de ne pas se baser sur la liste earliest_start_dates est pour conserver la source des prédécesseurs.
    * :param date_per_predecessor_list: Liste des dates de début au plus tôt par prédécesseur
    * :param predecessors_list: Liste des prédécesseurs
    * :param str_tab: String d'affichage du tableau sur lequel la fonction va se rajouter
    * :return: String du tableau mis à jour
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


def display_latest_finish_dates(date_per_successor_list, successors_list, str_tab):
    """
    * Fonction: display_latest_finish_dates
    * -------------------------------------
    * Afficher les dates de fin au plus tard.
    * Le choix de ne pas se baser sur la liste latest_dates_list est pour conserver la source des successeurs.
    * :param date_per_successor_list: Liste des dates de fin au plus tard par successeur
    * :param successors_list: Liste des successeurs
    * :param str_tab: String d'affichage du tableau sur lequel la fonction va se rajouter
    * :return: String du tableau mis à jour
    """
    # https://stackoverflow.com/questions/24391892/printing-subscript-in-python
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # string.translate(SUB)

    # Création de la ligne
    line5 = ["Dates au plus-tard"]
    for i in range(len(date_per_successor_list)):
        if date_per_successor_list[i] and successors_list[i] != []:
            str_dates = str(min(date_per_successor_list[i])) + str(successors_list[i][date_per_successor_list[i].index(min(date_per_successor_list[i]))]).translate(SUB)
            line5.append(colored(str_dates, attrs=["bold"]))
        elif date_per_successor_list[i] and successors_list[i] == []:
            line5.append(colored(str(date_per_successor_list[i][0]), attrs=["bold"]))
        else:
            line5.append(colored("0", attrs=["bold"]))

    # Deep copy du tableau et ajout de la ligne
    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(line5)
    return str_tab_copy, line5


def sort_table_by_rank(str_tab, ranks):
    """
    * Fonction: sort_table_by_rank
    * -----------------------------
    * Tri du tableau par tri insertion, indexé par les rangs.
    * :param str_tab: Tableau à trier
    * :param ranks: Liste des rangs de tous les sommets du graphe
    * :return: Tableau trié
    """
    # Créer une liste d'indices triés basés sur les rangs
    sorted_indices = sorted(range(len(ranks)), key=lambda x: ranks[x])

    # Réorganiser chaque ligne du tableau selon les indices triés
    sorted_str_tab = []
    for line in str_tab:
        # Conservation de l'en-tête de la colonne
        sorted_line = [line[0]]
        sorted_line.extend([line[i + 1] for i in sorted_indices])
        sorted_str_tab.append(sorted_line)

    return sorted_str_tab


def total_margin(earliest_start_dates, latest_finish_dates):
    """
    * Fonction: total_margin
    * ----------------------
    * Calcul des marges totales.
    * :param earliest_start_dates: Liste des dates de début au plus tôt
    * :param latest_finish_dates: Liste des dates de fin au plus tard
    * :return: Liste des marges totales
    """
    return [latest_finish_dates[i] - earliest_start_dates[i] for i in range(len(earliest_start_dates))]


def find_critical_paths(adjacency_matrix, margins):
    """
    * Fonction: find_critical_paths
    * -----------------------------
    * Recherche des chemins critiques.
    * On utilise une fonction récursive pour explorer les chemins critiques.
    * Cette fonction rajoute à un chemin temporaire le noeud actuel, vérifie si le noeud actuel est le noeud de fin (si oui, rajoute ce chemin en chemin critique)
    * sinon vérifie que le noeud actuel a une marge de zéro (sinon s'arrête) et continue à explorer les successeurs qui ont également une marge de zéro.
    * :param adjacency_matrix: Matrice d'adjacence du graphe
    * :param margins: Liste des marges totales
    * :return: Liste des chemins critiques
    """
    # Soit alpha, le point de départ et omega, le point final
    start_node = 0
    end_node = len(adjacency_matrix) - 1

    # Initialiser la liste des chemins critiques
    critical_paths = []

    # Fonction récursive pour explorer les chemins
    def dfs(current_node, path):
        # Ajouter le noeud actuel au chemin
        path.append(current_node)
        print(path)

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
    * Fonction: display_margin_table
    * ------------------------------
    * Affichage des marges totales dans le tableau (cf. VI. Ordonnancement Page 13).
    * :param total_margins: Liste des marges totales
    * :param earliest_start_dates_list_line: Liste des dates de début au plus tôt
    * :param latest_dates_list_line: Liste des dates de fin au plus tard
    * :param str_tab: String d'affichage du tableau sur lequel la fonction va se rajouter
    * :return: String du tableau mis à jour
    """

    # Création de la ligne
    line6 = ["Marges totales"]
    # Deep copy des listes
    earliest_start_dates_list_line = [line for line in earliest_start_dates_list_line]
    latest_dates_list_line = [line for line in latest_dates_list_line]

    for i in range(len(total_margins)):
        if total_margins[i] == 0:
            line6.append(colored(str(total_margins[i]), "red", attrs=["bold"]))
            earliest_start_dates_list_line[i + 1] = colored(str(earliest_start_dates_list_line[i + 1]), "red", attrs=["bold"])
            latest_dates_list_line[i + 1] = colored(str(latest_dates_list_line[i + 1]), "red", attrs=["bold"])
        else:
            line6.append(colored(str(total_margins[i]), attrs=["bold"]))

    # Copie du tableau et ajout de la ligne
    str_tab_copy = [line for line in str_tab]
    str_tab_copy.append(earliest_start_dates_list_line)
    str_tab_copy.append(latest_dates_list_line)
    str_tab_copy.append(line6)

    return str_tab_copy


def display_critical_paths(critical_paths):
    """
    * Fonction: display_critical_paths
    * --------------------------------
    * Affichage des chemins critiques.
    * :param critical_paths: Liste des chemins critiques
    * :return: String des chemins critiques
    """
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
