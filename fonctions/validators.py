"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Ce fichier est le fichier qui contient les fonctions de validation du graphe d'ordonnancement.
Version de Python : 3.12
"""

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
                transitive_matrix[i][j] = transitive_matrix[i][j] or (transitive_matrix[i][k] and transitive_matrix[k][j])

    return transitive_matrix


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

def ordonnancement_validator(matrix, graph={}):
    """
    Vérification des propriétés du graphe d'ordonnancement.
    """
    # Construction de la matrice d'adjaence et transitive
    adjacency_matrix = matrix_value_to_matrix_adjacency(matrix)
    transitive_matrix = matrix_adjacency_to_transitive_matrix(adjacency_matrix)
