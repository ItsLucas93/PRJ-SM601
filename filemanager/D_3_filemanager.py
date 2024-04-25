"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteur: KOCOGLU Lucas
Description: Ce fichier est le fichier qui lit les graphes, il permet de lister les fichiers .txt disponibles dans le dossier de testfiles ainsi que de le convertir en tableau de contraintes.
Version de Python : 3.12
"""
import os
from termcolor import colored

folder_path = "testfiles/"


def files_list(path=folder_path):
    """
    * Fonction: files_list
    * --------------------
    * Lit et renvoie la liste des fichiers de test disponibles dans le dossier enregistré dans la variable path.
    * Renvoie un message d'erreur si le dossier/fichiers n'est pas trouvé.
    * :param path: Chemin du dossier contenant les fichiers de test.
    * :return: Liste des fichiers de test disponibles, Dictionnaire des fichiers de test | En cas d'échec : Message d'erreur, None
    """
    # Dictionnaire des fichiers de test
    index_test_files = {}

    # Récupération de la liste de fichier
    try:
        files = os.listdir(path)
        if len(files) == 0:
            return colored(
                "Aucun fichier n'a été trouvé dans le dossier de " + colored(str(path), attrs=["bold", "underline"]),
                "red"), None
        # Construction d'une variable string pour l'affichage
        string = "\nFichiers disponibles dans le dossier : " + colored(str(path), attrs=["underline"]) + "\n"

        # Ajout de l'option de retour au menu principal
        index_test_files[0] = "Retour au menu principal"
        string += str(0) + ".\t" + index_test_files[0] + "\n"

        # Filtrage des fichiers .txt
        for i in files:
            if i.split('.')[-1] != 'txt':
                files.remove(i)

        # Tri des fichiers par ordre croissant
        files.sort(key=lambda str: int(str.split()[1].split('.')[0]))  # ['table', 'x', '.txt']

        # Ajout des fichiers à la liste des fichiers de test & à la variable string
        for i, file in enumerate(files):
            index_test_files[i + 1] = file
            string += str(i + 1) + ".\t" + file + "\n"
        return string, index_test_files
    except FileNotFoundError:
        return colored("Le dossier de ", "red") + colored(str(path), "red", attrs=["bold", "underline"]) + colored(
            " n'a pas été trouvé.", "red"), None
    except Exception as e:
        return colored("Une erreur est survenue : " + str(e), "red"), None


def read_file(file, path=folder_path):
    """
    * Fonction: read_file
    * --------------------
    * Lit un fichier contenant le graph et renvoie son contenu.
    * :param file: Nom du fichier à lire.
    * :param path: Chemin du dossier contenant les fichiers de test.
    * :return: Graphe sous format dictionnaire, Graphe sous format matriciel des valeurs
    """
    graph_dict = graph_dictionnary(file, path)
    graph_matri = graph_matrix(graph_dict)
    return graph_dict, graph_matri


def graph_dictionnary(file, path=folder_path):
    """
     * Fonction: graph_dictionnary
     * --------------------
     * Lit un fichier contenant le graph et renvoie son contenu sous forme de dictionnaire.
     * Renvoie un message d'erreur si le fichier n'est pas trouvé.
     * Structure du dictionnaire : {task_id: (duration, predecessors)}
     *       avec task_id : Identifiant de la tâche
     *       duration : Durée de la tâche
     *       predecessors : Liste des tâches précédentes
     * :param file: Nom du fichier à lire.
     * :param path: Chemin du dossier contenant les fichiers de test.
     * :return: Graphe sous format dictionnaire
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


def graph_matrix(graph_dictionnary):
    """
     * Fonction: graph_matrix
     * --------------------
     * Renvoie une matrice des valeurs à partir d'un graphe sous format dictionnaire.
     * :param graph_dictionnary: Graphe sous format dictionnaire
     * :return: Graphe sous format matriciel des valeurs
    """
    # Récupération du nombre de sommets
    max_sommets = max(graph_dictionnary.keys())

    # Initialise la matrice à None avec matrix[0][x]/matrix[x][0] = α, matrix[n][x]/matrix[x][n] = ω
    matrix = [[None for i in range(max_sommets + 2)] for j in range(max_sommets + 2)]

    # Remplissage de la matrice
    for task_id, (duration, predecessors) in graph_dictionnary.items():
        if not predecessors:
            matrix[0][task_id] = 0
        else:
            for predecessor in predecessors:
                matrix[predecessor][task_id] = graph_dictionnary[predecessor][0]

    # Création des sommets vers ω
    for task_id, (duration, predecessors) in graph_dictionnary.items():
        if all(value is None for value in matrix[task_id]):
            matrix[task_id][max_sommets + 1] = graph_dictionnary[task_id][0]

    return matrix
