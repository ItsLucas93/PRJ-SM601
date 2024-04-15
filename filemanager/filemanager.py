"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Ce fichier est le fichier qui lit les graphes, il permet de lister les fichiers .txt disponibles dans le dossier de testfiles ainsi que de le convertir en tableau de contraintes.
Version de Python : 3.12
"""
import os
from termcolor import colored

folder_path = "testfiles/"


def files_list(path=folder_path):
    """
    Lire et renvoie la liste des fichiers de test disponibles dans le dossier de testfiles.
    """
    index_test_files = {}
    try:
        files = os.listdir(path)
        if len(files) == 0:
            return colored(
                "Aucun fichier n'a été trouvé dans le dossier de " + colored(str(path), attrs=["bold", "underline"]),
                "red"), None
        for i in files:
            if i.split('.')[-1] != 'txt':
                files.remove(i)
        files.sort(key=lambda str: int(str.split()[1].split('.')[0]))  # ['table', 'x', '.txt']
        string = "\nFichiers disponibles dans le dossier : " + colored(str(path), attrs=["underline"]) + "\n"
        for i, file in enumerate(files):
            index_test_files[i + 1] = file
            string += str(i + 1) + ".\t" + file + "\n"
        index_test_files[len(index_test_files) + 1] = "Retour au menu principal"
        return string, index_test_files
    except FileNotFoundError:
        return colored("Le dossier de ", "red") + colored(str(path), "red", attrs=["bold", "underline"]) + colored(
            " n'a pas été trouvé.", "red"), None
    except Exception as e:
        return colored("Une erreur est survenue : " + str(e), "red"), None


def read_file(file, path=folder_path):
    """
    Lire un fichier contenant le graph et renvoie son contenu.
    """
    graph_dict = graph_dictionnary(file, path)
    graph_matri = graph_matrix(graph_dict, path=path)
    return graph_dict, graph_matri


def graph_dictionnary(file, path=folder_path):
    """
    Renvoie un dictionnaire des tâches.
    """
    tasks = {}
    try:
        with open(path + file, 'r') as file:
            for line in file:
                line = line.split()
                # Décomposition de la ligne
                task_id, duration, predecessors = int(line[0]), int(line[1]), [int(l) for l in line[2:]]
                tasks[task_id] = (duration, predecessors)
        return tasks
    except FileNotFoundError:
        return colored("Le fichier ", "red") + colored(str(file), "red", attrs=["bold", "underline"]) + colored(
            " n'a pas été trouvé.", "red"), None
    except Exception as e:
        return colored("Une erreur est survenue lors de la lecture du fichier : " + str(e), "red"), None


def graph_matrix(graph_dictionnary, path=folder_path):
    """
    Renvoie une matrice des valeurs à partir d'un graph_dictionnary.
    """
    max_sommets = max(graph_dictionnary.keys())

    # Initialise la matrice à None, matrix[0][x]/matrix[x][0] = α, matrix[n][x]/matrix[x][n] = ω
    matrix = [[None for i in range(max_sommets + 2)] for j in range(max_sommets + 2)]
    for task_id, (duration, predecessors) in graph_dictionnary.items():
        if not predecessors:
            matrix[0][task_id] = 0
        else:
            for predecessor in predecessors:
                matrix[predecessor][task_id] = graph_dictionnary[predecessor][0]

    for task_id, (duration, predecessors) in graph_dictionnary.items():
        if all(value is None for value in matrix[task_id]):
            matrix[task_id][max_sommets + 1] = graph_dictionnary[task_id][0]

    return matrix
