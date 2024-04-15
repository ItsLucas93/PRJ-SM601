"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Ce fichier est le fichier qui contient les fonctions de validation du graphe d'ordonnancement.
Version de Python : 3.12
"""
from termcolor import colored
from fonctions.graph_display import display_graph_matrix

def matrix_value_to_matrix_adjacency(matrix):
    """
    Convertir une matrice de valeurs en une matrice d'adjacence.
    """
    adjacency_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is not None:
                adjacency_matrix[i][j] = 1

    return adjacency_matrix


def matrix_adjacency_to_transitive_matrix(matrix):
    """
    Détection de la présence de circuit dans le graph
    Méthode appliqué : Matrice d’adjacence d’une fermeture transitive, obtention suivant la méthode de Roy-Warshall
    Source : https://fr.wikipedia.org/wiki/Algorithme_de_Warshall
     Roy-Warshall (C)
     pour k de 1 à n
       pour i de 1 à n
         pour j de 1 à n
           C[i,j] = C[i,j] or (C[i,k] and C[k,j])
     retourner C
    """
    transitive_matrix = [row[:] for row in matrix]

    for k in range(len(transitive_matrix)):
        for i in range(len(transitive_matrix)):
            for j in range(len(transitive_matrix)):
                transitive_matrix[i][j] = transitive_matrix[i][j] or (
                            transitive_matrix[i][k] and transitive_matrix[k][j])

    return transitive_matrix


def is_single_entry(adjacency_matrix):
    """
    Vérification de la présence d'un seul point d'entrée dans le graphe.
    Rappel: Un point d'entrée est un sommet ayant une colonne nulle. (Pas de sommets pointant vers lui)
    """
    entry_point = []
    for i in range(len(adjacency_matrix)):
        if sum([adjacency_matrix[j][i] for j in range(len(adjacency_matrix))]) == 0:
            entry_point.append(i)
    if len(entry_point) == 1:
        return entry_point[0], True
    return entry_point, False


def is_single_exit(adjacency_matrix):
    """
    Vérification de la présence d'une seule sortie dans le graphe.
    Rappel: Un point de sortie est un sommet ayant une ligne nulle. (Pas de sommets pointant vers lui)
    """
    exit_point = []
    for i in range(len(adjacency_matrix)):
        if sum([adjacency_matrix[i][j] for j in range(len(adjacency_matrix))]) == 0:
            exit_point.append(i)
    if len(exit_point) == 1:
        return exit_point[0], True
    return exit_point, False


def is_no_circuit(transitive_matrix):
    """
    Vérification de la présence de circuit dans le graphe.
    On part d'un graphe transitif et on vérifie que la diagonale est nulle.
    cf. Méthode 1 : Un graphe est sans circuit si la matrice d'adjacence M de sa fermeture transitive ne possède aucun 1 sur la diagonale.
    """
    for i in range(len(transitive_matrix)):
        if transitive_matrix[i][i] == 1:
            return False
    return True


def has_no_negative_edges(matrix):
    """
    Vérification de la présence d'arêtes négatives dans le graphe.
    On parcourt la matrice et on vérifie que les valeurs sont positives.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is not None and matrix[i][j] < 0:
                return False
    return True


def ordonnancement_validator(matrix, graph={}):
    """
    Vérification des propriétés du graphe d'ordonnancement.
    """
    # Construction de la matrice d'adjaence et transitive
    adjacency_matrix = matrix_value_to_matrix_adjacency(matrix)
    transitive_matrix = matrix_adjacency_to_transitive_matrix(adjacency_matrix)

    # Vérification de la présence d'un seul point d'entrée
    entry_point, is_single_entry_point = is_single_entry(adjacency_matrix)

    # Vérification de la présence d'une seule sortie
    exit_point, is_single_exit_point = is_single_exit(adjacency_matrix)

    # Vérification de l'absence de circuit
    is_no_circuit_graph = is_no_circuit(transitive_matrix)

    # Vérification de l'absence d'arêtes négatives
    has_no_negative_edges_graph = has_no_negative_edges(matrix)

    if is_single_entry_point and is_single_exit_point and is_no_circuit_graph and has_no_negative_edges_graph:
        print("Le graphe possède un seul point d'entrée : " + str(entry_point))
        print("Le graphe possède un seul point de sortie : " + str(exit_point))
        print("Le graphe ne possède pas de circuit.")
        print("Le graphe ne possède pas d'arêtes négatives.")
        print(colored("Le graphe est un graphe d'ordonnancement.", "green", attrs=["bold"]))
        return True
    else:
        if not is_single_entry_point:
            print(colored("Le graphe ne possède pas qu'un seul point d'entrée.", "red", attrs=["bold"]))
        else:
            print("Le graphe possède un seul point d'entrée : " + str(entry_point))
        if not is_single_exit_point:
            print(colored("Le graphe ne possède pas qu'un seul point de sortie.", "red", attrs=["bold"]))
        else:
            print("Le graphe possède un seul point de sortie : " + str(exit_point))
        if not is_no_circuit_graph:
            print(colored("Le graphe possède un circuit.", "red", attrs=["bold"]))
        else:
            print("Le graphe ne possède pas de circuit.")
        if not has_no_negative_edges_graph:
            print(colored("Le graphe possède des arêtes négatives.", "red", attrs=["bold"]))
        else:
            print("Le graphe ne possède pas d'arêtes négatives.")
    return False
